"""Tests for SQL injections in static queries.

NOTE: `execute=True` is intentionally avoided for the "injection used as the FOR EACH source"
case. `SConverter.convert`'s execute path resolves the FOR EACH table's original name via
`self.db_explorer.find_orig_name(ptable)`, which returns None for a table that only exists as
a CTE (not in `self.db.table_dict`), and the very next line calls `.lower()` on that result
unconditionally -- a pre-existing crash (`AttributeError: 'NoneType' object has no attribute
'lower'`) this test suite is not allowed to fix. That path is only exercised with
`execute=True`, so `execute=False` (SQL generation only) is used there instead.
"""

import pytest

from rtgl.validator.diagnostics import RTGLValidationError
from tests.helpers import assert_table_equals, ref_df_from_csv


def test_injection_with_outgoing_fk_used_in_aggregation(static_converter):
    # Arrange: only review 1 (rating 5) and review 3 (rating 4) pass the >= 4 filter
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM reviews WHERE rating >= 4]{highRatedReviews}
            {reviewId}
            {productId->products}
            {}
            .reviewId)
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert: product 1 -> review 1 only (review 4 has a null rating), product 2 -> review 3,
    # product 3 -> none (COUNT is COALESCE-wrapped, so it reports 0 rather than being excluded
    # -- same behavior as temporal aggregation, see test_sql_injection_tmp_converter.py)
    expected = ref_df_from_csv("fk, label\n1,  1.0\n2,  1.0\n3,  0.0")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)


def test_injection_body_with_nested_brackets(static_converter):
    # Arrange: same filter as above, expressed with a nested-bracket ANY(ARRAY[...]) predicate
    # to exercise SQL_INJECTION_BODY's recursive `[...]` handling
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM reviews WHERE rating = ANY(ARRAY[4, 5])]{highRatedReviews}
            {reviewId}
            {productId->products}
            {}
            .reviewId)
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert: same COALESCE-to-0 behavior as above -- product 3 reports 0, not excluded
    expected = ref_df_from_csv("fk, label\n1,  1.0\n2,  1.0\n3,  0.0")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)


def test_injection_referenced_by_a_real_tables_foreign_key(static_converter):
    # Arrange: `reviews.productId` is declared as pointing at this injection's primary key,
    # letting PathBuilder route users -> reviews -> selectedProducts
    rtgl_query = """
        PREDICT COUNT_DISTINCT(
            [SELECT * FROM products WHERE productId <= 2]{selectedProducts}
            {productId}
            {}
            {reviews.productId}
            .productId)
        FOR EACH users.userId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert: alice reviewed products {1, 2}, bob reviewed only {1} (both within the filter)
    expected = ref_df_from_csv("fk, label\n1,  2.0\n2,  1.0")
    assert_table_equals(res_table, expected, {"fk": "users"}, None, None)


def test_injection_used_as_for_each_source_generates_sql(static_converter):
    # Arrange
    rtgl_query = """
        PREDICT highRatedReviews.rating
        FOR EACH [
            SELECT * FROM reviews WHERE rating >= 4
        ]{highRatedReviews}
         {reviewId}
         {productId->products, userId->users}
         {}.reviewId;
    """

    # Act
    sql_query = static_converter.convert(rtgl_query, execute=False)

    # Assert
    assert isinstance(sql_query, str)
    assert "HIGHRATEDREVIEWS" in sql_query.upper()


def test_injection_with_outgoing_fk_to_nonexistent_table_is_rejected(static_converter):
    # Arrange
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM reviews]{r}
            {reviewId}
            {productId->nonexistentTable}
            {}
            .reviewId)
        FOR EACH products.productId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="nonexistenttable"):
        static_converter.convert(rtgl_query, execute=False)


def test_injection_referenced_by_nonexistent_column_is_rejected(static_converter):
    # Arrange: `reviews.notARealColumn` is declared as referencing the injection's pkey
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM products]{p}
            {productId}
            {}
            {reviews.notARealColumn}
            .productId)
        FOR EACH users.userId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="notarealcolumn"):
        static_converter.convert(rtgl_query, execute=False)


def test_injection_referenced_but_no_primary_key_declared_is_rejected(static_converter):
    # Arrange: fkey_table_col is non-empty (reviews.productId references it) but pkey_col ({})
    # is left empty
    rtgl_query = """
        PREDICT COUNT(
            [SELECT * FROM products]{p}
            {}
            {}
            {reviews.productId}
            .productId)
        FOR EACH users.userId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="primary key"):
        static_converter.convert(rtgl_query, execute=False)
