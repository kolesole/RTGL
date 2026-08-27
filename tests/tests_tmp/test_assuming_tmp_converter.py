"""Tests for temporal converter ASSUMING clause handling.

ASSUMING requires a non-negative time window (it looks forward from the prediction timestamp,
same as PREDICT) -- see `TValidator.validate_aggregation`.
"""

import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


@pytest.mark.parametrize("op,expected_csv", [
    pytest.param("IS NULL", """
        fk, timestamp,  label
        1,  2025-02-01, 3.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 1.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, id="is_null"),
    pytest.param("IS NOT NULL", """
        fk, timestamp,  label
        2,  2025-02-01, 1.0
    """, id="is_not_null"),
])
def test_assuming_restricts_entity_timestamp_pairs(temporal_converter, op, expected_csv):
    # Arrange: a forward window (0, 10, DAYS) covers (ts, ts+10], so product 1's window at
    # 2025-02-01 includes review 4 (2025-02-11, null rating) alongside its two other reviews.
    # LAST is order-sensitive, so it picks review 4 (the chronologically last one) and comes
    # back null there, even though non-null ratings exist earlier in the same window. Product
    # 2 at 2025-02-01 is the only (product, timestamp) pair where LAST is non-null (4.0, from
    # its single review). Everywhere else LAST is null (no reviews in window at all, or -- for
    # product 1 at 2025-02-10 -- only review 4 again). COUNT is coalesced to 0, so every
    # (product, timestamp) pair is available before ASSUMING narrows it down.
    rtgl_query = f"""
        PREDICT COUNT(reviews.reviewId, 0, 10, DAYS)
        FOR EACH products.productId
        ASSUMING LAST(reviews.rating, 0, 10, DAYS) {op};
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv(expected_csv, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")
