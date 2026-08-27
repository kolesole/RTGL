"""Tests for static converter condition handling (PREDICT table.column <op> value)."""

import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


@pytest.mark.parametrize("op,expected_csv", [
    pytest.param("!=", "fk, label\n1,  False\n2,  True\n3,  False", id="not_equal"),
    pytest.param("<", "fk, label\n1,  False\n2,  False\n3,  False", id="less_than"),
    pytest.param("<=", "fk, label\n1,  True\n2,  False\n3,  False", id="less_than_or_equal"),
    pytest.param("==", "fk, label\n1,  True\n2,  False\n3,  False", id="equal"),
    pytest.param(">", "fk, label\n1,  False\n2,  True\n3,  False", id="greater_than"),
    pytest.param(">=", "fk, label\n1,  True\n2,  True\n3,  False", id="greater_than_or_equal"),
])
def test_predict_numeric_condition_evaluates_correctly(static_converter, op, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT productMeta.priority {op} 3
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert_table_equals(res_table, ref_df_from_csv(expected_csv), {"fk": "products"}, None, None)


@pytest.mark.parametrize("op,expected_csv", [
    pytest.param("CONTAINS", "fk, label\n1,  False\n2,  True\n3,  True", id="contains"),
    pytest.param("NOT CONTAINS", "fk, label\n1,  True\n2,  False\n3,  False", id="not_contains"),
    pytest.param("LIKE", "fk, label\n1,  False\n2,  False\n3,  False", id="like"),
    pytest.param("NOT LIKE", "fk, label\n1,  True\n2,  True\n3,  True", id="not_like"),
    pytest.param("STARTS WITH", "fk, label\n1,  False\n2,  False\n3,  True", id="starts_with"),
    pytest.param("ENDS WITH", "fk, label\n1,  False\n2,  True\n3,  False", id="ends_with"),
    pytest.param("=", "fk, label\n1,  False\n2,  False\n3,  False", id="equal"),
])
def test_predict_string_condition_evaluates_correctly(static_converter, op, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT productMeta.category {op} "S"
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert_table_equals(res_table, ref_df_from_csv(expected_csv), {"fk": "products"}, None, None)


@pytest.mark.parametrize("op,expected_csv", [
    pytest.param("IS NULL", "fk, label\n1,  False\n2,  False\n3,  True", id="is_null"),
    pytest.param("IS NOT NULL", "fk, label\n1,  True\n2,  True\n3,  False", id="is_not_null"),
])
def test_predict_null_check_condition_evaluates_correctly(static_converter, op, expected_csv):
    # Arrange
    rtgl_query = f"""
        PREDICT productMeta.priority {op}
        FOR EACH products.productId;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert_table_equals(res_table, ref_df_from_csv(expected_csv), {"fk": "products"}, None, None)
