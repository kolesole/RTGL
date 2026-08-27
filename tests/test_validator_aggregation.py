"""Tests for validator rules around aggregation/condition compatibility, CLASSIFY/RANK_TOP,
temporal window signs, and the temporal-aggregation-needs-a-time-column requirement.
"""

import pytest

from rtgl.validator.diagnostics import RTGLValidationError


class TestAggregationConditionTypeCompatibility:
    @pytest.mark.parametrize("aggr", ["AVG", "COUNT", "COUNT_DISTINCT", "FIRST", "LAST", "MAX", "MIN", "SUM"])
    def test_numeric_compatible_aggregations_are_accepted_in_numeric_condition(self, static_converter, aggr):
        query = f"""
            PREDICT products.name
            FOR EACH products.productId
            WHERE {aggr}(reviews.rating) > 1;
        """
        static_converter.convert(query, execute=False)

    def test_list_distinct_is_rejected_in_a_numeric_condition(self, static_converter):
        query = """
            PREDICT products.name
            FOR EACH products.productId
            WHERE LIST_DISTINCT(reviews.rating) > 1;
        """
        with pytest.raises(RTGLValidationError, match="cannot be used in numeric condition"):
            static_converter.convert(query, execute=False)

    @pytest.mark.parametrize("aggr", ["FIRST", "LAST"])
    def test_string_compatible_aggregations_are_accepted_in_string_condition(self, static_converter, aggr):
        query = f"""
            PREDICT products.name
            FOR EACH products.productId
            WHERE {aggr}(reviews.comment) CONTAINS "P";
        """
        static_converter.convert(query, execute=False)

    @pytest.mark.parametrize("aggr", ["AVG", "SUM", "COUNT"])
    def test_numeric_only_aggregations_are_rejected_in_string_condition(self, static_converter, aggr):
        query = f"""
            PREDICT products.name
            FOR EACH products.productId
            WHERE {aggr}(reviews.rating) CONTAINS "P";
        """
        with pytest.raises(RTGLValidationError, match="cannot be used in string condition"):
            static_converter.convert(query, execute=False)

    @pytest.mark.parametrize("aggr", ["AVG", "COUNT", "LIST_DISTINCT", "SUM"])
    def test_every_aggregation_is_accepted_in_a_null_condition(self, static_converter, aggr):
        query = f"""
            PREDICT products.name
            FOR EACH products.productId
            WHERE {aggr}(reviews.rating) IS NOT NULL;
        """
        static_converter.convert(query, execute=False)


class TestClassifyAndRankTopModifiers:
    def test_classify_on_non_list_distinct_aggregation_is_rejected(self, static_converter):
        query = "PREDICT AVG(reviews.rating) CLASSIFY FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="CLASSIFY modifier is only allowed with LIST_DISTINCT"):
            static_converter.convert(query, execute=False)

    def test_rank_top_on_non_list_distinct_aggregation_is_rejected(self, static_converter):
        query = "PREDICT AVG(reviews.rating) RANK TOP 3 FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="RANK_TOP K modifier is only allowed with LIST_DISTINCT"):
            static_converter.convert(query, execute=False)

    def test_classify_on_list_distinct_is_accepted(self, static_converter):
        query = "PREDICT LIST_DISTINCT(reviews.rating) CLASSIFY FOR EACH products.productId;"
        static_converter.convert(query, execute=False)

    def test_rank_top_on_list_distinct_is_accepted(self, static_converter):
        query = "PREDICT LIST_DISTINCT(reviews.rating) RANK TOP 3 FOR EACH products.productId;"
        static_converter.convert(query, execute=False)

    @pytest.mark.parametrize("k", [0, -1])
    def test_rank_top_with_non_positive_k_is_rejected(self, static_converter, k):
        query = f"PREDICT LIST_DISTINCT(reviews.rating) RANK TOP {k} FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="must be a positive integer"):
            static_converter.convert(query, execute=False)


class TestTemporalWindowSignRules:
    def test_negative_window_in_predict_is_rejected(self, temporal_converter):
        query = "PREDICT COUNT(reviews.rating, -5, 10, DAYS) FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="must be non-negative in PREDICT and ASSUMING"):
            temporal_converter.convert(query, execute=False)

    def test_positive_window_in_temporal_where_is_rejected(self, temporal_converter):
        query = """
            PREDICT AVG(reviews.rating, 0, 10, DAYS)
            FOR EACH products.productId
            WHERE COUNT(reviews.rating, 5, 10, DAYS) > 0;
        """
        with pytest.raises(RTGLValidationError, match="must be non-positive in WHERE clause"):
            temporal_converter.convert(query, execute=False)

    def test_negative_window_in_assuming_is_rejected(self, temporal_converter):
        query = """
            PREDICT AVG(reviews.rating, 0, 10, DAYS)
            FOR EACH products.productId
            ASSUMING COUNT(reviews.rating, -10, -5, DAYS) > 0;
        """
        with pytest.raises(RTGLValidationError, match="must be non-negative in PREDICT and ASSUMING"):
            temporal_converter.convert(query, execute=False)

    def test_start_not_less_than_end_is_rejected(self, temporal_converter):
        query = "PREDICT COUNT(reviews.rating, 10, 5, DAYS) FOR EACH products.productId;"
        with pytest.raises(RTGLValidationError, match="Start time must be less than end time"):
            temporal_converter.convert(query, execute=False)

    def test_valid_window_signs_are_accepted(self, temporal_converter):
        query = """
            PREDICT AVG(reviews.rating, 0, 10, DAYS)
            FOR EACH products.productId
            WHERE COUNT(reviews.rating, -10, 0, DAYS) > 0
            ASSUMING COUNT(reviews.rating, 0, 10, DAYS) > 0;
        """
        temporal_converter.convert(query, execute=False)


class TestTemporalAggregationRequiresATimeColumn:
    def test_aggregation_with_no_time_column_anywhere_on_its_path_is_rejected(self, temporal_converter):
        # Arrange: neither "notes" nor "products" (the parent, which does not count) has a
        # time column, so this temporal aggregation has nothing to apply its window to
        query = "PREDICT COUNT(notes.noteId, 0, 10, DAYS) FOR EACH products.productId;"

        # Act / Assert
        with pytest.raises(RTGLValidationError, match="has no time column"):
            temporal_converter.convert(query, execute=False)

    def test_aggregation_with_its_own_time_column_is_accepted(self, temporal_converter):
        # Arrange: "reviews" has its own time column
        query = "PREDICT COUNT(reviews.reviewId, 0, 10, DAYS) FOR EACH products.productId;"

        # Act / Assert: should not raise
        temporal_converter.convert(query, execute=False)
