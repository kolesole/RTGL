"""Tests for Common Path Expressions (CPEs) in static queries."""

import pytest

from rtgl.validator.diagnostics import RTGLValidationError
from tests.helpers import assert_table_equals, ref_df_from_csv


def test_single_hop_cpe_matches_equivalent_direct_query(static_converter):
    # Arrange: the CPE just names the auto-discovered reviews->products route explicitly
    with_query = """
        WITH reviewsOfProduct AS (reviews.productId->products.productId)
        PREDICT AVG(reviewsOfProduct.rating)
        FOR EACH products.productId;
    """
    direct_query = """
        PREDICT AVG(reviews.rating)
        FOR EACH products.productId;
    """

    # Act
    with_table = static_converter.convert(with_query, execute=True)
    direct_table = static_converter.convert(direct_query, execute=True)

    # Assert
    assert with_table.df.equals(direct_table.df)
    assert with_table.fkey_col_to_pkey_table == direct_table.fkey_col_to_pkey_table
    assert with_table.pkey_col == direct_table.pkey_col
    assert with_table.time_col == direct_table.time_col


def test_two_hop_cpe_with_differing_join_key_names(static_converter):
    # Arrange: products -(reviews, entered via productId)-(exits via userId)-> users.
    # reviews.productId != reviews.userId, so the middle hop needs the ":right_key" form to
    # say "enter this table via productId, but leave it via userId".
    rtgl_query = """
        WITH reviewerOfProduct AS (products.productId->reviews.productId:userId->users.userId)
        PREDICT COUNT_DISTINCT(reviewerOfProduct.productId)
        FOR EACH users.userId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert: alice (userId=1) reviewed products {1, 2}; bob (userId=2) reviewed only {1}
    expected = ref_df_from_csv("fk, label\n1,  2.0\n2,  1.0")
    assert_table_equals(res_table, expected, {"fk": "users"}, None, None)


def test_multiple_cpes_declared_in_one_with_clause(static_converter):
    # Arrange
    rtgl_query = """
        WITH reviewsOfProduct AS (reviews.productId->products.productId),
             notesOfProduct AS (notes.productId->products.productId)
        PREDICT AVG(reviewsOfProduct.rating)
        FOR EACH products.productId
        WHERE notesOfProduct.note IS NOT NULL;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert: product 3 has no note at all -> excluded by the WHERE
    expected = ref_df_from_csv("fk, label\n1,  4.0\n2,  4.0")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)


def test_cpe_with_invalid_hop_is_rejected_even_if_unused(static_converter):
    # Arrange: "wrongColumn" does not correspond to any real foreign key between reviews/products
    rtgl_query = """
        WITH badPath AS (reviews.wrongColumn->products.productId)
        PREDICT products.name
        FOR EACH products.productId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="badpath"):
        static_converter.convert(rtgl_query, execute=False)


def test_cpe_with_invalid_hop_used_in_predict_is_rejected(static_converter):
    # Arrange
    rtgl_query = """
        WITH badPath AS (reviews.wrongColumn->products.productId)
        PREDICT AVG(badPath.rating)
        FOR EACH products.productId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="badpath"):
        static_converter.convert(rtgl_query, execute=False)
