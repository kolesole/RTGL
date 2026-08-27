"""Base validator module for RTGL query validation."""

from abc import ABC, abstractmethod
from enum import Enum, StrEnum, auto

from rtgl.base import DatabaseExplorer, Database, Table
from rtgl.base.path_builder import Path, PathBuilder
from rtgl.validator.diagnostics import IssueCollector
from rtgl.visitor import ParsedValue

# aggregation types that can be used with numeric conditions
AGGR_NUM_COND = {"avg", "count", "count_distinct", "first", "last", "max", "min", "sum"}

# aggregation types that can be used with string conditions
AGGR_STR_COND = {"first", "last"}

# aggregation types that can be used with NULL checks conditions
AGGR_NULL_COND = AGGR_NUM_COND | {"list_distinct"}


class AggrContext(Enum):
    r"""Context indicating where an aggregation appears in the query.

    Used for context-specific validation rules (e.g., temporal ranges
    must be non-negative in PREDICT but non-positive in ASSUMING).
    """

    FROM_PREDICT = auto()
    FROM_WHERE = auto()
    FROM_ASSUMING = auto()


class IdDotIdContext(StrEnum):
    r"""Context indicating where a table.column reference appears.

    Provides descriptive strings for error messages when validating
    table.column references in different parts of the query.
    """

    FROM_FOR_EACH = "FOR EACH clause"
    FROM_PREDICT = "PREDICT clause"
    FROM_COND = "condition"
    FROM_STAT_AGGR = "static aggregation"
    FROM_TMP_AGGR = "temporal aggregation"


class Validator(ABC):
    r"""Base abstract validator for RTGL queries.

    Provides common validation logic for both static and temporal queries.
    """

    def __init__(self, collector: IssueCollector, db_explorer: DatabaseExplorer, path_builder: PathBuilder) -> None:
        r"""Initialize the validator with an error collector, database explorer, and path builder.

        Args:
            collector (IssueCollector): *`IssueCollector`* to accumulate validation errors.
            db_explorer (DatabaseExplorer): *`DatabaseExplorer`* used to resolve table/column
                names and look up CTE/SQL-injection relations.
            path_builder (PathBuilder): *`PathBuilder`* used to resolve joins and CPEs.

        Returns:
            out (None):
        """
        self.collector = collector
        self.db_explorer = db_explorer
        self.path_builder = path_builder

    @abstractmethod
    def validate(self, query_dict: dict) -> None:
        r"""Top-level validation entry point.

        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def validate_query(self, query: ParsedValue) -> None:
        r"""Validate the entire query structure.

        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def validate_aggregation(self, aggr: ParsedValue, ptable_name: str, context: AggrContext) -> None:
        r"""Validate an aggregation expression.

        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass

    def validate_id_dot_id(
        self, table_token: ParsedValue, column_token: ParsedValue, ptable_name: str, context: IdDotIdContext
    ) -> None:
        r"""Validate a table.column reference.

        Check that the table exists, is connected to the parent table, and that the column
        exists in that table. Identical for static and temporal queries.

        Args:
            table_token (ParsedValue): Parsed table name.
            column_token (ParsedValue): Parsed column name.
            ptable_name (str): Name of the parent table.
            context (IdDotIdContext): Context where this reference appears.

        Returns:
            out (None):
        """
        table_name = table_token.value

        # check table existence
        if not (orig_name := self.path_builder.find_orig_src_table(table_name)) and not self.db_explorer.find_table(table_name):
            self.collector.add_error(
                line=table_token.line,
                column=table_token.column,
                msg=f"Table/Path '{table_name}' in {context} does not exist"
            )

        # check table relationship with parent
        if context == IdDotIdContext.FROM_TMP_AGGR:
            if not self._has_conn_with_parent_table(table_token.value, ptable_name, only_temporal=True):
                self.collector.add_error(
                    line=table_token.line,
                    column=table_token.column,
                    msg=(
                        f"Table '{orig_name}' in temporal aggregation has no time column, and neither does "
                        f"any table on its path to parent table '{ptable_name}' (other than the parent table "
                        "itself); a temporal aggregation requires a time-aware table to apply its time window to"
                    )
                )
        elif not self._has_conn_with_parent_table(table_name, ptable_name):
            self.collector.add_error(
                line=table_token.line,
                column=table_token.column,
                msg=(
                    f"Table '{orig_name}' in {context} is not connected (path does not exist) "
                    f"to parent table '{ptable_name}'"
                )
            )

        column_name = column_token.value

        # check column existence
        if not self.db_explorer.find_column(orig_name, column_name):
            self.collector.add_error(
                line=column_token.line,
                column=column_token.column,
                msg=f"Column '{column_name}' in {context} does not exist in table '{orig_name}'"
            )

        # FOR EACH requires a primary key column
        if context == IdDotIdContext.FROM_FOR_EACH:
            if orig_name != table_name:
                self.collector.add_error(
                    line=table_token.line,
                    column=table_token.column,
                    msg=f"Path '{table_name}' cannot be used in {context}; a direct table reference is required"
                )

            if not (pkey := self.db_explorer.find_pkey(orig_name)):
                self.collector.add_error(
                    line=column_token.line,
                    column=column_token.column,
                    msg=f"Table '{orig_name}' in {context} does not have a primary key column, which is required"
                )

            if pkey and column_name != "*" and pkey != column_name:
                self.collector.add_error(
                    line=column_token.line,
                    column=column_token.column,
                    msg=f"Column '{column_name}' in {context} is not a primary key column of table '{orig_name}'"
                )

    def validate_predefined_paths(self, predefined_paths: dict) -> None:
        r"""Validate Common Path Expressions (CPEs) declared in a `WITH ... AS (...)` clause.

        Args:
            predefined_paths (dict): Mapping of CPE alias (*`ParsedValue`*) to its declared
                hops, as parsed from the query.

        Returns:
            out (None):
        """
        for path_alias, _ in predefined_paths.items():
            if not self.path_builder.is_path_correct(path_alias.value):
                self.collector.add_error(
                    line=path_alias.line,
                    column=path_alias.column,
                    msg=f"Predefined path '{path_alias.value}' is invalid or does not exist"
                )

    def validate_injections(self, injections: dict) -> None:
        r"""Validate the declared keys of SQL injections used in the query.

        Checks that every table an injection's foreign keys reference actually exists, that a
        primary key is specified whenever other tables declare a foreign key into the
        injection, and that those referencing columns exist.

        Args:
            injections (dict): List of parsed SQL-injection tuples, as collected by the visitor.

        Returns:
            out (None):
        """
        for injection in injections:
            name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col = injection[1:5]

            for fkey_col, pkey_table in fkey_col_to_pkey_table.items():
                if not self.db_explorer.find_table(pkey_table.value):
                    self.collector.add_error(
                        line=pkey_table.line,
                        column=pkey_table.column,
                        msg=(
                            f"Foreign key column '{fkey_col.value}' of SQL-injection '{name.value}' references "
                            f"non-existent table '{pkey_table.value}'"
                        )
                    )

            if not pkey_col and fkey_table_to_fkey_col:
                self.collector.add_error(
                    line=name.line,
                    column=name.column,
                    msg=(
                        f"SQL-injection '{name.value}' is referenced by foreign keys from other tables but "
                        "has no primary key column specified"
                    )
                )

            for fkey_table, fkey_col in fkey_table_to_fkey_col.items():
                if not self.db_explorer.find_table(fkey_table.value):
                    self.collector.add_error(
                        line=fkey_table.line,
                        column=fkey_table.column,
                        msg=(
                            f"Table '{fkey_table.value}' declared as referencing SQL-injection "
                            f"'{name.value}' does not exist"
                        )
                    )

                if not self.db_explorer.find_column(fkey_table.value, fkey_col.value):
                    self.collector.add_error(
                        line=fkey_col.line,
                        column=fkey_col.column,
                        msg=(
                            f"Column '{fkey_col.value}' declared as referencing SQL-injection '{name.value}' "
                            f"does not exist in table '{fkey_table.value}'"
                        )
                    )

    def validate_for_each(self, for_each: ParsedValue) -> str | None:
        r"""Validate the FOR EACH clause and return the parent table name.

        Args:
            for_each (ParsedValue): Parsed FOR EACH clause.

        Returns:
            table_name (str): Name of the parent table, or None if FOR EACH is not present.
        """
        if for_each is None:
            return None

        for_each_dict = for_each.value

        # if table or column tokens are not presented -> exit from for each validation
        # otherwise -> validate table.column and WHERE clause
        table_name = None
        if (table_token := for_each_dict["Table"]) and (column_token := for_each_dict["Column"]):
            table_name = table_token.value
            # validate that the table.column reference is valid
            self.validate_id_dot_id(table_token, column_token, table_name, IdDotIdContext.FROM_FOR_EACH)
            # validate WHERE clause
            self.validate_where(for_each_dict["Where"], table_name)

        return table_name

    def validate_predict(self, predict: ParsedValue, ptable_name: str, stat: bool = False) -> None:
        r"""Validate PREDICT clause.

        Args:
            predict (ParsedValue): Parsed PREDICT clause.
            ptable_name (str): Name of the parent table.
            stat (bool): Whether any aggregation conditions in this PREDICT are static
                aggregations (e.g. inside a `where_stat`, which never embeds a temporal
                aggregation regardless of whether the outer query is static or temporal).
                Default=False.

        Returns:
            out (None):
        """
        if predict is None:
            return

        predict_dict = predict.value

        match predict_dict["PredType"]:
            case "aggregation":
                aggr = predict_dict["Aggregation"]
                self.validate_aggregation(aggr, ptable_name, AggrContext.FROM_PREDICT)

                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value.lower()

                # LIST_DISTINCT is the only aggregation that supports CLASSIFY and RANK_TOP
                if aggr_type != "list_distinct":
                    if classify_token := predict_dict["Classify"]:
                        self.collector.add_error(
                            line=classify_token.line,
                            column=classify_token.column,
                            msg=(
                                "CLASSIFY modifier is only allowed with LIST_DISTINCT aggregation, "
                                f"found with {aggr_type}"
                            )
                        )

                    if rank_top_token := predict_dict["RankTop"]:
                        self.collector.add_error(
                            line=rank_top_token.line,
                            column=rank_top_token.column,
                            msg=(
                                "RANK_TOP K modifier is only allowed with LIST_DISTINCT aggregation, "
                                f"found with {aggr_type}"
                            )
                        )

                # Validate K parameter if RANK_TOP is present
                if k_token := predict_dict["K"]:
                    k = int(k_token.value)
                    if k <= 0:
                        self.collector.add_error(
                            line=k_token.line,
                            column=k_token.column,
                            msg=f"K in RANK_TOP K must be a positive integer, found {k}"
                        )
            case "expr":
                # validate boolean expression in PREDICT
                self.validate_expr(predict_dict["Expr"], ptable_name, AggrContext.FROM_PREDICT, stat)
            case "id_dot_id":
                # static queries can predict table.column directly
                table_token = predict_dict["Table"]
                column_token = predict_dict["Column"]
                # validate table.column reference
                self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_PREDICT)
            case _:
                pass

    def validate_where(self, where: ParsedValue, ptable_name: str, stat: bool = False) -> None:
        r"""Validate WHERE clause.

        Delegates to `validate_expr` with `AggrContext.FROM_WHERE`.

        Args:
            where (ParsedValue): Parsed WHERE clause.
            ptable_name (str): Name of the parent table.
            stat (bool): Whether any aggregation conditions in this WHERE are static
                aggregations (e.g. inside a `where_stat`, which never embeds a temporal
                aggregation regardless of whether the outer query is static or temporal).
                Default=False.

        Returns:
            out (None):
        """
        if where is None:
            return

        where_dict = where.value

        self.validate_expr(where_dict["Expr"], ptable_name, AggrContext.FROM_WHERE, stat)

    def validate_expr(
        self, expr: ParsedValue | dict, ptable_name: str, context: AggrContext, stat: bool = False
    ) -> None:
        r"""Validate a boolean expression (recursively handles AND/OR).

        Args:
            expr (ParsedValue | dict): Parsed expression to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the expression appears.
            stat (bool): Whether any aggregation conditions in this expression are static
                aggregations (e.g. inside a `where_stat`, which never embeds a temporal
                aggregation regardless of whether the outer query is static or temporal).
                Default=False.

        Returns:
            out (None):
        """
        if expr is None:
            return

        # unwrap ParsedValue if necessary
        expr_dict = expr.value if isinstance(expr, ParsedValue) else expr

        # if expression has an operator (AND/OR), recursively validate both sides
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            self.validate_expr(expr_dict["LeftExpr"], ptable_name, context, stat)
            self.validate_expr(expr_dict["RightExpr"], ptable_name, context, stat)
        else:
            # base case: validate a single condition
            if isinstance(expr_dict, dict):
                self.validate_condition(expr, ptable_name, context, stat)
            else:
                self.validate_condition(expr_dict, ptable_name, context, stat)

    def validate_condition(
        self, condition: ParsedValue, ptable_name: str, context: AggrContext, stat: bool = False
    ) -> None:
        r"""Validate a single condition.

        Ensure that aggregation types are compatible with the comparison operators.

        Args:
            condition (ParsedValue): Parsed condition to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the condition appears.
            stat (bool): Whether an aggregation in this condition is a static aggregation
                (e.g. inside a `where_stat`, which never embeds a temporal aggregation
                regardless of whether the outer query is static or temporal).
                Default=False.

        Returns:
            out (None):
        """
        if condition is None:
            return

        cond_dict = condition.value

        match cond_dict["CondType"]:
            case "aggregation":
                # validate the aggregation and its components
                aggr = cond_dict["Aggregation"]
                if stat:
                    self.validate_stat_aggregation(aggr, ptable_name)
                else:
                    self.validate_aggregation(aggr, ptable_name, context)
                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value.lower()

                # Validate that the aggregation type is compatible with the condition type
                match cond_dict["CType"]:
                    case "num":
                        if aggr_type not in AGGR_NUM_COND:
                            self.collector.add_error(
                                line=condition.line,
                                column=condition.column,
                                msg=f"Aggregation type '{aggr_type}' cannot be used in numeric condition"
                            )
                    case "str":
                        if aggr_type not in AGGR_STR_COND:
                            self.collector.add_error(
                                line=condition.line,
                                column=condition.column,
                                msg=f"Aggregation type '{aggr_type}' cannot be used in string condition"
                            )
                    case "null":
                        if aggr_type not in AGGR_NULL_COND:
                            self.collector.add_error(
                                line=condition.line,
                                column=condition.column,
                                msg=f"Aggregation type '{aggr_type}' cannot be used in NULL condition"
                            )
                    case _:
                        pass
            case "id_dot_id":
                table_token = cond_dict["Table"]
                column_token = cond_dict["Column"]
                # validate table.column reference
                self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_COND)
            case _:
                pass

    def validate_stat_aggregation(self, aggr: ParsedValue, ptable_name: str) -> None:
        r"""Validate a static aggregation.

        Args:
            aggr (ParsedValue): Parsed aggregation to validate.
            ptable_name (str): Name of the parent table.

        Returns:
            out (None):
        """
        if aggr is None:
            return

        aggr_dict = aggr.value

        table_token = aggr_dict["Table"]
        column_token = aggr_dict["Column"]

        # validate WHERE clause inside the aggregation if present
        if where := aggr_dict["Where"]:
            if not self.db_explorer.find_pkey(table_token.value) and not where.value["IsSimple"]:
                self.collector.add_error(
                    line=table_token.line,
                    column=table_token.column,
                    msg=(
                        f"Table '{table_token.value}' in static aggregation does not have a primary key column, "
                        "which is required for non-simple WHERE filtering (when the WHERE clause references "
                        "tables other than the aggregation's own table)"
                    )
                )
            self.validate_where(where, table_token.value, stat=True)

        # validate table.column in the aggregation
        self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_STAT_AGGR)

    ################## Helper methods ##################

    def _format_path(self, table_name: str, path: Path) -> str:
        r"""Render a join path as a human-readable `table.key -> table.key -> ...` chain.

        Args:
            table_name (str): Name of the table the path starts from.
            path (Path): Join path, as returned by `PathBuilder.build_paths`.

        Returns:
            out (str): The path rendered with each hop's join column attached to whichever
                table owns it (e.g. `orders.user_id -> users`). A table sitting between two
                hops that each contribute a different key shows both, e.g. `reviews.product_id/user_id`.
        """
        tables = [table_name] + [table for _, table, _ in path]
        keys = [[] for _ in tables]

        for i, (fk, _, edge_type) in enumerate(path):
            if edge_type == "f":
                left_key = fk
                right_key = self.db_explorer.find_pkey(tables[i+1])
            else:
                left_key = self.db_explorer.find_pkey(tables[i])
                right_key = fk

            if left_key and left_key not in keys[i]:
                keys[i].append(left_key)

            if right_key and right_key not in keys[i+1]:
                keys[i+1].append(right_key)

        labels = [f"{table}.{':'.join(fks)}" if fks else table for table, fks in zip(tables, keys)]

        return " -> ".join(labels)

    def _has_conn_with_parent_table(self, table_name: str, ptable_name: str, only_temporal: bool=False) -> bool:
        r"""Check if a table is connected to the parent table via foreign key (case-insensitive).

        Args:
            table_name (str): Name of the child table to check.
            ptable_name (str): Name of the parent table.
            only_temporal (bool): If True, only consider paths that pass through at least one
                table with a time column (see `PathBuilder.build_paths`). Default=False.

        Returns:
            bool: True if the table is the parent itself or has a foreign key
                referencing it, False otherwise.
        """
        if table_name == ptable_name:
            return True

        paths = self.path_builder.build_paths(table_name, ptable_name, only_temporal)
        kind = "temporal " if only_temporal else ""

        if len(paths) == 0:
            return False
        elif len(paths) == 1:
            # an invalid predefined path resolves to an empty hop list -> not connected
            return bool(paths[0]) and paths[0][-1][1] == ptable_name
        else:
            # build_paths stops after finding two paths, so paths[0] is always the shortest;
            # if paths[1] has the same length, the shortest path itself is ambiguous (error),
            # otherwise it is just a longer alternative and paths[0] can be used unambiguously
            if len(paths[0]) == len(paths[1]):
                self.collector.add_error(
                    line=None,
                    column=None,
                    msg=(
                        f"Multiple {kind}paths, with the shortest length, exist between table '{table_name}' "
                        f"and parent table '{ptable_name}', which is ambiguous"
                    )
                )
            else:
                self.collector.add_warning(
                    msg=(
                        f"Table '{table_name}' has multiple {kind}paths to parent table "
                        f"'{ptable_name}'. Using the shortest one: {self._format_path(table_name, paths[0])}"
                    )
                )
            return True
