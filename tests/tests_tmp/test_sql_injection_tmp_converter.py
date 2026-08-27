"""Tests for SQL injections in temporal queries.

See tests/tests_stat/test_sql_injection_stat_converter.py for why the "injection used as the
FOR EACH source" case is only exercised with `execute=False`.
"""

import pytest

from rtgl.validator.diagnostics import RTGLValidationError
from tests.helpers import assert_table_equals, ref_df_from_csv


def test_injection_with_time_col_used_in_aggregation(temporal_converter):
    # Arrange: only review 1 (rating 5, 2025-02-02) and review 3 (rating 4, 2025-02-03) pass
    # the >= 4 filter, and the injection declares its own reviewDate as the time_col so the
    # window (ts, ts+10] applies to it
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM reviews WHERE rating >= 4]{highRatedReviews}
            {reviewId}
            {productId->products}
            {}
            {reviewDate}.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert: at 2025-02-01 both matching reviews fall in the (02-01, 02-11] window (product 1
    # -> review 1, product 2 -> review 3); at 2025-02-10 neither does. COUNT is COALESCE-wrapped,
    # so product 3 (no reviews at all) reports 0 rather than being excluded -- same as the static
    # version of this same query in test_sql_injection_stat_converter.py.
    expected = ref_df_from_csv("""
        fk, timestamp,  label
        1,  2025-02-01, 1.0
        2,  2025-02-01, 1.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 0.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")


def test_injection_body_with_nested_brackets(temporal_converter):
    # Arrange: same filter as above, expressed with a nested-bracket ANY(ARRAY[...]) predicate
    # to exercise SQL_INJECTION_BODY's recursive `[...]` handling
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM reviews WHERE rating = ANY(ARRAY[4, 5])]{highRatedReviews}
            {reviewId}
            {productId->products}
            {}
            {reviewDate}.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert: same result as the plain filter above
    expected = ref_df_from_csv("""
        fk, timestamp,  label
        1,  2025-02-01, 1.0
        2,  2025-02-01, 1.0
        3,  2025-02-01, 0.0
        1,  2025-02-10, 0.0
        2,  2025-02-10, 0.0
        3,  2025-02-10, 0.0
    """, date_cols=["timestamp"])
    assert_table_equals(res_table, expected, {"fk": "products"}, None, "timestamp")


def test_injection_referenced_by_a_real_tables_foreign_key(temporal_converter):
    # Arrange: `reviews.productId` is declared as pointing at this injection's primary key
    rtgl_query = """
        PREDICT COUNT_DISTINCT(
            [SELECT * FROM products WHERE productId <= 2]{selectedProducts}
            {productId}
            {}
            {reviews.productId}
            {}.productId, 0, 10, DAYS)
        FOR EACH users.userId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    assert set(res_table.df.columns) == {"fk", "timestamp", "label"}


def test_injection_used_as_for_each_source_generates_sql(temporal_converter):
    # Arrange
    rtgl_query = """
        PREDICT COUNT(highRatedReviews.reviewId, 0, 10, DAYS)
        FOR EACH [
            SELECT * FROM reviews WHERE rating >= 4
        ]{highRatedReviews}
         {reviewId}
         {productId->products, userId->users}
         {}
         {reviewDate}.reviewId;
    """

    # Act
    sql_query = temporal_converter.convert(rtgl_query, execute=False)

    # Assert
    assert isinstance(sql_query, str)
    assert "HIGHRATEDREVIEWS" in sql_query.upper()


def test_injection_with_outgoing_fk_to_nonexistent_table_is_rejected(temporal_converter):
    # Arrange
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM reviews]{r}
            {reviewId}
            {productId->nonexistentTable}
            {}
            {reviewDate}.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="nonexistenttable"):
        temporal_converter.convert(rtgl_query, execute=False)


def test_injection_referenced_by_nonexistent_column_is_rejected(temporal_converter):
    # Arrange
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM products]{p}
            {productId}
            {}
            {reviews.notARealColumn}
            {}.productId, 0, 10, DAYS)
        FOR EACH users.userId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="notarealcolumn"):
        temporal_converter.convert(rtgl_query, execute=False)
