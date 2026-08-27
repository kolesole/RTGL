"""Tests for temporal converter condition handling (PREDICT AGGR(...) <op> value).

`PREDICT AGGR(...) <op> value` compiles as a full condition (`build_expr`/`build_condition`),
whose label is `CASE WHEN __MAIN__.fk IS NOT NULL THEN TRUE ELSE FALSE END` -- i.e. it is a
row-existence check against the set of (entity, timestamp) pairs that satisfy the condition,
not a raw boolean column. A NULL aggregation therefore never produces a NULL label; it simply
never satisfies the condition, so it always resolves to False. Every (entity, timestamp) pair
is present in the output.
"""

import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


@pytest.mark.parametrize("op,expected_csv", [
    # AVG(rating, 0, 10, DAYS): (1, 02-01) -> 4.0, (2, 02-01) -> 4.0, everything else -> null
    # (no reviews, or none in that window) -> null never satisfies the comparison -> False
    pytest.param("!=", """
        fk, timestamp,  label
        1,  2025-02-01, True
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="not_equal"),
    pytest.param("<", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, False
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="less_than"),
    pytest.param("<=", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, False
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="less_than_or_equal"),
    pytest.param("==", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, False
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="equal"),
    pytest.param(">", """
        fk, timestamp,  label
        1,  2025-02-01, True
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="greater_than"),
    pytest.param(">=", """
        fk, timestamp,  label
        1,  2025-02-01, True
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="greater_than_or_equal"),
])
def test_predict_numeric_condition_on_aggregation(temporal_converter, op, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT AVG(reviews.rating, 0, 10, DAYS) {op} 3.5
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv(expected_csv, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")


@pytest.mark.parametrize("op,expected_csv", [
    # FIRST(comment, 0, 10, DAYS): (1, 02-01) -> "OPT", (2, 02-01) -> "PRP", (1, 02-10) ->
    # "ITM"; everything else is null (no reviews, or none in that window)
    pytest.param("CONTAINS", """
        fk, timestamp,  label
        1,  2025-02-01, True
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="contains"),
    pytest.param("NOT CONTAINS", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, False
        3,  2025-02-01, False
        1,  2025-02-10, True
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="not_contains"),
    pytest.param("LIKE", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, False
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="like"),
    pytest.param("NOT LIKE", """
        fk, timestamp,  label
        1,  2025-02-01, True
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, True
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="not_like"),
    pytest.param("STARTS WITH", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="starts_with"),
    pytest.param("ENDS WITH", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="ends_with"),
    pytest.param("=", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, False
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="equal"),
])
def test_predict_string_condition_on_aggregation(temporal_converter, op, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT FIRST(reviews.comment, 0, 10, DAYS) {op} "P"
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv(expected_csv, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")


@pytest.mark.parametrize("op,expected_csv", [
    # A forward window (0, 10, DAYS) covers (ts, ts+10], so product 1's window at 2025-02-01
    # includes review 4 (2025-02-11, null rating) alongside its two other reviews. LAST is
    # order-sensitive, so it picks review 4 (the chronologically last one) and comes back null
    # there, even though non-null ratings exist earlier in the same window. LAST(rating, 0, 10,
    # DAYS): (2, 02-01) -> 4.0 (the only non-null case), everything else -> null.
    pytest.param("IS NULL", """
        fk, timestamp,  label
        1,  2025-02-01, True
        2,  2025-02-01, False
        3,  2025-02-01, True
        1,  2025-02-10, True
        2,  2025-02-10, True
        3,  2025-02-10, True
    """, id="is_null"),
    pytest.param("IS NOT NULL", """
        fk, timestamp,  label
        1,  2025-02-01, False
        2,  2025-02-01, True
        3,  2025-02-01, False
        1,  2025-02-10, False
        2,  2025-02-10, False
        3,  2025-02-10, False
    """, id="is_not_null"),
])
def test_predict_null_check_condition_on_aggregation(temporal_converter, op, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT LAST(reviews.rating, 0, 10, DAYS) {op}
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv(expected_csv, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")
