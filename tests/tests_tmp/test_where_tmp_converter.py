"""Tests for temporal converter WHERE clause handling.

The temporal (trailing) WHERE clause requires a non-positive time window (it looks backward
from the prediction timestamp) -- see `TValidator.validate_aggregation`. This intentionally
differs from `PREDICT`/`ASSUMING` windows, which must be non-negative (forward-looking).

NOTE: a window `(start, end, UNIT)` covers `(ts+start, ts+end]` -- exclusive of the start
boundary, inclusive of the end boundary -- regardless of whether it looks forward or backward.
"""

import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


def test_where_filters_by_backward_looking_temporal_aggregation(temporal_converter):
    # Arrange: COUNT is coalesced to 0, so every (product, timestamp) pair exists before the
    # WHERE filter is applied; only the backward-looking LAST(...) IS NOT NULL check narrows it.
    rtgl_query = """
        PREDICT COUNT(reviews.reviewId, 0, 10, DAYS)
        FOR EACH products.productId
        WHERE LAST(reviews.rating, -10, 0, DAYS) IS NOT NULL;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert: at 2025-02-01 the backward window (2025-01-22, 2025-02-01] has no reviews at all
    # for any product, so nothing survives there. At 2025-02-10 the backward window
    # (2025-01-31, 2025-02-10] covers reviews 1-3: product 1's LAST rating is 3.0 (review 2,
    # the most recent of its two rows), product 2's is 4.0 (review 3), product 3 has none.
    expected = ref_df_from_csv("""
        fk, timestamp,  label
        1,  2025-02-10, 1.0
        2,  2025-02-10, 0.0
    """, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")


@pytest.mark.parametrize("op,expected_csv", [
    pytest.param("AND", """
        fk, timestamp,  label
        1,  2025-02-10, 1.0
    """, id="and"),
    pytest.param("OR", """
        fk, timestamp,  label
        1,  2025-02-01, 3.0
        2,  2025-02-01, 1.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 1.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, id="or"),
])
def test_nested_where_combines_temporal_aggregations(temporal_converter, op, expected_csv):
    # Arrange: cond1 = LAST(rating, -10, 0, DAYS) IS NOT NULL, true only for (1, 02-10) and
    # (2, 02-10) (see the test above). cond2 = the FIRST(comment, ...) group is true whenever
    # there is no comment in the backward window at all (IS NULL branch), or whenever the
    # earliest comment in that window starts with "O": at 2025-02-01 nothing has a comment
    # yet, so cond2 is true for every product; at 2025-02-10, product 1's earliest comment is
    # "OPT" (true), product 2's is "PRP" (false, no comment and no "O" prefix), product 3 has
    # none (true via the null branch). AND therefore keeps only (1, 02-10); OR keeps everything.
    # Note the forward window (0, 10, DAYS) on the PREDICT COUNT itself covers (ts, ts+10], so
    # product 1's count at 2025-02-01 is 3 (reviews 1, 2, and 4 -- 4 falls in-window here too).
    rtgl_query = f"""
        PREDICT COUNT(reviews.reviewId, 0, 10, DAYS)
        FOR EACH products.productId
        WHERE LAST(reviews.rating, -10, 0, DAYS) IS NOT NULL
        {op} (FIRST(reviews.comment, -10, 0, DAYS) IS NULL
        OR FIRST(reviews.comment, -10, 0, DAYS) STARTS WITH "O");
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv(expected_csv, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")
