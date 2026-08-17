"""Base RTGL converter class."""

import sys
from abc import ABC, abstractmethod

import duckdb
from antlr4 import CommonTokenStream, InputStream

from rtgl.base import Database, Table
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
from rtgl.converter.path_builder import PathBuilder
from rtgl.validator import IssueCollector, Validator
from rtgl.visitor import Visitor


class Converter(ABC):
    r"""Base abstract RTGL converter class for conversion RTGL -> SQL.

    Provides shared functionality for temporal and static RTGL converters.
    Some methods are abstract and must be implemented by concrete subclasses,
    but others provide common logic used in both static and temporal conversion.
    """

    def __init__(self, db: Database) -> None:
        r"""Base constructor.

        Initializes *`Database`* instance and normalized version, *`Visitor`* instance, 
        and *`ErrorCollector`* instance for storing validation errors.

        Args:
            db (Database): *`Database`* instance containing the schema and data tables to be queried.

        Returns:
            out (None):
        """
        self.conn = None
        self.db = db
        self.norm_db = self._normalize_db()

        self.visitor = Visitor()
        self.validator = None
        self.collector = IssueCollector()
        self.ctes = ""
        self.cte_dict = {}
        self.path_builder = None

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
        r"""Abstrac method to build the SQL query for the for each part of the RTGL query.

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
        r"""Parses the RTGL query string into a dictionary representation.

        Parses a query, builds CTEs, and validates a dictionary representation, prints all errors on stderr
        and exit the program if any errors were found.

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

        query_dict, injections, predict_path = self.visitor.visit(tree)
        self.build_ctes(injections)
        self.path_builder = PathBuilder(self.norm_db, self.cte_dict, predict_path)

        if self.validator:
            self.validator.validate(query_dict, self.cte_dict, self.path_builder)

        # semantic warnings and errors collected during validation
        self.collector.report(after_syntax_validation=False)

        return query_dict

    def build_stat_where(self, where_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds the SQL query for the static WHERE part of the RTGL query.

        Filters a ptable before using.

        Args:
            where_dict (dict): Dictionary representation of the WHERE part of the RTGL query.
            ptable (str): Name of the parent table.
            ppkey (str): Name of the primary key column in the parent table.

        Returns:
            where_query (str): SQL query string representing the filtered ptable.
        """
        # create division markers for formatted output
        div_line1, div_line2 = get_div_lines("STAT_WHERE")

        if where_dict["IsSimple"] and self.path_builder.find_orig_src_table(where_dict["Table"]) == ptable:
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
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_simple_expr(expr_dict["LeftExpr"])
            # build right expression
            right_expr = self.build_simple_expr(expr_dict["RightExpr"])
        
            # check operation and convert to SQL format for tables
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
        # check condition type and build main query for condition accordingly
        # aggregation / id_dot_id
        cond_type = cond_dict["CondType"]
        match cond_type:
            case "aggregation":
                pass
            case "id_dot_id":
                pass
            case _:
                pass

        # column to compare in condition
        comp_col = cond_dict["Column"].value

        # check value condition type and build condition accordingly
        # num / str / null
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

        # handle NOT operator
        not_op = "NOT " if cond_dict["NOT"] else ""

        # build final condition query
        cond_query = f"{not_op}{cond(comp_col)}"
        

        return cond_query

    def build_stat_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds a SQL query for the static expression part of the RTGL query.

        Args:
            expr_dict (dict): Dictionary representation of the expr part of the RTGL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query string representing the expr part of the RTGL query.
        """
        # create division markers for formatted output
        div_line1, div_line2 = get_div_lines("STAT_EXPR")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_stat_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = format_query(left_expr)
            # build right expression
            right_expr = self.build_stat_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = format_query(right_expr)

            # check operation and convert to SQL format for tables
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
        r"""Builds a SQL query for a condition part of the RTGL query.

        Args:
            cond_dict (dict): Dictionary representation of the condition part of the RTGL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            stat (bool): Flag indicating whether the condition is part of a static expression or not.

        Returns:
            cond_query (str): SQL query string representing the condition part of the RTGL query.
        """
        # create division markers for formatted output
        div_line1, div_line2 = get_div_lines("CONDITION")

        # check condition type and build main query for condition accordingly
        # aggregation / id_dot_id
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

        # column to compare in condition
        comp_col = "comp_col"

        # check value condition type and build condition accordingly
        # num / str / null
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

        # handle NOT operator
        not_op = "NOT " if cond_dict["NOT"] else ""

        # build final condition query
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
        r"""Builds a SQL query for a static RTGL aggregation.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary containing 'Table', 'Column', 'Where'(optional) keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning pairs (fk, comp_col).
        """
        # create division markers for formatted output
        div_line1, div_line2 = get_div_lines("STAT_AGGREGATION")

        # extract aggregation table
        aggr_table = aggr_table_name = self.path_builder.find_orig_src_table(aggr_dict["Table"].value)
        aggr_column = self._find_column(aggr_table, aggr_dict["Column"].value)
        
        if aggr_table != ptable:
            aggr_dict["Column"].value = f"__TABLE0__" + aggr_column
            
        if aggr_column == "*":
            aggr_dict["Column"].value = ppk
        
        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict)
        aggr = format_query(aggr_func("__JOINED_TABLES__"))
        aggr_dict["Column"].value = aggr_column
        
        # build static WHERE query if exists
        if where := aggr_dict["Where"]:
            aggr_ppk = self._find_pkey(aggr_table)
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = f"({aggr_table}\n)"

        joined_tables = self.build_stat_join(aggr_dict["Table"].value, aggr_table, ptable)

        # build aggregation query
        aggr_query = (
            f"{div_line1}\n"
            "SELECT\n"
            f"    __JOINED_TABLES__.{ppk} AS fk,\n"
            f"    {aggr} AS comp_col\n"
            "FROM\n"
            f"    {joined_tables} __JOINED_TABLES__\n"
            "GROUP BY\n"
            f"    __JOINED_TABLES__.{ppk}\n"
            f"{div_line2}"
        )

        return aggr_query

    def build_id_dot_id(self, some_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds the SQL query for a table.column(id_dot_id) part of the RTGL query.

        Args:
            some_dict (dict): Dictionary containing 'Table', 'Column' keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            id_dot_id_query (str): SQL query string representing the id_dot_id part of the RTGL query.
        """
        # create division markers for formatted output
        div_line1, div_line2 = get_div_lines("ID_DOT_ID")

        table = self.path_builder.find_orig_src_table(some_dict["Table"].value)
        column = self._find_column(table, some_dict["Column"].value)

        # column to compare in condition
        comp_col = "comp_col"

        joined_tables = self.build_stat_join(some_dict["Table"].value, table, ptable)

        prefix = f"__TABLE0__" if table != ptable else ""
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
        r"""Builds SQL join between two table.
        
        Args:
            src_table (str): Source table.
            src_table_query (str): Source table representation (e.g., after filtering).
            dst_table (str): Destination table.
        
        Returns:
            join_query (str): SQL query with joined tables.
        """
        # create division markers for formatted output
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
                right_col = self._find_pkey(right_table)
            else:
                # fk on the destination table
                left_pk = self._find_pkey(left_table)
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

    def _normalize_table(self, table_obj: Table) -> Table:
        r"""Normalizes a *`Table`* object by converting all column names to lowercase.

        Args:
            table_obj (Table): *`Table`* object to be normalized.
        
        Returns:
            out (Table): Normalized *`Table`* object with lowercase column names.
        """
        return Table(
            df=table_obj.df.head(0).rename(columns=str.lower) if table_obj.df is not None else None,
            fkey_col_to_pkey_table={fkey.lower(): ptable for fkey, ptable in table_obj.fkey_col_to_pkey_table.items()},
            pkey_col=table_obj.pkey_col.lower() if table_obj.pkey_col else None,
            time_col=table_obj.time_col.lower() if table_obj.time_col else None,
        )

    def _normalize_db(self) -> Database:
        r"""Normalizes a *`Database`* instance by converting all table and column names to lowercase.
        
        Returns:
            out (Database): Normalized *`Database`* instance with lowercase table and column names.
        """
        return Database(
            table_dict={name.lower(): self._normalize_table(table) 
                for name, table in self.db.table_dict.items()} if self.db.table_dict else {}
        )

    def _clear_metadata(self) -> None:
        r"""Clears the metadata of the converter, including the error collector, CTEs, and CTE dictionary.
        
        Returns:
            out (None):
        """
        self.collector.clear()
        self.ctes = "" 
        self.cte_dict = {}

    def _register_db(self) -> None:
        """Registers all tables from the *`Database`* instance in the *`DuckDB`* connection.

        Returns:
            out (None):
        """
        if self.conn:
            return

        self.conn = duckdb.connect()

        for name, table in self.db.table_dict.items():
            self.conn.register(name, table.df)

    def _find_table(self, table: str) -> tuple[str, Table, dict[str, str] | None] | None:
        r"""Finds a *`Table`* object in the *`Database`* by its name (case-insensitive).

        Args:
            table (str): Name of the table to find.

        Returns:
            out (tuple[str, Table] | None): Tuple of the form (original_table_name, Table)
                Returns None if no table with the given name was found.
        """
        table_lower = table.lower()

        if cte_inf := self.cte_dict.get(table_lower):
            return table_lower, *cte_inf
        
        if table_obj := self.norm_db.table_dict.get(table_lower):
            return table_lower, table_obj, None

        return None

    def _find_column(self, table: str, column: str) -> str | None:
        r"""Finds a column name in a table (case-insensitive).

        Args:
            table (str): Name of the table.
            column (str): Name of the column to find.

        Returns:
            out (str | None): Original name of the column if found, None otherwise.
        """
        _, table_obj, _ = self._find_table(table)

        if table_obj:
            # if column is "*" -> return primary key column
            if column == "*":
                return table_obj.pkey_col if table_obj.pkey_col else "*"
        
            return column.lower()
                
        return None

    def _find_ptable(self, table: str, fk: str) -> str | None:
        r"""Finds the parent table name that a given table references through a given foreign key (case-insensitive).

        Args:
            table (str): Name of the child table.
            fk (str): Name of the foreign key column in the child table.

        Returns:
            out (str | None): Name of the parent table that the child table references through the foreign key column
                if found, None otherwise.
        """
        table_lower, fk_lower = table.lower(), fk.lower()

        for cte_name, (_, fkey_table_col) in self.cte_dict.items():
            if (fk_col := fkey_table_col.get(table_lower)) and (fk_col == fk_lower):
                return cte_name

        _, table_obj, _ = self._find_table(table)
        
        return table_obj.fkey_col_to_pkey_table.get(fk_lower) if table_obj else None

    def _find_fk(self, ctable: str, ptable: str, ppk: str) -> str | None:
        r"""Finds the foreign key column in a child table that references the parent table (case-insensitive).

        Args:
            ctable (str): Name of the child table.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            out (str | None): Name of the foreign key column in the child table if found, None otherwise.
        """
        ctable_lower, ptable_lower = ctable.lower(), ptable.lower()

        # if child and parent table are the same -> return primary key
        if ctable_lower == ptable_lower:
            return ppk

        _, ctable_obj, _ = self._find_table(ctable)

        if cte_inf := self.cte_dict.get(ptable_lower):
            return cte_inf[1].get(ctable_lower)
        
        # fk ... name of foreign key column in child table
        # parent_table ... name of referenced parent table
        for fk, parent_table in ctable_obj.fkey_col_to_pkey_table.items():
            if parent_table == ptable_lower:
                return fk
        
        return None

    def _find_pkey(self, table: str) -> str | None:
        r"""Finds the primary key column of a table (case-insensitive).

        Args:
            table (str): Name of the table.

        Returns:
            out (str | None): Name of the primary key column of the table if found, None otherwise.
        """
        _, table_obj, _ = self._find_table(table)
        return table_obj.pkey_col
    
    def _find_orig_name(self, table: str) -> str | None:
        r"""Finds the original name of a table (case-insensitive).

        Args:
            table (str): Name of the table.

        Returns:
            out (str | None): Original name of the table if found, None otherwise.
        """
        for orig_name in self.db.table_dict.keys():
            if orig_name.lower() == table.lower():
                return orig_name
        
        return table
    