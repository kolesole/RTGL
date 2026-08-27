"""Tests for static converter aggregation functions.

Static aggregations have no time window: `AGGR_FUNC(table.column)` aggregates over *every*
related row reachable from the FOR EACH entity, regardless of any time column.

NOTE: FIRST and LAST are intentionally not covered here. `Converter.build_stat_aggregation`
calls `build_aggr_func(aggr_dict)` without a `time_column` (see rtgl/converter/converter.py),
so the generated SQL for FIRST/LAST is `ARRAY_AGG(... ORDER BY <table>.None ASC)[1]` -- a
reference to a literal column named "None". This is a pre-existing source bug (not something
this test suite is allowed to fix); asserting a passing result for FIRST/LAST here would be
asserting behavior that does not actually work.
"""

import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


@pytest.mark.parametrize("rtgl_aggr,expected_csv", [
    # product 1 has three reviews (5, 3, and one null rating); product 2 has one (4); product 3
    # has zero reviews. Static aggregation is anchored on the parent table with a LEFT JOIN out
    # to the aggregation table (mirroring temporal), so product 3 still gets a group -- COALESCE-
    # wrapped functions (SUM, COUNT, COUNT_DISTINCT) report 0 there; non-COALESCE'd ones (AVG,
    # MAX, MIN) report NULL and get filtered out by the outer `WHERE label IS NOT NULL`.
    pytest.param("AVG", "fk, label\n1,  4.0\n2,  4.0", id="avg"),
    pytest.param("MAX", "fk, label\n1,  5.0\n2,  4.0", id="max"),
    pytest.param("MIN", "fk, label\n1,  3.0\n2,  4.0", id="min"),
    pytest.param("SUM", "fk, label\n1,  8.0\n2,  4.0\n3,  0.0", id="sum"),
    pytest.param("COUNT", "fk, label\n1,  2.0\n2,  1.0\n3,  0.0", id="count"),
    pytest.param("COUNT_DISTINCT", "fk, label\n1,  2.0\n2,  1.0\n3,  0.0", id="count_distinct"),
])
def test_predict_aggregation_over_all_related_rows(static_converter, rtgl_aggr, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT {rtgl_aggr}(reviews.rating)
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert_table_equals(res_table, ref_df_from_csv(expected_csv), {"fk": "products"}, None, None)


@pytest.mark.parametrize("list_distinct_op", [
    pytest.param("", id="plain"),
    pytest.param("CLASSIFY", id="classify"),
    pytest.param("RANK TOP 2", id="rank_top"),
])
def test_predict_list_distinct_collects_unique_values(static_converter, list_distinct_op):
    # Arrange
    rtgl_query = f"""
        PREDICT LIST_DISTINCT(reviews.rating) {list_distinct_op}
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)
    res_df = res_table.df
    res_df["label"] = res_df["label"].apply(lambda values: sorted(values))

    # Assert: product 1 -> {3, 5}, product 2 -> {4}; product 3 has no reviews and is excluded
    assert res_df.to_dict("records") == [
        {"fk": 1, "label": [3.0, 5.0]},
        {"fk": 2, "label": [4.0]},
    ]
    assert res_table.fkey_col_to_pkey_table == {"fk": "products"}
    assert res_table.pkey_col is None
    assert res_table.time_col is None


def test_predict_non_coalesced_aggregation_over_entity_with_zero_related_rows_is_excluded(static_converter):
    # Arrange: product 3 ("Gizmo") has no reviews at all. It still gets a group (via the LEFT
    # JOIN anchored on the parent table), but AVG has no COALESCE wrapper, so its group's NULL
    # result gets filtered out by the outer `WHERE label IS NOT NULL` -- unlike SUM/COUNT/
    # COUNT_DISTINCT, which report 0 for the very same zero-row group (see the parametrized
    # test above).
    rtgl_query = """
        PREDICT AVG(reviews.rating)
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert sorted(res_table.df["fk"].tolist()) == [1, 2]


def test_predict_aggregation_where_clause_filters_child_rows(static_converter):
    # Arrange
    rtgl_query = """
        PREDICT COUNT(reviews.reviewId WHERE reviews.rating >= 4)
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert: product 1 has one review with rating >= 4 (the 5), product 2 has one (the 4),
    # product 3 has none at all -- COUNT is COALESCE-wrapped, so it reports 0 rather than being
    # excluded, same as an entity with rows that all fail the WHERE filter would
    expected = ref_df_from_csv("fk, label\n1,  1.0\n2,  1.0\n3,  0.0")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)
