"""Utility functions for building SQL conditions and aggregations."""

from collections.abc import Callable


def build_num_condition(cond_dict: dict) -> Callable[[str], str]:
    """Build SQL numeric comparison condition from parsed dictionary.

    Args:
        cond_dict (dict): Dictionary containing 'N' (numeric value) and
            'CompOp' (comparison operator like '>', '<=', '==').

    Returns:
        out (Callable[[str], str]): Lambda that takes a column name and returns a SQL condition string.
    """
    tmp = cond_dict["N"].value
    n = float(tmp) if "." in tmp else int(tmp)

    comp_op = cond_dict["CompOp"].value

    return lambda column: f"{column} {comp_op} {n}"


def build_str_condition(cond_dict: dict) -> Callable[[str], str]:
    """Build SQL string comparison condition from parsed dictionary.

    Args:
        cond_dict (dict): Dictionary containing 'String' (string value) and
            'CompOp' (comparison operator like 'contains', 'starts with').

    Returns:
        out (Callable[[str], str]): Lambda that takes a column name and returns a SQL condition string.
    """
    s = cond_dict["String"].value.strip("'\"")
    comp_op = cond_dict["CompOp"].value.lower()

    match comp_op:
        case "contains":
            return lambda column: f"{column} LIKE '%{s}%'"
        case "not contains":
            return lambda column: f"{column} NOT LIKE '%{s}%'"
        case "like":
            return lambda column: f"{column} LIKE '{s}'"
        case "not like":
            return lambda column: f"{column} NOT LIKE '{s}'"
        case "starts with":
            return lambda column: f"{column} LIKE '{s}%'"
        case "ends with":
            return lambda column: f"{column} LIKE '%{s}'"
        case "=":
            return lambda column: f"{column} = '{s}'"
        case _:
            pass


def build_null_condition(cond_dict: dict) -> Callable[[str], str]:
    """Build SQL NULL check condition from parsed dictionary.

    Args:
        cond_dict (dict): Dictionary containing 'CheckOp' (NULL, IS_NULL).

    Returns:
        out (Callable[[str], str]): Lambda that takes a column name and returns a SQL condition string.
    """
    check_op = cond_dict["CheckOp"].value.upper()

    return lambda column: f"{column} {check_op}"


def build_aggr_func(aggr_dict: dict, time_column: str = None) -> Callable[[str], str]:
    """Build SQL aggregation function from parsed dictionary.

    Args:
        aggr_dict (dict): Dictionary containing 'AggrType' (aggregation type) and 'Column' (column to aggregate).
        time_column (str, optional): Time column name for temporal aggregations.

    Returns:
        out (Callable[[str], str]): Lambda that takes a table name and returns a SQL aggregation expression.
    """
    aggr_type = aggr_dict["AggrType"].value.lower()
    aggr_column = aggr_dict["Column"].value

    match aggr_type:
        case "avg":
            return lambda table: f"AVG({table}.{aggr_column})"
        case "count":
            return lambda table: f"COALESCE(COUNT({table}.{aggr_column}), 0)"
        case "count_distinct":
            return lambda table: f"COALESCE(COUNT(DISTINCT {table}.{aggr_column}), 0)"
        case "first":
            return lambda table: f"ARRAY_AGG({table}.{aggr_column} ORDER BY {table}.{time_column} ASC)[1]"
        case "last":
            return lambda table: f"ARRAY_AGG({table}.{aggr_column} ORDER BY {table}.{time_column} DESC)[1]"
        case "list_distinct":
            return lambda table: f"ARRAY_AGG(DISTINCT {table}.{aggr_column})"
        case "max":
            return lambda table: f"MAX({table}.{aggr_column})"
        case "min":
            return lambda table: f"MIN({table}.{aggr_column})"
        case "sum":
            return lambda table: f"COALESCE(SUM({table}.{aggr_column}), 0)"
        case _:
            pass


def build_cte(name: str, body: str) -> str:
    """Build a Common Table Expression (CTE) SQL string.

    Args:
        name (str): Name of the CTE.
        body (str): SQL query body of the CTE.

    Returns:
        out (str): Formatted CTE SQL string.
    """
    return f"{name} AS (\n{body})"


def add_prefix(table_query: str, prefix: str) -> str:
    """Add a prefix to all column names in a table.

    Args:
        table_query (str): SQL query representing the table.
        prefix (str): Prefix to add to each column name.

    Returns:
        out (str): SQL query with prefixed column names.
    """
    return f"(SELECT COLUMNS(*) AS '{prefix}\\0' FROM {table_query})"


def format_query(query: str) -> str:
    """Format a SQL query string for better readability.

    Args:
        query (str): SQL query string to format.

    Returns:
        out (str): Formatted SQL query string with indentation.
    """
    return query.replace("\n", "\n" + 4 * " ") + "\n"


def get_div_lines(message: str) -> tuple[str, str]:
    """Generate division lines with a messages for SQL formatting.

    Create SQL comment lines with a message.

    Args:
        message (str): Message to include in the division line.

    Returns:
        out (tuple[str, str]): Tuple containing the starting and ending division lines.
    """
    return f"{'--' * 3}{message}_START{'--' * 3}", f"{'--' * 3}{message}_END{'--' * 3}"

