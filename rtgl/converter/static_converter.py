"""Static RTGL converter class for non-temporal queries."""

import time

from rtgl.base import Database, Table
from rtgl.converter.converter import Converter
from rtgl.converter.utils import build_cte, format_query, get_div_lines
from rtgl.validator import SValidator


class SConverter(Converter):
    r"""Static RTGL converter class for static conversion RTGL -> SQL.

    Converts static (non-temporal) RTGL queries into SQL queries.
    Extends the base Converter class with concrete implementations
    for static prediction tasks.
    """

    def __init__(self, db: Database) -> None:
        r"""Initialize a static RTGL converter.

        Args:
            db (Database): Database object containing the tables.

        Returns:
            out (None):
        """
        super().__init__(db)
        self.validator_class = SValidator

    def convert(self, rtgl_query: str, execute: bool = False) -> str | Table:
        r"""Convert the static RTGL query string into an executable SQL query.

        Args:
            rtgl_query (str): The RTGL query string to be converted and executed.
            execute (bool): If True, executes the generated SQL query and returns the result as a Table.

        Returns:
            out (str | Table): The *`Table`* object containing the result of the executed SQL query (if execute=True),
                    with columns (*fk*, *label*) corresponding to the translated RTGL query output.
                    Otherwise, returns the generated SQL query string (if execute=False).
        """
        self._clear_metadata()
        query_dict = self.parse_query(rtgl_query)
        query_dict = query_dict["QueryStat"].value

        for_each_dict = query_dict["ForEach"].value
        ptable, ppk = self.build_for_each(for_each_dict)

        predict_dict = query_dict["Predict"].value
        sql_query = self.build_predict(predict_dict, ptable, ppk)

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
                select_clause = "fk, list_filter(label, x -> x IS NOT NULL) AS label"
                _, table, table_obj, _ = self.db_explorer.find_table(
                    table=self.path_builder.find_orig_src_table(aggr_dict["Table"].value)
                )
                column = self.db_explorer.find_column(table, aggr_dict["Column"].value)

                label_fk = table if table_obj.pkey_col == column else table_obj.fkey_col_to_pkey_table.get(column)

        div_line1, div_line2 = get_div_lines("MAIN_QUERY")

        sql_query = (
            f"{self.ctes}"
            f"{div_line1}\n"
            f"SELECT\n"
            f"    {select_clause}\n"
            "FROM\n"
            f"    ({sql_query}\n)\n"
            f"WHERE {filt}\n"
            "ORDER BY fk ASC\n;\n"
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
        if label_fk:  # label column in output table corresponds to pk or fk of aggregation table
            fkey_col_to_pkey_table["label"] = label_fk # only set for LIST_DISTINCT (see above)

        return Table(
            df=df,
            fkey_col_to_pkey_table=fkey_col_to_pkey_table,
            pkey_col=None,
            time_col=None,
        )

    def build_for_each(self, for_each_dict: dict) -> tuple[str, str]:
        r"""Build a SQL query for the FOR EACH clause in static conversion.

        Args:
            for_each_dict (dict): Parsed dictionary of the FOR EACH clause.

        Returns:
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
        """
        div_line1, div_line2 = get_div_lines("FOR_EACH")

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
                f"    *\n"
                "FROM\n"
                f"    {ptable}\n"
                "WHERE\n"
                f"    {ppk} IN (\n"
                f"SELECT {ppk} FROM (\n"
                f"{where_query}))\n"
                f"{div_line2}\n"
            )
        )
        self.ctes += (",\n" if self.ctes else "WITH ") + parent_cte

        div_line1, div_line2 = get_div_lines("FOR_EACH_CTE")

        for_each_cte = build_cte(
            name="__FOR_EACH__",
            body= (
                f"{div_line1}\n"
                "SELECT\n"
                f"    {ppk} AS fk\n"
                "FROM\n"
                f"    __FILTERED_PARENT__\n"
                f"{div_line2}\n"
            )
        )
        self.ctes += ",\n" + for_each_cte + "\n"

        return ptable, ppk

    def build_predict(self, query_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build a SQL query for the PREDICT clause in static conversion.

        Args:
            query_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            predict_query (str): SQL subquery returning (fk, label) pairs.
        """
        div_line1, div_line2 = get_div_lines("PREDICT")

        pred_type = query_dict["PredType"]
        if pred_type == "aggregation":
            main_query = self.build_aggregation(query_dict["Aggregation"].value, ptable, ppk)
            label_query = "__MAIN__.comp_col"
        elif pred_type == "expr":
            main_query = self.build_expr(query_dict["Expr"].value, ptable, ppk)
            label_query = "CASE\n    WHEN __MAIN__.fk IS NOT NULL THEN TRUE\n    ELSE FALSE\nEND"
        elif pred_type == "id_dot_id":
            main_query = self.build_id_dot_id(query_dict, ptable, ppk)
            label_query = "__MAIN__.comp_col"
        else:
            pass

        main_query = format_query(main_query)
        label_query = format_query(label_query)

        predict_query = (
            f"{div_line1}\n"
            "SELECT\n"
            "    __FOR_EACH__.fk AS fk,\n"
            f"    {label_query} AS label\n"
            "FROM\n"
            "    __FOR_EACH__\n"
            "LEFT JOIN\n"
            f"    ({main_query}) __MAIN__\n"
            "ON\n"
            "    __MAIN__.fk = __FOR_EACH__.fk\n"
            f"{div_line2}"
        )

        return predict_query

    def build_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build a SQL query for a logical expression tree.

        Delegates to *build_stat_expr* on the base *`Converter`* class.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query returning foreign keys where the expression is true.
        """
        expr_query = self.build_stat_expr(expr_dict, ptable, ppk)

        return expr_query

    def build_where(self, where_dict: dict, ptable: str, ppk: str, predict_query: str) -> str:
        r"""Build a SQL query for the WHERE clause in static conversion.

        Combine the PREDICT query with the expression from the WHERE clause using JOIN
        to filter the predicted foreign keys based on the expression.

        Args:
            where_dict (dict): Parsed dictionary of the WHERE clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            predict_query (str): SQL query from the PREDICT clause, providing fk and label columns.

        Returns:
            where_query (str): SQL query returning (fk, label) pairs filtered by the WHERE expression.
        """
        div_line1, div_line2 = get_div_lines("WHERE")

        expr_dict = where_dict["Expr"].value
        expr_query = self.build_expr(expr_dict, ptable, ppk)

        expr_query = format_query(expr_query)
        predict_query = format_query(predict_query)

        where_query = (
            f"{div_line1}\n"
            "SELECT\n"
            "    __PREDICT__.*\n"
            "FROM\n"
            f"    ({predict_query}) __PREDICT__\n"
            "JOIN\n"
            f"    ({expr_query}\n) __EXPR__\n"
            "ON\n"
            "    __PREDICT__.fk = __EXPR__.fk\n"
            "ORDER BY\n"
            "    __PREDICT__.fk ASC\n"
            f"{div_line2}"
        )

        return where_query

    def build_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Build a SQL query for a static RTGL aggregation.

        Delegates to *build_stat_aggregation* on the base *`Converter`* class.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary containing 'Table', 'Column', 'Where'(optional) keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning pairs (fk, comp_col).
        """
        aggr_query = self.build_stat_aggregation(aggr_dict, ptable, ppk)

        return aggr_query

    def build_ctes(self, injections: list[tuple[str, str, dict[str, str], str]]) -> None:
        r"""Build Common Table Expressions (CTEs) for the static RTGL query.

        Args:
            injections (list[tuple[str, str, dict[str, str], str]]): List of tuples containing
                (body, name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col) for each CTE to be built.

        Returns:
            out (None):
        """
        for body, name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col in injections:
            name = name.value.lower()
            div_line1, div_line2 = get_div_lines(f"{name.upper()}_CTE")

            cte = build_cte(
                name=name,
                body=(
                    f"{div_line1}\n"
                    f"{body}\n"
                    f"{div_line2}\n"
                )
            )
            self.ctes += cte + ",\n"

            self.cte_dict[name] = (Table(
                df=None,
                fkey_col_to_pkey_table={
                    fk_col.value.lower(): pk_table.value.lower()
                    for fk_col, pk_table in fkey_col_to_pkey_table.items()
                },
                pkey_col=pkey_col if pkey_col else None,
                time_col=None,
            ),
            {
                fk_table.value.lower(): fk_col.value.lower()
                for fk_table, fk_col in fkey_table_to_fkey_col.items()
            })

        if self.ctes:
            self.ctes = "WITH " + self.ctes[:-2]

    def build_join(self, src_table: str, src_table_query: str, dst_table: str, **kwargs: dict) -> str:
        r"""Build a SQL query for joining two tables in static conversion.

        Delegates to *build_stat_join* on the base *`Converter`* class.

        Args:
            src_table (str): Source table.
            src_table_query (str): SQL query for the source table.
            dst_table (str): Destination table.
            kwargs (dict): Additional keyword arguments.

        Returns:
            join_query (str): SQL query with joined tables.
        """
        return self.build_stat_join(src_table, src_table_query, dst_table)
