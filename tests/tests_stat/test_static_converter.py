"""Tests for general static converter shape/behavior (no conditions or aggregations)."""

from tests.helpers import assert_table_equals, ref_df_from_csv


def test_convert_without_execute_returns_sql_string(static_converter):
    # Arrange
    rtgl_query = """
        PREDICT productMeta.category
        FOR EACH products.productId;
    """

    # Act
    sql_query = static_converter.convert(rtgl_query, execute=False)

    # Assert
    assert isinstance(sql_query, str)
    assert "SELECT" in sql_query.upper()


def test_predict_table_column_filters_out_null_labels(static_converter):
    # Arrange: product 3 ("Gizmo") has no priority -> excluded from the result
    rtgl_query = """
        PREDICT productMeta.priority
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv("fk, label\n1,  3.0\n2,  7.0")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)


def test_predict_column_of_the_for_each_table_itself(static_converter):
    # Arrange: predicting a column on the same table as FOR EACH needs no join
    rtgl_query = """
        PREDICT products.name
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv("fk, label\n1,  Widget\n2,  Gadget\n3,  Gizmo")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)


def test_for_each_star_resolves_to_primary_key_column(static_converter):
    # Arrange: FOR EACH products.* should behave identically to FOR EACH products.productId
    rtgl_query = """
        PREDICT productMeta.category
        FOR EACH products.*;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    expected = ref_df_from_csv("fk, label\n1,  AI\n2,  DS\n3,  SI")
    assert_table_equals(res_table, expected, {"fk": "products"}, None, None)
