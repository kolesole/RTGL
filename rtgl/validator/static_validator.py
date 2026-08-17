"""Static query validator class for RTGL."""

from rtgl.base import Database
from rtgl.converter.path_builder import PathBuilder
from rtgl.validator.diagnostics import IssueCollector
from rtgl.validator.validator import AggrContext, IdDotIdContext, Validator
from rtgl.visitor import ParsedValue


class SValidator(Validator):
    r"""Validator for static (non-temporal) RTGL queries.

    Implements abstract methods from the base *`Validator`* class.
    """

    def __init__(self, collector: IssueCollector, db: Database) -> None:
        """Initializes the Static Validator with an error collector and database.

        Args:
            collector (ErrorCollector): *`ErrorCollector`* to accumulate validation errors.
            db (Database): *`Database`* instance containing schema information.

        Returns:
            out (None):
        """
        super().__init__(collector, db)

    def validate(self, query_dict: dict, cte_dict: dict, path_builder: PathBuilder) -> None:
        r"""Validates a parsed query dictionary.

        Ensures the query is static (not temporal) and delegates to validate_query.

        Args:
            query_dict (dict): Parsed query dictionary from the visitor.

        Returns:
            out (None):
        """
        self.cte_dict = cte_dict
        self.path_builder = path_builder

        # check if the query is static
        if query := query_dict["QueryStat"]:
            self.validate_query(query)
        elif query := query_dict["QueryTmp"]:
            self.collector.add_error(
                line=query.line,
                column=query.column,
                msg="For static converter, only static queries are supported, found temporal query"
            )

        self.cte_dict = {}
        self.path_builder = None

    def validate_query(self, query: ParsedValue) -> None:
        r"""Validates all components of a static query.

        Args:
            query (ParsedValue): Parsed static query to validate.

        Returns:
            out (None):
        """
        if query is None:
            return

        query_dict = query.value
        # validate FOR EACH clause and get parent table name
        # if FOR EACH is not present -> end validation
        # otherwisr -> validate PREDICT AND WHERE clauses
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name)
            self.validate_where(query_dict["Where"], ptable_name)

    def validate_aggregation(self, aggr: ParsedValue, ptable_name: str, context: AggrContext) -> None:
        r"""Validates a static aggregation.

        Args:
            aggr (ParsedValue): Parsed aggregation to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the aggregation appears.
                Does not affect validation logic for static queries.

        Returns:
            out (None):
        """
        self.validate_stat_aggregation(aggr, ptable_name)

    def validate_id_dot_id(
        self, table_token: ParsedValue, column_token: ParsedValue, ptable_name: str, context: str
    ) -> None:
        r"""Validates a table.column reference in a static query.

        Checks that the table exists, is connected to the parent table,
        and that the column exists in that table.

        Args:
            table_token (ParsedValue): Parsed table name.
            column_token (ParsedValue): Parsed column name.
            ptable_name (str): Name of the parent table.
            context (str): Context where this reference appears.

        Returns:
            out (None):
        """
        table_name = table_token.value

        # check table existence
        if not self._is_table_in_db(table_name):
            self.collector.add_error(
                line=table_token.line,
                column=table_token.column,
                msg=f"Table '{table_name}' in {context} does not exist"
            )

        # check table relationship with parent
        if not self._has_conn_with_main_table(table_name, ptable_name):
            self.collector.add_error(
                line=table_token.line,
                column=table_token.column,
                msg=f"Table '{table_name}' in {context} is not connected (path does not exist) to main table '{ptable_name}'"
            )

        column_name = column_token.value
        
        # check column existence
        if not self._is_column_in_table(table_name, column_name):
            self.collector.add_error(
                line=column_token.line,
                column=column_token.column,
                msg=f"Column '{column_name}' in {context} does not exist in table '{table_name}'"
            )

        # FOR EACH requires a primary key column
        if context == IdDotIdContext.FROM_FOR_EACH and not self._is_pkey_col(table_name, column_name):
            self.collector.add_error(
                line=column_token.line,
                column=column_token.column,
                msg=f"Column '{column_name}' in {context} is not a primary key column of table '{table_name}'"
            )
