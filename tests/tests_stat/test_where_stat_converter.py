"""Tests for static converter WHERE clause handling."""

import pytest

from tests.helpers import assert_table_equals, ref_df_from_csv


def test_where_filters_parent_entities_before_predicting(static_converter):
    # Arrange
    rtgl_query = """
        PREDICT productMeta.category
        FOR EACH products.productId
        WHERE productMeta.priority <= 3;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert_table_equals(res_table, ref_df_from_csv("fk, label\n1,  AI"), {"fk": "products"}, None, None)


@pytest.mark.parametrize("op,expected_csv", [
    pytest.param(
        "AND",
        "fk, label\n1,  AI\n3,  SI",
        id="and",
    ),
    pytest.param(
        "OR",
        "fk, label\n1,  AI\n2,  DS\n3,  SI",
        id="or",
    ),
])
def test_nested_where_combines_conditions_correctly(static_converter, op, expected_csv):
    # Arrange: product 1 (Widget, priority 3) and product 3 (Gizmo, priority null) both satisfy
    # the AND branch (Widget/Gizmo both contain "i", and Gizmo's null priority satisfies the
    # trailing IS NULL regardless); product 2 (Gadget, priority 7) has no "i" in its name, so it
    # only survives via the OR branch.
    rtgl_query = f"""
        PREDICT productMeta.category
        FOR EACH products.productId
        WHERE (productMeta.priority >= 1 {op} products.name CONTAINS "i")
        OR productMeta.priority IS NULL;
    """

    # Act
    res_table = static_converter.convert(rtgl_query, execute=True)

    # Assert
    assert_table_equals(res_table, ref_df_from_csv(expected_csv), {"fk": "products"}, None, None)
