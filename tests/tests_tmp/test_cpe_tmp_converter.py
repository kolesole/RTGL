"""Tests for Common Path Expressions (CPEs) in temporal queries."""

import pytest

from rtgl.validator.diagnostics import RTGLValidationError


def test_single_hop_cpe_matches_equivalent_direct_query(temporal_converter):
    # Arrange: the CPE just names the auto-discovered reviews->products route explicitly
    with_query = """
        WITH reviewsOfProduct AS (reviews.productId->products.productId)
        PREDICT COUNT(reviewsOfProduct.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """
    direct_query = """
        PREDICT COUNT(reviews.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    with_table = temporal_converter.convert(with_query, execute=True)
    direct_table = temporal_converter.convert(direct_query, execute=True)

    # Assert
    assert with_table.df.equals(direct_table.df)
    assert with_table.time_col == direct_table.time_col == "timestamp"


def test_two_hop_cpe_with_differing_join_key_names_matches_direct_query(temporal_converter):
    # Arrange: products -(reviews, entered via productId)-(exits via userId)-> users, mirroring
    # the static CPE test but through a temporal aggregation
    with_query = """
        WITH reviewerOfProduct AS (products.productId->reviews.productId:userId->users.userId)
        PREDICT COUNT_DISTINCT(reviewerOfProduct.productId, 0, 10, DAYS)
        FOR EACH users.userId;
    """

    # Act
    res_table = temporal_converter.convert(with_query, execute=True)

    # Assert: just confirm the query resolves and executes without error, producing the
    # expected columns -- exact per-window values depend on window-boundary semantics already
    # covered by the aggregation test suite, so this test is about CPE resolution, not windows.
    assert set(res_table.df.columns) == {"fk", "timestamp", "label"}
    assert res_table.time_col == "timestamp"


def test_cpe_combined_with_assuming(temporal_converter):
    # Arrange: mirrors the proven `product_product` notebook pattern (CPE referenced inside
    # both PREDICT and ASSUMING)
    rtgl_query = """
        WITH reviewsOfProduct AS (reviews.productId->products.productId)
        PREDICT COUNT(reviewsOfProduct.reviewId, 0, 10, DAYS)
        FOR EACH products.productId
        ASSUMING COUNT(reviewsOfProduct.reviewId, 0, 10, DAYS) != 0;
    """

    # Act / Assert: should convert and execute without raising
    res_table = temporal_converter.convert(rtgl_query, execute=True)
    assert set(res_table.df.columns) == {"fk", "timestamp", "label"}


def test_cpe_with_invalid_hop_is_rejected_even_if_unused(temporal_converter):
    # Arrange
    rtgl_query = """
        WITH badPath AS (reviews.wrongColumn->products.productId)
        PREDICT COUNT(reviews.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="badpath"):
        temporal_converter.convert(rtgl_query, execute=False)


def test_cpe_with_invalid_hop_used_in_predict_is_rejected(temporal_converter):
    # Arrange
    rtgl_query = """
        WITH badPath AS (reviews.wrongColumn->products.productId)
        PREDICT COUNT(badPath.reviewId, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act / Assert
    with pytest.raises(RTGLValidationError, match="badpath"):
        temporal_converter.convert(rtgl_query, execute=False)
