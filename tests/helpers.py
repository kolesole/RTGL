"""Shared assertion helpers for the RTGL test suite."""

import pandas as pd

from rtgl.base import Table


def assert_table_equals(
    table: Table,
    expected_df: pd.DataFrame,
    expected_fkey_col_to_pkey_table: dict | None = None,
    expected_pkey_col: str | None = None,
    expected_time_col: str | None = None,
) -> None:
    r"""Assert a converted *`Table`* matches expected row data and metadata.

    Args:
        table (Table): Table returned by `converter.convert(..., execute=True)`.
        expected_df (pd.DataFrame): Expected row data.
        expected_fkey_col_to_pkey_table (dict | None): Expected `table.fkey_col_to_pkey_table`.
        expected_pkey_col (str | None): Expected `table.pkey_col`.
        expected_time_col (str | None): Expected `table.time_col`.

    Returns:
        out (None):
    """
    pd.testing.assert_frame_equal(
        table.df.reset_index(drop=True),
        expected_df.reset_index(drop=True),
        check_dtype=False,
        atol=1e-5,
    )
    assert table.fkey_col_to_pkey_table == expected_fkey_col_to_pkey_table
    assert table.pkey_col == expected_pkey_col
    assert table.time_col == expected_time_col


def ref_df_from_csv(csv_text: str, date_cols: list[str] | None = None) -> pd.DataFrame:
    r"""Build a reference *`DataFrame`* from an indented CSV literal, matching the fixture style.

    Args:
        csv_text (str): Indented CSV text (as used throughout the test suite for `ref_data`).
        date_cols (list[str] | None): Columns to parse as dates.

    Returns:
        out (pd.DataFrame): Parsed reference DataFrame.
    """
    from io import StringIO

    return pd.read_csv(
        StringIO(csv_text),
        skipinitialspace=True,
        parse_dates=date_cols or [],
        na_values=["nan", "NaN", "NONE", ""],
    )
