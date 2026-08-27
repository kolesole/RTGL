"""Static query validator class for RTGL."""

from rtgl.base import DatabaseExplorer, Database
from rtgl.base.path_builder import PathBuilder
from rtgl.validator.diagnostics import IssueCollector
from rtgl.validator.validator import AggrContext, Validator
from rtgl.visitor import ParsedValue


class SValidator(Validator):
    r"""Validator for static (non-temporal) RTGL queries.

    Implements abstract methods from the base *`Validator`* class.
    """

    def __init__(self, collector: IssueCollector, db_explorer: DatabaseExplorer, path_builder: PathBuilder) -> None:
        r"""Initialize the static validator with an error collector, database explorer, and path builder.

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

        Ensure the query is static (not temporal) and delegate to validate_query.

        Args:
            query_dict (dict): Parsed query dictionary from the visitor.

        Returns:
            out (None):
        """
        # validate declared CPEs and SQL injections
        self.validate_predefined_paths(query_dict["PredefinedPaths"])
        self.validate_injections(query_dict["Injections"])

        # check if the query is static
        if query := query_dict["QueryStat"]:
            self.validate_query(query)
        elif query := query_dict["QueryTmp"]:
            self.collector.add_error(
                line=query.line,
                column=query.column,
                msg="For static converter, only static queries are supported, found temporal query"
            )

    def validate_query(self, query: ParsedValue) -> None:
        r"""Validate all components of a static query.

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
        # otherwise -> validate PREDICT AND WHERE clauses
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name, stat=True)
            self.validate_where(query_dict["Where"], ptable_name, stat=True)

    def validate_aggregation(self, aggr: ParsedValue, ptable_name: str, context: AggrContext) -> None:
        r"""Validate a static aggregation.

        Args:
            aggr (ParsedValue): Parsed aggregation to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the aggregation appears.
                Does not affect validation logic for static queries.

        Returns:
            out (None):
        """
        self.validate_stat_aggregation(aggr, ptable_name)
