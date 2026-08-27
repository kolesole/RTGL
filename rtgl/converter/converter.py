"""Base RTGL converter class."""

from abc import ABC, abstractmethod

import duckdb
from antlr4 import CommonTokenStream, InputStream

from rtgl.base import Database, DatabaseExplorer, Table
from rtgl.base.path_builder import PathBuilder
from rtgl.converter.utils import (
    add_prefix,
    build_aggr_func,
    build_null_condition,
    build_num_condition,
    build_str_condition,
    format_query,
    get_div_lines,
)
from rtgl.parser import LexerRTGL, ParserRTGL
from rtgl.validator import IssueCollector, Validator
from rtgl.visitor import Visitor


class Converter(ABC):
    r"""Base abstract RTGL converter class for conversion RTGL -> SQL.

    Provides shared functionality for temporal and static RTGL converters.
    Some methods are abstract and must be implemented by concrete subclasses,
    but others provide common logic used in both static and temporal conversion.
    """

    def __init__(self, db: Database) -> None:
        r"""Initialize the base converter.

        Initialize the *`Database`* instance and its normalized version, the *`Visitor`* instance,
        and the *`IssueCollector`* instance for storing validation errors.

        Args:
            db (Database): *`Database`* instance containing the schema and data tables to be queried.

        Returns:
            out (None):
        """
        self.conn = None
        self.db = db

        self.collector = IssueCollector()
        self.visitor = Visitor()

        self.ctes = ""
        self.cte_dict = {}

        self.db_explorer: DatabaseExplorer = None
        self.path_builder: PathBuilder = None
        self.validator_class: type[Validator] = None
        self.validator: Validator = None

    @abstractmethod
    def convert(self, rtgl_query: str, execute: bool = False) -> str | Table:
        r"""Abstract conversion method.

        Main entry point.

        Note:
            For explanation of the conversion process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_for_each(self, for_each_dict: dict) -> tuple[str, str]:
        r"""Abstract method to build the SQL query for the FOR EACH part of the RTGL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_predict(self, predict_dict: dict, ptable: str, ppk: str) -> str:
        r"""Abstract method to build the SQL query for the predict part of the RTGL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Abstract method to build the SQL query for the expression part of the RTGL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Abstract method to build the SQL query for the aggregation part of the RTGL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_ctes(self, injections: list[tuple]) -> None:
        r"""Abstract method to build the SQL query for CTEs found in RTGL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_join(self, src_table: str, src_table_query: str, dst_table: str, **kwargs: dict) -> str:
        r"""Abstract method to build the SQL query for joining two different tables.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    def parse_query(self, rtgl_query: str) -> dict:
        r"""Parse the RTGL query string into a dictionary representation.

        Parse a query, build CTEs, and validate the resulting dictionary representation; print all errors
        on stderr and exit the program if any errors were found.

        Args:
            rtgl_query (str): The RTGL query string to be parsed.

        Returns:
            query_dict (dict): Dictionary representation of the parsed RTGL query.
        """
        input_stream = InputStream(rtgl_query)
        lexer = LexerRTGL(input_stream)
        token_stream = CommonTokenStream(lexer)

        parser = ParserRTGL(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.collector)
        tree = parser.query()

        # syntax errors collected during parsing
        self.collector.report(after_syntax_validation=True)

        query_dict = self.visitor.visit(tree)
        self.build_ctes(query_dict["Injections"])
        self.db_explorer = DatabaseExplorer(self.db, self.cte_dict)
        self.path_builder = PathBuilder(self.db_explorer, query_dict["PredefinedPaths"])

        if self.validator_class:
            self.validator = self.validator_class(self.collector, self.db_explorer, self.path_builder)
            self.validator.validate(query_dict)

        # semantic warnings and errors collected during validation
        self.collector.report(after_syntax_validation=False)

        return query_dict

    def build_stat_where(self, where_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build the SQL query for the static WHERE part of the RTGL query.

        Filter a ptable before using it.

        Args:
            where_dict (dict): Dictionary representation of the WHERE part of the RTGL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            where_query (str): SQL query string representing the filtered ptable.
        """
        div_line1, div_line2 = get_div_lines("STAT_WHERE")

        if where_dict["IsSimple"]:
            expr_query = self.build_simple_expr(where_dict["Expr"].value)
            where_query = (
                f"{div_line1}\n"
                "SELECT\n"
                "    *\n"
                "FROM\n"
                f"    {ptable}\n"
                "WHERE\n"
                f"{expr_query}"
                f"{div_line2}"
            )
        else:
            expr_query = self.build_stat_expr(where_dict["Expr"].value, ptable, ppk)
            expr_query = format_query(expr_query)

            where_query = (
                f"{div_line1}\n"
                "SELECT\n"
                "    *\n"
                "FROM\n"
                f"    {ptable}\n"
                "WHERE\n"
                f"    {ppk} IN (\n"
                "        SELECT fk FROM (\n"
                f"            {expr_query}\n"
                "        ) __IN_SUBQUERY__\n"
                "    )\n"
                f"{div_line2}"
            )

        return where_query

    def build_simple_expr(self, expr_dict: dict) -> str:
        r"""Build a raw boolean expression for a simple WHERE (no join/subquery needed).

        Only reachable when `where_dict["IsSimple"]` is True, i.e. every leaf condition is a
        plain `table.column` reference to the parent table itself (see
        `Visitor._is_where_simple`).

        Args:
            expr_dict (dict): Parsed expression (can contain 'Op', 'LeftExpr', 'RightExpr'
                keys, or a single condition).

        Returns:
            expr_query (str): SQL boolean expression, to be inlined directly in a WHERE clause.
        """
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            left_expr = self.build_simple_expr(expr_dict["LeftExpr"])
            right_expr = self.build_simple_expr(expr_dict["RightExpr"])
            op = expr_dict["Op"].value.upper()

            expr_query = (
                f"    ({left_expr})\n"
                f"{op}\n"
                f"    ({right_expr})\n"
            )
        else:
            expr_query = self.build_simple_condition(expr_dict.value)

        return expr_query

    def build_simple_condition(self, cond_dict: dict) -> str:
        r"""Build a raw boolean condition for a simple WHERE (no join/subquery needed).

        Args:
            cond_dict (dict): Parsed condition dictionary for a plain `table.column` reference.

        Returns:
            cond_query (str): SQL condition expression, e.g. `age > 18`.
        """
        # a simple WHERE only ever contains plain id_dot_id conditions on the
        # parent table (see Visitor._is_where_simple) -> use the column directly
        comp_col = cond_dict["Column"].value

        ctype = cond_dict["CType"]
        match ctype:
            case "num":
                cond = build_num_condition(cond_dict)
            case "str":
                cond = build_str_condition(cond_dict)
            case "null":
                cond = build_null_condition(cond_dict)
            case _:
                pass

        not_op = "NOT " if cond_dict["NOT"] else ""
        cond_query = f"{not_op}{cond(comp_col)}"

        return cond_query

    def build_stat_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build a SQL query for the static expression part of the RTGL query.

        Args:
            expr_dict (dict): Dictionary representation of the expr part of the RTGL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query string representing the expr part of the RTGL query.
        """
        div_line1, div_line2 = get_div_lines("STAT_EXPR")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            left_expr = self.build_stat_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = format_query(left_expr)
            right_expr = self.build_stat_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = format_query(right_expr)

            # each side yields an independently-computed set of matching foreign keys, so AND/OR
            # combine them as set operations (INTERSECT/UNION) rather than inline boolean logic
            op = expr_dict["Op"].value.lower()
            if op == "and":
                filt = "INTERSECT"
            elif op == "or":
                filt = "UNION"
            else:
                pass

            expr_query = (
                f"{div_line1}\n"
                "SELECT\n"
                "    fk\n"
                "FROM\n"
                f"    ({left_expr}) __LEFT_EXPR__\n"
                f"{filt}\n"
                "SELECT\n"
                "    fk\n"
                f"FROM ({right_expr}) __RIGHT_EXPR__\n"
                f"{div_line2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk, stat=True)

        return expr_query

    def build_condition(self, cond_dict: dict, ptable: str, ppk: str, stat: bool = False) -> str:
        r"""Build a SQL query for a condition part of the RTGL query.

        Args:
            cond_dict (dict): Dictionary representation of the condition part of the RTGL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            stat (bool): Flag indicating whether the condition is part of a static expression or not.

        Returns:
            cond_query (str): SQL query string representing the condition part of the RTGL query.
        """
        div_line1, div_line2 = get_div_lines("CONDITION")

        cond_type = cond_dict["CondType"]
        match cond_type:
            case "aggregation":
                if stat:
                    main_query = self.build_stat_aggregation(cond_dict["Aggregation"].value, ptable, ppk)
                else:
                    main_query = self.build_aggregation(cond_dict["Aggregation"].value, ptable, ppk)
            case "id_dot_id":
                main_query = self.build_id_dot_id(cond_dict, ptable, ppk)
            case _:
                pass
        main_query = format_query(main_query)

        comp_col = "comp_col"

        ctype = cond_dict["CType"]
        match ctype:
            case "num":
                cond = build_num_condition(cond_dict)
            case "str":
                cond = build_str_condition(cond_dict)
            case "null":
                cond = build_null_condition(cond_dict)
            case _:
                pass

        not_op = "NOT " if cond_dict["NOT"] else ""
        cond_query = (
            f"{div_line1}\n"
            "SELECT\n"
            "    *\n"
            "FROM\n"
            f"    ({main_query})\n"
            "WHERE\n"
            f"    {not_op}{cond(comp_col)}\n"
            f"{div_line2}"
        )

        return cond_query

    def build_stat_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build a SQL query for a static RTGL aggregation.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary containing 'Table', 'Column', 'Where'(optional) keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning pairs (fk, comp_col).
        """
        div_line1, div_line2 = get_div_lines("STAT_AGGREGATION")

        # extract aggregation table
        aggr_table = self.path_builder.find_orig_src_table(aggr_dict["Table"].value)
        aggr_column = self.db_explorer.find_column(aggr_table, aggr_dict["Column"].value)

        if aggr_table != ptable:
            aggr_dict["Column"].value = "__TABLE0__" + aggr_column

        if aggr_column == "*":
            aggr_dict["Column"].value = ppk

        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict)
        aggr = format_query(aggr_func("__JOINED_TABLES__"))
        aggr_dict["Column"].value = aggr_column

        # build static WHERE query if exists
        if where := aggr_dict["Where"]:
            aggr_ppk = self.db_explorer.find_pkey(aggr_table)
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = f"({aggr_table}\n)"

        joined_tables = self.build_stat_join(aggr_dict["Table"].value, aggr_table, ptable)

        # Anchor on the raw parent table (not on the aggregation-table join chain itself) with a
        # LEFT JOIN, so an entity with zero matching rows still gets a group -- giving `aggr`'s own
        # COALESCE (e.g. for COUNT/SUM) a chance to report 0 instead of the entity being silently
        # excluded. This mirrors temporal aggregation's behavior, which is anchored on __FOR_EACH__.
        aggr_query = (
            f"{div_line1}\n"
            "SELECT\n"
            f"    __PARENT__.{ppk} AS fk,\n"
            f"    {aggr} AS comp_col\n"
            "FROM\n"
            f"    {ptable} __PARENT__\n"
            "LEFT JOIN\n"
            f"    {joined_tables} __JOINED_TABLES__\n"
            "ON\n"
            f"    __JOINED_TABLES__.{ppk} = __PARENT__.{ppk}\n"
            "GROUP BY\n"
            f"    __PARENT__.{ppk}\n"
            f"{div_line2}"
        )

        return aggr_query

    def build_id_dot_id(self, some_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build the SQL query for a table.column(id_dot_id) part of the RTGL query.

        Args:
            some_dict (dict): Dictionary containing 'Table', 'Column' keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            id_dot_id_query (str): SQL query string representing the id_dot_id part of the RTGL query.
        """
        div_line1, div_line2 = get_div_lines("ID_DOT_ID")

        table = self.path_builder.find_orig_src_table(some_dict["Table"].value)
        column = self.db_explorer.find_column(table, some_dict["Column"].value)

        # column to compare in condition
        comp_col = "comp_col"

        joined_tables = self.build_stat_join(some_dict["Table"].value, table, ptable)

        prefix = "__TABLE0__" if table != ptable else ""
        id_dot_id_query = (
            f"{div_line1}\n"
            "SELECT\n"
            f"    *,\n"
            f"    {ppk} AS fk,\n"
            f"    {prefix}{column} AS {comp_col}\n"
            "FROM\n"
            f"    {joined_tables}\n"
            f"{div_line2}"
        )

        return id_dot_id_query

    def build_stat_join(self, src_table: str, src_table_query: str, dst_table: str) -> str:
        r"""Build SQL join between two table.

        Args:
            src_table (str): Source table.
            src_table_query (str): Source table representation (e.g., after filtering).
            dst_table (str): Destination table.

        Returns:
            join_query (str): SQL query with joined tables.
        """
        div_line1, div_line2 = get_div_lines("TABLES_JOIN")

        src_table, path = self.path_builder.find_shortest_path(src_table, dst_table)

        cur_table = src_table_query
        if path:
            cur_table = add_prefix(src_table_query, "__TABLE0__")

        cur_table = (
            "SELECT\n"
            "    *\n"
            "FROM\n"
            f"    {cur_table} __TABLE0__\n"
        )
        prev_table = src_table
        for i, (fk, table, edge_type) in enumerate(path):
            left_table = prev_table
            right_table = table

            if edge_type == "f":
                # fk on the source table
                left_col = f"__TABLE{i}__{fk}"
                right_col = self.db_explorer.find_pkey(right_table)
            else:
                # fk on the destination table
                left_pk = self.db_explorer.find_pkey(left_table)
                left_col = f"__TABLE{i}__{left_pk}"
                right_col = fk

            if i != len(path) - 1:
                right_table = add_prefix(right_table, f"__TABLE{i+1}__")
                right_col = f"__TABLE{i+1}__{right_col}"

            prev_table = table

            cur_table = (
                f"{cur_table}"
                f"JOIN\n"
                f"    {right_table} __TABLE{i+1}__\n"
                "ON\n"
                f"    __TABLE{i}__.{left_col} = __TABLE{i+1}__.{right_col}\n"
            )

        join_query = (
            f"({div_line1}\n"
            f"{cur_table}\n"
            f"{div_line2}\n)"
        )

        return join_query

    ################## Helper methods ##################

    def _clear_metadata(self) -> None:
        r"""Clear the metadata of the converter, including the error collector, CTEs, and CTE dictionary.

        Returns:
            out (None):
        """
        self.collector.clear()
        self.ctes = ""
        self.cte_dict = {}

    def _register_db(self) -> None:
        r"""Register all tables from the *`Database`* instance in the *`DuckDB`* connection.

        Returns:
            out (None):
        """
        self.conn = duckdb.connect()

        for name, table in self.db.table_dict.items():
            self.conn.register(name, table.df)
