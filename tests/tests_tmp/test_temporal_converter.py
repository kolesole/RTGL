"""Tests for general temporal converter shape/behavior."""

import pandas as pd

from rtgl.converter import TConverter


def test_convert_without_execute_returns_sql_string(temporal_converter):
    # Arrange
    rtgl_query = """
        PREDICT AVG(reviews.rating, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    sql_query = temporal_converter.convert(rtgl_query, execute=False)

    # Assert
    assert isinstance(sql_query, str)
    assert "SELECT" in sql_query.upper()
    assert "TIMESTAMP" in sql_query.upper()


def test_execute_returns_table_with_fk_timestamp_label_columns(temporal_converter):
    # Arrange
    rtgl_query = """
        PREDICT AVG(reviews.rating, 0, 10, DAYS)
        FOR EACH products.productId;
    """

    # Act
    res_table = temporal_converter.convert(rtgl_query, execute=True)

    # Assert
    assert set(res_table.df.columns) == {"fk", "timestamp", "label"}
    assert res_table.time_col == "timestamp"
    assert res_table.pkey_col is None


def test_set_timestamps_changes_the_prediction_timestamps(test_db):
    # Arrange: a fresh converter (not the shared session fixture) so mutating its timestamps
    # can't leak into other tests
    converter = TConverter(db=test_db, timestamps=pd.Series(pd.to_datetime(["2025-02-01"])))
    new_timestamps = pd.Series(pd.to_datetime(["2025-02-05"]))

    # Act
    converter.set_timestamps(new_timestamps)
    res_table = converter.convert(
        "PREDICT COUNT(reviews.rating, 0, 10, DAYS) FOR EACH products.productId;", execute=True
    )

    # Assert
    assert set(res_table.df["timestamp"].dt.strftime("%Y-%m-%d")) == {"2025-02-05"}
