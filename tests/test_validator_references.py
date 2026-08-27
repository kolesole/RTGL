"""Tests for validator reference checks: existence, connectivity, primary keys, CPEs, and
SQL-injection key declarations.

NOTE: identifiers are lowercased during parsing (see `Visitor._node2value`), so every error
message quotes the lowercase form regardless of how the query text capitalized it -- `match=`
patterns below use lowercase accordingly.
"""

import pytest

from rtgl.validator.diagnostics import RTGLValidationError


class TestNonexistentReferences:
    def test_for_each_table_does_not_exist(self, static_converter):
        query = "PREDICT products.name FOR EACH nonexistentTable.id;"
        with pytest.raises(RTGLValidationError, match="does not exist"):
            static_converter.convert(query, execute=False)

    def test_predict_table_does_not_exist(self, static_converter):
        query = "PREDICT nonexistentTable.col FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="does not exist"):
            static_converter.convert(query, execute=False)

    def test_where_table_does_not_exist(self, static_converter):
        query = """
            PREDICT products.name
            FOR EACH products.productId
            WHERE nonexistentTable.col == 1;
        """
        with pytest.raises(RTGLValidationError, match="does not exist"):
            static_converter.convert(query, execute=False)

    def test_aggregation_table_does_not_exist(self, static_converter):
        query = "PREDICT COUNT(nonexistentTable.col) FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="does not exist"):
            static_converter.convert(query, execute=False)

    def test_column_does_not_exist(self, static_converter):
        query = "PREDICT products.nonexistentColumn FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="does not exist"):
            static_converter.convert(query, execute=False)


class TestForEachPrimaryKeyRequirement:
    def test_for_each_column_that_is_not_the_primary_key_is_rejected(self, static_converter):
        # Arrange: "name" is a real column of products but not its primary key
        query = "PREDICT products.productId FOR EACH products.name;"

        # Act / Assert
        with pytest.raises(RTGLValidationError, match="primary key"):
            static_converter.convert(query, execute=False)

    def test_for_each_column_that_is_the_primary_key_is_accepted(self, static_converter):
        # Arrange
        query = "PREDICT products.name FOR EACH products.productId;"

        # Act / Assert: should not raise
        static_converter.convert(query, execute=False)


class TestConverterQueryTypeMismatch:
    def test_static_converter_rejects_temporal_query(self, static_converter):
        query = "PREDICT COUNT(reviews.rating, 0, 10, DAYS) FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="only static queries are supported"):
            static_converter.convert(query, execute=False)

    def test_temporal_converter_rejects_static_query(self, temporal_converter):
        query = "PREDICT products.name FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="only temporal queries are supported"):
            temporal_converter.convert(query, execute=False)


class TestCommonPathExpressionValidation:
    def test_cpe_with_invalid_hop_is_rejected_even_if_never_referenced(self, static_converter):
        query = """
            WITH neverUsed AS (reviews.wrongColumn->products.productId)
            PREDICT products.name
            FOR EACH products.productId;
        """
        with pytest.raises(RTGLValidationError, match="neverused"):
            static_converter.convert(query, execute=False)

    def test_valid_cpe_is_accepted(self, static_converter):
        query = """
            WITH reviewsOfProduct AS (reviews.productId->products.productId)
            PREDICT AVG(reviewsOfProduct.rating)
            FOR EACH products.productId;
        """
        static_converter.convert(query, execute=False)


class TestMultiPathAmbiguity:
    def test_two_equally_short_paths_raise_an_ambiguity_error(self, static_converter):
        # Arrange: products->users has two distinct 2-hop routes of equal length
        # (via reviews and via wishlists), which the path search cannot disambiguate
        query = "PREDICT products.productId FOR EACH users.userId;"

        # Act / Assert
        with pytest.raises(RTGLValidationError, match="ambiguous"):
            static_converter.convert(query, execute=False)

    def test_a_uniquely_shortest_path_among_several_only_warns(self, static_converter):
        # Arrange: carts->users has one uniquely-shortest 2-hop route (via cartItems) and a
        # longer 3-hop alternative (via products) -- not ambiguous, just worth a warning
        query = "PREDICT carts.cartId FOR EACH users.userId;"

        # Act / Assert
        with pytest.warns(UserWarning, match="carts"):
            static_converter.convert(query, execute=False)


class TestSqlInjectionKeyValidation:
    def test_outgoing_foreign_key_to_nonexistent_table_is_rejected(self, static_converter):
        query = """
            PREDICT COUNT(
                [SELECT * FROM reviews]{r}
                {reviewId}
                {productId->nonexistentTable}
                {}
                .reviewId)
            FOR EACH products.productId;
        """
        with pytest.raises(RTGLValidationError, match="nonexistenttable"):
            static_converter.convert(query, execute=False)

    def test_incoming_reference_from_nonexistent_table_is_rejected(self, static_converter):
        query = """
            PREDICT COUNT(
                [SELECT * FROM products]{p}
                {productId}
                {}
                {nonexistentTable.productId}
                .productId)
            FOR EACH users.userId;
        """
        with pytest.raises(RTGLValidationError, match="nonexistenttable"):
            static_converter.convert(query, execute=False)

    def test_incoming_reference_to_nonexistent_column_is_rejected(self, static_converter):
        query = """
            PREDICT COUNT(
                [SELECT * FROM products]{p}
                {productId}
                {}
                {reviews.notARealColumn}
                .productId)
            FOR EACH users.userId;
        """
        with pytest.raises(RTGLValidationError, match="notarealcolumn"):
            static_converter.convert(query, execute=False)

    def test_incoming_reference_with_no_primary_key_declared_is_rejected(self, static_converter):
        query = """
            PREDICT COUNT(
                [SELECT * FROM products]{p}
                {}
                {}
                {reviews.productId}
                .productId)
            FOR EACH users.userId;
        """
        with pytest.raises(RTGLValidationError, match="primary key"):
            static_converter.convert(query, execute=False)
