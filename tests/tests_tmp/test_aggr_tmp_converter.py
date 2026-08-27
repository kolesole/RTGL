"""Tests for temporal converter aggregation functions.

Unlike static aggregation (which uses an INNER JOIN and drops an entity entirely when it has
zero related rows), temporal aggregation is anchored on `__FOR_EACH__` with a LEFT JOIN, so
every (entity, timestamp) pair gets a group. COALESCE-wrapped functions (SUM, COUNT,
COUNT_DISTINCT) report 0 for a group with no matching rows; non-COALESCE'd ones (AVG, MIN, MAX,
FIRST, LAST) report NULL there and get filtered out by the outer `WHERE label IS NOT NULL`.

NOTE: a forward window `(start, end, UNIT)` covers `(ts+start, ts+end]` -- exclusive of the
start boundary, inclusive of the end boundary.
"""

import json

import pandas as pd
import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


@pytest.mark.parametrize("rtgl_aggr,expected_csv", [
    # reviews.rating in the forward window [ts, ts+10): at 2025-02-01 the window holds reviews
    # 1 (product 1, rating 5), 2 (product 1, rating 3), 3 (product 2, rating 4); at 2025-02-10
    # it holds only review 4 (product 1, null rating). Product 3 has no reviews at all.
    pytest.param("AVG", """
        fk, timestamp,  label
        1,  2025-02-01, 4.0
        2,  2025-02-01, 4.0
    """, id="avg"),
    pytest.param("MAX", """
        fk, timestamp,  label
        1,  2025-02-01, 5.0
        2,  2025-02-01, 4.0
    """, id="max"),
    pytest.param("MIN", """
        fk, timestamp,  label
        1,  2025-02-01, 3.0
        2,  2025-02-01, 4.0
    """, id="min"),
    pytest.param("SUM", """
        fk, timestamp,  label
        1,  2025-02-01, 8.0
        2,  2025-02-01, 4.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 0.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, id="sum"),
    pytest.param("COUNT", """
        fk, timestamp,  label
        1,  2025-02-01, 2.0
        2,  2025-02-01, 1.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 0.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, id="count"),
    pytest.param("COUNT_DISTINCT", """
        fk, timestamp,  label
        1,  2025-02-01, 2.0
        2,  2025-02-01, 1.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 0.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, id="count_distinct"),
    pytest.param("FIRST", """
        fk, timestamp,  label
        1,  2025-02-01, 5.0
        2,  2025-02-01, 4.0
    """, id="first"),
    pytest.param("LAST", """
        fk, timestamp,  label
        2,  2025-02-01, 4.0
    """, id="last"),
])
def test_predict_aggregation_over_time_window(temporal_converter, rtgl_aggr, expected_csv):
    # Arrange: the window is (ts, ts+10] (exclusive start, inclusive end), so review 4
    # (2025-02-11, null rating) falls inside product 1's 2025-02-01 window too. LAST is
    # order-sensitive (unlike AVG/MIN/MAX, which just ignore nulls), so it picks review 4 as
    # the chronologically-last row and comes back null there -- excluded by the outer filter.
    rtgl_query = f"""
        PREDICT {rtgl_aggr}(reviews.rating, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv(expected_csv, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")


def _normalize_list_distinct_label(res_df: pd.DataFrame) -> pd.DataFrame:
    def normalize(value):
        if isinstance(value, str):
            items = json.loads(value)
        elif hasattr(value, "tolist"):
            items = value.tolist()
        else:
            items = list(value)
        return sorted(item if pd.notna(item) else 0.0 for item in items)

    res_df["label"] = res_df["label"].apply(normalize)
    return res_df


def test_predict_list_distinct_collects_unique_values_per_window(temporal_converter):
    # Arrange: only product 1 and product 2 at 2025-02-01 have a non-empty, non-null rating in
    # their forward window (see the aggregation test above); the remaining combinations reduce
    # to an all-null or all-empty distinct-aggregate and are left unasserted here.
    rtgl_query = """
        PREDICT LIST_DISTINCT(reviews.rating, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)
    res_df = _normalize_list_distinct_label(res_table.df)
    res_df = res_df[res_df["timestamp"] == pd.Timestamp("2025-02-01")]

    # Assert
    assert res_df.sort_values("fk").to_dict("records") == [
        {"fk": 1, "timestamp": pd.Timestamp("2025-02-01"), "label": [3.0, 5.0]},
        {"fk": 2, "timestamp": pd.Timestamp("2025-02-01"), "label": [4.0]},
    ]
    assert res_table.fkey_col_to_pkey_table == {"fk": "products"}
    assert res_table.pkey_col is None
    assert res_table.time_col == "timestamp"


def test_predict_list_distinct_classify_does_not_change_the_result(temporal_converter):
    # Arrange: CLASSIFY only marks the label as a classification target, it does not truncate
    # or otherwise alter the aggregated list itself
    rtgl_query = """
        PREDICT LIST_DISTINCT(reviews.rating, 0, 10, DAYS) CLASSIFY
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)
    res_df = _normalize_list_distinct_label(res_table.df)
    res_df = res_df[res_df["timestamp"] == pd.Timestamp("2025-02-01")]

    # Assert
    assert res_df.sort_values("fk").to_dict("records") == [
        {"fk": 1, "timestamp": pd.Timestamp("2025-02-01"), "label": [3.0, 5.0]},
        {"fk": 2, "timestamp": pd.Timestamp("2025-02-01"), "label": [4.0]},
    ]


@pytest.mark.parametrize("k", [1, 2, 3])
def test_predict_list_distinct_rank_top_truncates_to_at_most_k(temporal_converter, k):
    # Arrange: the underlying DISTINCT-aggregation order is implementation-defined, so this
    # only asserts the truncation bound (<=K), not which specific element(s) survive
    rtgl_query = f"""
        PREDICT LIST_DISTINCT(reviews.rating, 0, 10, DAYS) RANK TOP {k}
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    assert all(len(label) <= k for label in res_table.df["label"])


def test_predict_aggregation_with_no_rows_in_window_and_coalesce(temporal_converter):
    # Arrange: no review falls within [20, 21) days of either prediction timestamp for any
    # product -- COUNT is COALESCE-wrapped, so it reports 0 rather than being excluded
    rtgl_query = """
        PREDICT COUNT(reviews.rating, 20, 21, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    assert len(res_table.df) == 6
    assert (res_table.df["label"] == 0.0).all()


def test_predict_aggregation_with_no_rows_in_window_and_no_coalesce(temporal_converter):
    # Arrange: same empty window as above, but AVG has no COALESCE wrapper, so every
    # (entity, timestamp) pair gets a null label and is filtered out entirely
    rtgl_query = """
        PREDICT AVG(reviews.rating, 20, 21, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    assert res_table.df.empty
