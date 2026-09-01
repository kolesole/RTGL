"""Temporal RTGL converter class for time-series queries."""

import time

import pandas as pd

from rtgl.base import Database, Table
from rtgl.converter.converter import Converter
from rtgl.converter.utils import add_prefix, build_aggr_func, build_cte, format_query, get_div_lines
from rtgl.validator import TValidator


class TConverter(Converter):
    r"""Temporal RTGL converter class for temporal conversion RTGL -> SQL.

    Converts temporal (time-series) RTGL queries into SQL queries.
    Extends the base Converter class with concrete implementations
    for temporal prediction tasks with time window support.
    """

    def __init__(self, db: Database, timestamps: "pd.Series[pd.Timestamp]") -> None:
        r"""Initialize a temporal RTGL converter with timestamp support.

        Args:
            db (Database): Database object containing the tables.
            timestamps (pd.Series[pd.Timestamp]): Initial time points for predictions.

        Returns:
            out (None):
        """
        super().__init__(db)

        self.timestamps = timestamps
        self.validator_class = TValidator

    def convert(self, rtgl_query: str, execute: bool = False) -> str | Table:
        r"""Convert the temporal RTGL query string into an executable SQL query.

        Args:
            rtgl_query (str): The RTGL query string to be converted and executed.
            execute (bool): If True, executes the generated SQL query and returns the result as a Table.

        Returns:
            out (str | Table): The *`Table`* object containing the result of the executed SQL query (if execute=True),
                    with columns (*fk*, *timestamp*, *label*) corresponding to the translated RTGL query output.
                    Otherwise, returns the generated SQL query string (if execute=False).
        """
        self._clear_metadata()
        query_dict = self.parse_query(rtgl_query)
        query_dict = query_dict["QueryTmp"].value

        for_each_dict = query_dict["ForEach"].value
        ptable, ppk = self.build_for_each(for_each_dict)

        predict_dict = query_dict["Predict"].value
        sql_query = self.build_predict(predict_dict, ptable, ppk)

        # build WHERE query if exists, using PREDICT query as base
        if where := query_dict["Where"]:
            where_dict = where.value
            sql_query = self.build_assuming_where(where_dict, ptable, ppk, sql_query, context="WHERE")

        # build ASSUMING query if exists, using PREDICT query as base
        if assuming := query_dict["Assuming"]:
            assuming_dict = assuming.value
            sql_query = self.build_assuming_where(assuming_dict, ptable, ppk, sql_query, context="ASSUMING")

        label_fk = None
        select_clause = "*"
        filt = "label IS NOT NULL"
        if aggr := predict_dict["Aggregation"]:
            aggr_dict = aggr.value
            if aggr_dict["AggrType"].value.lower() == "list_distinct":
                # LIST_DISTINCT produces an array label, so a null child value survives inside the
                # array instead of making the whole row NULL - filter it out of the array directly,
                # and treat a label of exactly [NULL] (no real values matched) as equivalent to a
                # NULL scalar label. label_fk also needs special resolution here: the array elements
                # come from the aggregated column itself, which may be the aggregation table's own
                # primary key or a foreign key into another table, unlike every other aggregation
                # type where the label is just a plain scalar with no fkey semantics of its own.
                filt = f"{filt} AND label != [NULL]"
                select_clause = "fk, timestamp, list_filter(label, x -> x IS NOT NULL) AS label"
                _, table, table_obj, _ = self.db_explorer.find_table(
                    table=self.path_builder.find_orig_src_table(aggr_dict["Table"].value)
                )
                column = self.db_explorer.find_column(table, aggr_dict["Column"].value)
                label_fk = table if table_obj.pkey_col == column else table_obj.fkey_col_to_pkey_table.get(column)

        div_line1, div_line2 = get_div_lines("MAIN_QUERY")

        sql_query = (
            f"{self.ctes}"
            f"{div_line1}\n"
            "SELECT\n"
            f"    {select_clause}\n"
            "FROM\n"
            f"    ({sql_query}\n)\n"
            f"WHERE {filt}\n"
            "ORDER BY timestamp ASC, fk ASC;\n"
            f"{div_line2}"
        )

        if not execute:
            return sql_query

        if not self.conn:
            self._register_db()

        if ptable_inf := self.cte_dict.get(ptable):
            ptable_obj, _ = ptable_inf
            ptable_orig = ptable_obj.fkey_col_to_pkey_table.get(ppk)
            ptable_orig = self.db_explorer.find_orig_name(ptable_orig) if ptable_orig else None
        else:
            ptable_orig = self.db_explorer.find_orig_name(ptable)

        # execute SQL query and return result as Table
        start_time = time.time()
        df = self.conn.sql(sql_query).df()
        end_time = time.time()

        print(f"SQL query executed in {end_time - start_time:.2f} seconds")

        fkey_col_to_pkey_table = {"fk": ptable_orig} # fk column in output table corresponds to pk of parent table
        if label_fk: # label column in output table corresponds to pk or fk of aggregation table
            fkey_col_to_pkey_table["label"] = label_fk # only set for LIST_DISTINCT (see above)

        return Table(
            df=df,
            fkey_col_to_pkey_table=fkey_col_to_pkey_table,
            pkey_col=None,
            time_col="timestamp",  # mark timestamp as the time column
        )

    def build_for_each(self, for_each_dict: dict) -> tuple[str, str]:
        r"""Build a SQL query for the FOR EACH clause in temporal conversion.

        CROSS JOINS the parent table with timestamps.
        If the parent table has a time column, keeps only rows for which cur_timestamp >= time_col.

        Args:
            for_each_dict (dict): Parsed dictionary of the FOR EACH clause.

        Returns:
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
        """
        # extract parent table and primary key column
        ptable = for_each_dict["Table"].value
        ppk = self.db_explorer.find_column(ptable, for_each_dict["Column"].value)

        # build static WHERE query if exists to filter parent table rows before prediction
        where_query = (
            "SELECT\n"
            f"    *\n"
            "FROM\n"
            f"    {ptable}"
        )
        if where := for_each_dict["Where"]:
            where_query = self.build_stat_where(where.value, ptable, ppk)
            where_query = format_query(where_query)

        div_line1, div_line2 = get_div_lines("FILTERED_PARENT_CTE")

        parent_cte = build_cte(
            name="__FILTERED_PARENT__",
            body=(
                f"{div_line1}\n"
                "SELECT\n"
                "    *\n"
                "FROM\n"
                f"    {ptable}\n"
                "WHERE\n"
                f"    {ppk} IN (\n"
                f"SELECT {ppk} FROM (\n"
                f"{where_query}))\n"
                f"{div_line2}\n"
            )
        )
        self.ctes += ",\n" + parent_cte

        # filter parent table rows based on time column
        # if exists -> time_col must be <= timestamp
        # otherwise -> cross join with timestamps
        join = "CROSS JOIN"
        time_query = ""
        if time_col := self.db_explorer.find_time_column(ptable):
            join = "JOIN"
            time_query = (
                "ON\n"
                f"    __PARENT__.{time_col} <= __TIME__.timestamp\n"
            )

        div_line1, div_line2 = get_div_lines("FOR_EACH_CTE")

        for_each_cte = build_cte(
            name="__FOR_EACH__",
            body= (
                f"{div_line1}\n"
                "SELECT\n"
                f"    __PARENT__.{ppk} AS fk,\n"
                f"    __TIME__.timestamp AS timestamp\n"
                "FROM\n"
                f"    __FILTERED_PARENT__ __PARENT__\n"
                f"{join}\n"
                "    __TIMESTAMPS__ __TIME__\n"
                f"{time_query}"
                f"{div_line2}\n"
            )
        )
        self.ctes += ",\n" + for_each_cte + "\n"

        return ptable, ppk

    def build_predict(self, predict_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build the SQL query for the PREDICT clause in temporal conversion.

        Handle temporal prediction logic by cross-joining with prediction timestamps and
        implementing different label generation strategies based on prediction type.

        Args:
            predict_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            predict_query (str): SQL subquery returning (fk, timestamp, label) triples.
        """
        div_line1, div_line2 = get_div_lines("PREDICT")

        pred_type = predict_dict["PredType"]
        if pred_type == "aggregation":
            main_query = self.build_aggregation(predict_dict["Aggregation"].value, ptable, ppk)

            # determine label extraction logic based on modifiers
            if predict_dict["Classify"]:
                # CLASSIFY: use aggregated value directly
                label_query = "__MAIN__.comp_col"
            elif predict_dict["RankTop"]:
                # RANK_TOP K: keep only top K elements from aggregation
                k = int(predict_dict["K"].value)
                label_query = (
                    "CASE\n"
                    f"    WHEN ARRAY_LENGTH(__MAIN__.comp_col) > {k} THEN __MAIN__.comp_col[1:{k}]\n"
                    "    ELSE __MAIN__.comp_col\n"
                    "END"
                )
            else:
                # default: use full aggregated value
                label_query = "__MAIN__.comp_col"
        elif pred_type == "expr":
            main_query = self.build_expr(predict_dict["Expr"].value, ptable, ppk)

            label_query = (
                "CASE\n"
                "    WHEN __MAIN__.fk IS NOT NULL THEN TRUE\n"
                "    ELSE FALSE\n"
                "END"
            )
        else:
            pass

        main_query = format_query(main_query)
        label_query = format_query(label_query)

        predict_query = (
            f"{div_line1}\n"
            "SELECT\n"
            "    __FOR_EACH__.fk,\n"
            "    __FOR_EACH__.timestamp,\n"
            f"    {label_query} AS label\n"
            "FROM\n"
            "    __FOR_EACH__\n"
            "LEFT JOIN\n"
            f"    ({main_query}) __MAIN__\n"
            "ON\n"
            f"    __MAIN__.fk = __FOR_EACH__.fk\n"
            "AND\n"
            "    __MAIN__.timestamp = __FOR_EACH__.timestamp\n"
            f"{div_line2}"
        )

        return predict_query

    def build_assuming_where(self, some_dict: dict, ptable: str, ppk: str, predict_query: str, context: str) -> str:
        r"""Restrict a temporal prediction query using an ASSUMING or WHERE expression.

        Filter prediction results to keep only rows where the ASSUMING or WHERE condition is true.
        Works by joining the prediction results with the ASSUMING or WHERE expression on both fk and timestamp,
        preserving the label column only for matching rows.

        Args:
            some_dict (dict): Parsed dictionary of the ASSUMING or WHERE clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            predict_query (str): The SQL subquery for the PREDICT part (*fk*, *timestamp*, *label*).
            context (str): String indicating the context of the filter ("ASSUMING" or "WHERE").

        Returns:
            assuming_query (str): The SQL query filtering predictions using ASSUMING with temporal constraints.
        """
        div_line1, div_line2 = get_div_lines(context)

        expr_dict = some_dict["Expr"].value
        expr_query = self.build_expr(expr_dict, ptable, ppk)

        expr_query = format_query(expr_query)
        predict_query = format_query(predict_query)

        assuming_where_query = (
            f"{div_line1}\n"
            "SELECT\n"
            f"    __PREDICT__.*\n"
            "FROM\n"
            f"    ({predict_query}) __PREDICT__\n"
            "JOIN\n"
            f"    ({expr_query}) __EXPR__\n"
            "ON\n"
            f"    __EXPR__.fk = __PREDICT__.fk\n"
            "AND\n"
            "    __EXPR__.timestamp = __PREDICT__.timestamp\n"
            f"{div_line2}"
        )

        return assuming_where_query

    def build_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Recursively build a SQL query for a logical expression tree.

        Convert nested boolean expressions (from PREDICT, WHERE or ASSUMING clauses) into SQL.
        Combine sub-expressions using UNION (for OR) or INTERSECT (for AND) operations
        to return a set of (foreign key, timestamp) pairs where the expression evaluates to true.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query returning (*fk*, *timestamp*) pairs where the expression is true.
        """
        div_line1, div_line2 = get_div_lines("EXPR")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            left_expr = self.build_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = format_query(left_expr)
            right_expr = self.build_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = format_query(right_expr)

            # each side yields an independently-computed set of matching (fk, timestamp) pairs, so
            # AND/OR combine them as set operations (INTERSECT/UNION) rather than inline boolean logic
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
                "    fk,\n"
                "    timestamp\n"
                "FROM\n"
                f"    ({left_expr}) __LEFT_EXPR__\n"
                f"{filt}\n"
                "SELECT\n"
                "    fk,\n"
                "    timestamp\n"
                "FROM\n"
                f"    ({right_expr}) __RIGHT_EXPR__\n"
                f"{div_line2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk)

        return expr_query

    def build_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build the SQL query for a RTGL aggregation over a time window.

        Compute aggregations relative to prediction timestamps within a defined
        `(start, end]` time window (exclusive of the start boundary, inclusive of the end).

        Args:
            aggr_dict (dict): Parsed aggregation dictionary with Table, Start, End, MeasureUnit.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning (fk, col_for_comp, timestamp) where col_for_comp is aggregated.
        """
        div_line1, div_line2 = get_div_lines("AGGREGATION")

        # extract aggregation parameters
        start = float(aggr_dict["Start"].value)
        end = float(aggr_dict["End"].value)
        measure_unit = aggr_dict["MeasureUnit"].value.upper()

        aggr_table = aggr_table_name = self.path_builder.find_orig_src_table(aggr_dict["Table"].value)
        aggr_column = self.db_explorer.find_column(aggr_table, aggr_dict["Column"].value)

        # find time column for temporal filtering
        time_column = self.db_explorer.find_time_column(aggr_table)

        if aggr_table != ptable:
            aggr_dict["Column"].value = "__TABLE0__" + aggr_column
            time_column = "__TABLE0__" + time_column if time_column else None

        if aggr_column == "*":
            aggr_dict["Column"].value = ppk

        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict, time_column)
        aggr = format_query(aggr_func("__JOINED_TABLES__"))
        aggr_dict["Column"].value = aggr_column

        # build static WHERE query if exists to filter aggregation table rows before temporal aggregation
        if where := aggr_dict["Where"]:
            aggr_ppk = self.db_explorer.find_pkey(aggr_table)
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = format_query(aggr_table)
            aggr_table = f"({aggr_table}\n)"

        joined_tables = self.build_join(aggr_dict["Table"].value, aggr_table, ptable, (start, end, measure_unit))

        # if aggregation column is a foreign key to another table with a time column ->
        # -> perform temporal join with that table to filter aggregation rows
        aggr_parent_join = ""
        if (aggr_ptable := self.db_explorer.find_ptable(aggr_table_name, aggr_column)) and (
            aggr_ptable_time_col := self.db_explorer.find_time_column(aggr_ptable)
        ):
            aggr_ptable_pk = self.db_explorer.find_pkey(aggr_ptable)
            prefix = ""
            if aggr_table_name != ptable:
                prefix = "__TABLE0__"

            aggr_parent_join = (
                "JOIN\n"
                f"    {aggr_ptable} __AGGR_PARENT__\n"
                "ON\n"
                f"    __AGGR_PARENT__.{aggr_ptable_pk} = __JOINED_TABLES__.{prefix}{aggr_column}\n"
                "AND\n"
                f"    __AGGR_PARENT__.{aggr_ptable_time_col} <= __JOINED_TABLES__.timestamp\n"
            )

        aggr_query = (
            f"{div_line1}\n"
            "SELECT\n"
            f"    __FOR_EACH__.fk,\n"
            f"    __FOR_EACH__.timestamp,\n"
            f"    {aggr} AS comp_col\n"
            "FROM\n"
            "    __FOR_EACH__\n"
            "LEFT JOIN\n"
            f"    {joined_tables} __JOINED_TABLES__\n"
            "ON\n"
            f"    __JOINED_TABLES__.{ppk} = __FOR_EACH__.fk\n"
            "AND\n"
            f"    __JOINED_TABLES__.timestamp = __FOR_EACH__.timestamp\n"
            f"{aggr_parent_join}"
            "GROUP BY\n"
            f"    __FOR_EACH__.timestamp, __FOR_EACH__.fk\n"
            f"{div_line2}"
        )

        return aggr_query

    def build_ctes(self, injections: list[tuple[str, str, dict[str, str], str, str, str]]) -> None:
        r"""Build Common Table Expressions (CTEs) for the temporal RTGL query.

        Args:
            injections (list[tuple[str, str, dict[str, str], str]]): List of tuples containing
                (body, name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col, time_col)
                for each CTE to be built.

        Returns:
            out (None):
        """
        self._build_timestamp_cte()
        for body, name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col, time_col in injections:
            name = name.value.lower()
            div_line1, div_line2 = get_div_lines(f"{name.upper()}_CTE")

            cte = build_cte(
                name,
                body=(
                    f"{div_line1}\n"
                    f"{body}\n"
                    f"{div_line2}\n"
                )
            )
            self.ctes += ",\n" + cte

            self.cte_dict[name] = (Table(
                df=None,
                fkey_col_to_pkey_table={
                    fk_col.value.lower(): pkey_table.value.lower()
                    for fk_col, pkey_table in fkey_col_to_pkey_table.items()
                },
                pkey_col=pkey_col.lower() if pkey_col else None,
                time_col=time_col.lower() if time_col else None,
            ),
            {
                fk_table.value.lower(): fk_col.value.lower()
                for fk_table, fk_col in fkey_table_to_fkey_col.items()
            })

    def build_join(
        self, src_table: str, src_table_query: str, dst_table: str,
        time_interval: tuple[float, float, str], **kwargs: dict
    ) -> str:
        r"""Build a SQL query for joining source and destination tables with temporal constraints.

        Args:
            src_table (str): Name of the source table.
            src_table_query (str): SQL query for the source table.
            dst_table (str): Name of the destination table.
            time_interval (tuple[float, float, str]): Tuple containing (start, end, measure_unit)
                for the temporal window.
            **kwargs (dict): Additional keyword arguments.

        Returns:
            join_query (str): SQL query joining source and destination tables with temporal constraints.
        """
        div_line1, div_line2 = get_div_lines("TABLES_JOIN")

        start, end, measure_unit = time_interval

        src_table, path = self.path_builder.find_shortest_path(src_table, dst_table)

        prefix = ""
        cur_table = src_table_query
        if path:
            prefix = "__TABLE0__"
            cur_table = add_prefix(src_table_query, prefix)

        src_start_query = src_end_query = ""
        join = "CROSS JOIN"
        if src_time_col := self.db_explorer.find_time_column(src_table):
            if start != float("-inf"):
                src_start_query = (
                    "ON\n"
                    f"    __TABLE0__.{prefix}{src_time_col} > __TIME__.timestamp + INTERVAL '{start} {measure_unit}'\n"
                )

            if end != float("inf"):
                src_end_query = (
                    f"{'AND' if src_start_query else 'ON'}\n"
                    f"    __TABLE0__.{prefix}{src_time_col} <= __TIME__.timestamp + INTERVAL '{end} {measure_unit}'\n"
                )

            join = "JOIN"

        cur_table = (
            f"SELECT\n"
            "    *\n"
            "FROM\n"
            f"    {cur_table} __TABLE0__\n"
            f"{join}\n"
            "    __TIMESTAMPS__ __TIME__\n"
            f"{src_start_query}"
            f"{src_end_query}"
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

            join = "JOIN"
            start_query = end_query = ""
            if i != len(path) - 1:
                right_table = add_prefix(right_table, f"__TABLE{i+1}__")
                right_col = f"__TABLE{i+1}__{right_col}"

                if time_col := self.db_explorer.find_time_column(table):
                    if start != float("-inf"):
                        start_query = (
                            "AND\n"
                            f"    __TABLE{i+1}__.__TABLE{i+1}__{time_col} > __TIME__.timestamp"
                            f" + INTERVAL '{start} {measure_unit}'\n"
                        )

                    if end != float("inf"):
                        end_query = (
                            "AND\n"
                            f"    __TABLE{i+1}__.__TABLE{i+1}__{time_col} <= __TIME__.timestamp"
                            f" + INTERVAL '{end} {measure_unit}'\n"
                        )

            prev_table = table

            cur_table = (
                f"{cur_table}\n"
                f"{join}\n"
                f"    {right_table} __TABLE{i+1}__\n"
                "ON\n"
                f"    __TABLE{i}__.{left_col} = __TABLE{i+1}__.{right_col}\n"
                f"{start_query}"
                f"{end_query}"
            )

        join_query = (
            f"({div_line1}\n"
            f"{cur_table}\n"
            f"{div_line2}\n)"
        )

        return join_query

    def set_timestamps(self, timestamps: "pd.Series[pd.Timestamp]") -> None:
        r"""Set the prediction timestamps for the temporal converter.

        Args:
            timestamps (pd.Series[pd.Timestamp]): The new prediction timestamps to be used for conversion.

        Returns:
            out (None):
        """
        self.timestamps = timestamps

    ################## Helper methods ##################

    def _build_timestamp_cte(self) -> None:
        r"""Build CTE (Common Table Expression) for the prediction timestamps.

        Returns:
            out (None):
        """
        div_line1, div_line2 = get_div_lines("TIMESTAMPS_CTE")

        values = ",".join([f"(TIMESTAMP '{timestamp}')" for timestamp in self.timestamps])

        timestamp_cte = "WITH " + build_cte(
            name="__TIMESTAMPS__",
            body=(
                f"{div_line1}\n"
                "SELECT\n"
                "    *\n"
                "FROM\n"
                f"   (VALUES {values}) AS tmp(timestamp)\n"
                f"{div_line2}\n"
            )
        )

        self.ctes = timestamp_cte
