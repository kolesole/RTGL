"""Temporal query validator class for RTGL."""

from rtgl.base import DatabaseExplorer, PathBuilder
from rtgl.validator.diagnostics import IssueCollector
from rtgl.validator.validator import AggrContext, IdDotIdContext, Validator
from rtgl.visitor import ParsedValue


class TValidator(Validator):
    r"""Validator for temporal RTGL queries.

    Implements abstract methods from the base *`Validator`* class.
    In addition, implements validation logic for ASSUMING clause.
    """

    def __init__(self, collector: IssueCollector, db_explorer: DatabaseExplorer, path_builder: PathBuilder) -> None:
        r"""Initialize the temporal validator with an error collector, database explorer, and path builder.

        Args:
            collector (IssueCollector): *`IssueCollector`* to accumulate validation errors.
            db_explorer (DatabaseExplorer): *`DatabaseExplorer`* used to resolve table/column
                names and look up CTE/SQL-injection relations.
            path_builder (PathBuilder): *`PathBuilder`* used to resolve joins and CPEs.

        Returns:
            out (None):
        """
        super().__init__(collector, db_explorer, path_builder)

    def validate(self, query_dict: dict) -> None:
        r"""Validate a parsed query dictionary.

        Ensure the query is temporal (not static) and delegate to validate_query.

        Args:
            query_dict (dict): Parsed query dictionary from the visitor.

        Returns:
            out (None):
        """
        # validate declared CPEs and SQL injections regardless of whether they end up used
        self.validate_predefined_paths(query_dict["PredefinedPaths"])
        self.validate_injections(query_dict["Injections"])

        # check if the query is temporal
        if query := query_dict["QueryTmp"]:
            self.validate_query(query)
        elif query := query_dict["QueryStat"]:
            self.collector.add_error(
                line=query.line,
                column=query.column,
                msg="For temporal converter, only temporal queries are supported, found static query"
            )

    def validate_query(self, query: ParsedValue) -> None:
        r"""Validate all components of a temporal query.

        Args:
            query (ParsedValue): Parsed temporal query to validate.

        Returns:
            out (None):
        """
        if query is None:
            return

        query_dict = query.value
        # validate FOR EACH clause and get parent table name
        # if FOR EACH is not present -> end validation
        # otherwise -> validate PREDICT, WHERE, and ASSUMING clauses
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name)
            self.validate_where(query_dict["Where"], ptable_name)
            self.validate_assuming(query_dict["Assuming"], ptable_name)

    def validate_aggregation(self, aggr: ParsedValue, ptable_name: str, context: AggrContext) -> None:
        r"""Validate a temporal aggregation with time window constraints.

        Check that:
        - Start < End
        - Time ranges are non-negative in PREDICT or ASSUMING (looking forward)
        - Time ranges are non-positive in WHERE (looking backward)

        Args:
            aggr (ParsedValue): Parsed aggregation to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the aggregation appears.

        Returns:
            out (None):
        """
        if aggr is None:
            return

        aggr_dict = aggr.value

        table_token = aggr_dict["Table"]
        column_token = aggr_dict["Column"]

        # validate table.column in the aggregation
        self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_TMP_AGGR)

        # validate WHERE clause inside the aggregation if present
        if where := aggr_dict["Where"]:
            if not self.db_explorer.find_pkey(table_token.value) and not where.value["IsSimple"]:
                self.collector.add_error(
                    line=table_token.line,
                    column=table_token.column,
                    msg=(
                        f"Table '{table_token.value}' in temporal aggregation does not have a primary key column, "
                        "which is required for non-simple WHERE filtering (when the WHERE clause references "
                        "tables other than the aggregation's own table)"
                    )
                )
            self.validate_where(where, table_token.value, stat=True)

        # validate temporal window constraints
        start_token = aggr_dict["Start"]
        start = float(start_token.value)
        end_token = aggr_dict["End"]
        end = float(end_token.value)

        # start time must be less than end time
        if start >= end:
            self.collector.add_error(
                line=start_token.line,
                column=start_token.column,
                msg=(
                    "Start time must be less than end time in temporal aggregation, "
                    f"found start={start}, end={end}"
                )
            )

        # PREDICT and ASSUMING look forward in time (non-negative range)
        if context in [AggrContext.FROM_PREDICT, AggrContext.FROM_ASSUMING] and (start < 0 or end < 0):
            self.collector.add_error(
                line=start_token.line,
                column=start_token.column,
                msg=(
                    "Start and end time in temporal aggregation must be non-negative in PREDICT and ASSUMING clauses"
                    f", found start={start}, end={end}"
                )
            )

        # WHERE looks backward in time (non-positive range)
        if context == AggrContext.FROM_WHERE and (start > 0 or end > 0):
            self.collector.add_error(
                line=start_token.line,
                column=start_token.column,
                msg=(
                    "Start and end time in temporal aggregation must be non-positive in WHERE clause, "
                    f"found start={start}, end={end}"
                )
            )

    def validate_assuming(self, assuming: ParsedValue, ptable_name: str) -> None:
        r"""Validate ASSUMING clause.

        Delegates to `validate_expr` with `AggrContext.FROM_ASSUMING`.

        Args:
            assuming (ParsedValue): Parsed ASSUMING clause.
            ptable_name (str): Name of the parent table.

        Returns:
            out (None):
        """
        if assuming is None:
            return

        assuming_dict = assuming.value

        self.validate_expr(assuming_dict["Expr"], ptable_name, AggrContext.FROM_ASSUMING)
