"""Visitor implementation for traversing RTGL parse trees."""

from typing import override

from antlr4 import ParserRuleContext, TerminalNode

from rtgl.parser import ParserRTGL, ParserRTGLVisitor
from rtgl.visitor.parsed_value import ParsedValue


class Visitor(ParserRTGLVisitor):
    r"""*`Visitor`* class for converting RTGL parse trees to dictionaries.

    Implements the visitor pattern to traverse ANTLR-generated parse trees
    and convert them into structured Python dictionaries. Each visit method
    corresponds to a grammar rule and extracts relevant information while
    preserving source location data for error reporting.

    The visitor wraps parsed values in *`ParsedValue`* objects that track
    their line and column positions in the source query.
    """

    def __init__(self):
        r"""Initialize the visitor with empty SQL-injection and CPE collections.

        Returns:
            out (None):
        """
        super().__init__()
        self.injections = []
        self.predefined_paths = {}

    @override
    def visitQuery(self, ctx: ParserRTGL.QueryContext) -> dict:
        r"""Visit the top-level query rule.

        Extract both temporal and static query components (only one will be non-None).

        Args:
            ctx (ParserRTGL.QueryContext): Parse tree context.

        Returns:
            query_dict (dict): Dictionary with 'QueryTmp' and 'QueryStat' keys.
        """
        query_dict = {
            "QueryTmp": self._rule2value(ctx.query_tmp()),
            "QueryStat": self._rule2value(ctx.query_stat())
        }

        query_dict.update({
            "Injections": self.injections,
            "PredefinedPaths": self.predefined_paths
        })

        self.injections = []  # reset injections for next query
        self.predefined_paths = {}  # reset predefined paths for next query

        return query_dict

    @override
    def visitQuery_tmp(self, ctx: ParserRTGL.Query_tmpContext) -> dict:
        r"""Visit a temporal query rule.

        Args:
            ctx (ParserRTGL.Query_tmpContext): Parse tree context.

        Returns:
            query_dict (dict): Dictionary with temporal query components.
        """
        self._rule2value(ctx.common_path_exprs())

        for_each = self._rule2value(ctx.for_each_tmp())
        parent_table = for_each.value["Table"].value

        where = self._rule2value(ctx.where_tmp())
        if where:
            where.value["IsSimple"] = self._is_where_simple(where, parent_table)

        query_dict = {
            "Predict": self._rule2value(ctx.predict_tmp()),
            "ForEach": for_each,
            "Where": where,
            "Assuming": self._rule2value(ctx.assuming())
        }

        return query_dict

    @override
    def visitQuery_stat(self, ctx: ParserRTGL.Query_statContext) -> dict:
        r"""Visit a static query rule.

        Args:
            ctx (ParserRTGL.Query_statContext): Parse tree context.

        Returns:
            query_dict (dict): Dictionary with static query components.
        """
        self._rule2value(ctx.common_path_exprs())

        for_each = self._rule2value(ctx.for_each_stat())
        parent_table = for_each.value["Table"].value

        where = self._rule2value(ctx.where_stat())
        if where:
            where.value["IsSimple"] = self._is_where_simple(where, parent_table)

        query_dict = {
            "Predict": self._rule2value(ctx.predict_stat()),
            "ForEach": for_each,
            "Where": where
        }

        return query_dict

    @override
    def visitCommon_path_exprs(self, ctx:ParserRTGL.Common_path_exprsContext) -> None:
        r"""Visit the `WITH ... AS (...)` clause and visit each declared CPE in turn.

        Args:
            ctx (ParserRTGL.Common_path_exprsContext): Parse tree context.

        Returns:
            out (None): The CPEs are stored in `self.predefined_paths`.
        """
        for common_path_expr in ctx.common_path_expr():
            self._rule2value(common_path_expr)

    @override
    def visitCommon_path_expr(self, ctx:ParserRTGL.Common_path_exprContext) -> None:
        r"""Visit a single Common Path Expression and register it under its alias.

        Args:
            ctx (ParserRTGL.Common_path_exprContext): Parse tree context.

        Returns:
            out (None): The CPE is stored in `self.predefined_paths`.
        """
        path = [self._rule2value(path_node, unwrap=True) for path_node in ctx.steps]
        self.predefined_paths[self._node2value(ctx.path_name)] = path

    @override
    def visitFor_each_tmp(self, ctx: ParserRTGL.For_each_tmpContext) -> dict:
        r"""Visit temporal FOR EACH clause.

        Args:
            ctx (ParserRTGL.For_each_tmpContext): Parse tree context.

        Returns:
            for_each_dict (dict): Dictionary with FOR EACH components.
        """
        table = self._rule2value(ctx.table_tmp(), unwrap=True)

        where = self._rule2value(ctx.where_stat())
        if where:
            where.value["IsSimple"] = self._is_where_simple(where, table.value)

        for_each_dict = {
            "Table": table,
            "Column": self._rule2value(ctx.column(), unwrap=True),
            "Where": where
        }

        return for_each_dict

    @override
    def visitFor_each_stat(self, ctx: ParserRTGL.For_each_statContext) -> dict:
        r"""Visit static FOR EACH clause.

        Args:
            ctx (ParserRTGL.For_each_statContext): Parse tree context.

        Returns:
            for_each_dict (dict): Dictionary with FOR EACH components.
        """
        table = self._rule2value(ctx.table_stat(), unwrap=True)

        where = self._rule2value(ctx.where_stat())
        if where:
            where.value["IsSimple"] = self._is_where_simple(where, table.value)

        for_each_dict = {
            "Table": table,
            "Column": self._rule2value(ctx.column(), unwrap=True),
            "Where": where
        }

        return for_each_dict

    @override
    def visitPredict_tmp(self, ctx: ParserRTGL.Predict_tmpContext) -> dict:
        r"""Visit temporal PREDICT clause.

        Args:
            ctx (ParserRTGL.Predict_tmpContext): Parse tree context.

        Returns:
            predict_dict (dict): Dictionary with temporal PREDICT components.
        """
        if ctx.aggregation_tmp():
            pred_type = "aggregation"
        elif ctx.expr_or_tmp():
            pred_type = "expr"

        predict_dict = {
            "PredType": pred_type,
            "Aggregation": self._rule2value(ctx.aggregation_tmp()),
            "Expr": self._rule2value(ctx.expr_or_tmp()),
            "RankTop": self._node2value(ctx.RANK_TOP()),
            "K": self._node2value(ctx.INT()),
            "Classify": self._node2value(ctx.CLASSIFY()),
        }

        return predict_dict

    @override
    def visitPredict_stat(self, ctx: ParserRTGL.Predict_statContext) -> dict:
        r"""Visit static PREDICT clause.

        Args:
            ctx (ParserRTGL.Predict_statContext): Parse tree context.

        Returns:
            predict_dict (dict): Dictionary with static PREDICT components.
        """
        if ctx.aggregation_stat():
            pred_type = "aggregation"
        elif ctx.expr_or_stat():
            pred_type = "expr"
        else:
            pred_type = "id_dot_id"

        predict_dict = {
            "PredType": pred_type,
            "Aggregation": self._rule2value(ctx.aggregation_stat()),
            "Expr": self._rule2value(ctx.expr_or_stat()),
            "Table": self._rule2value(ctx.table_stat(), unwrap=True),
            "Column": self._rule2value(ctx.column(), unwrap=True),
            "RankTop": self._node2value(ctx.RANK_TOP()),
            "K": self._node2value(ctx.INT()),
            "Classify": self._node2value(ctx.CLASSIFY()),
        }

        return predict_dict

    @override
    def visitWhere_tmp(self, ctx: ParserRTGL.Where_tmpContext) -> dict:
        r"""Visit temporal WHERE clause.

        Args:
            ctx (ctx:ParserRTGL.Where_tmpContext): Parse tree context.

        Returns:
            where_dict (dict): Dictionary with temporal WHERE components.
        """
        where_dict = {
            "Expr": self._rule2value(ctx.expr_or_tmp())
        }

        return where_dict

    @override
    def visitWhere_stat(self, ctx: ParserRTGL.Where_statContext) -> dict:
        r"""Visit static WHERE clause.

        Args:
            ctx (ctx:ParserRTGL.Where_statContext): Parse tree context.

        Returns:
            where_dict (dict): Dictionary with static WHERE components.
        """
        where_dict = {
            "Expr": self._rule2value(ctx.expr_or_stat()),
        }

        return where_dict

    @override
    def visitAssuming(self, ctx: ParserRTGL.AssumingContext) -> dict:
        r"""Visit ASSUMING clause.

        Args:
            ctx (ctx:ParserRTGL.AssumingContext): Parse tree context.

        Returns:
            assuming_dict (dict): Dictionary with ASSUMING components.
        """
        assuming_dict = {
            "Expr": self._rule2value(ctx.expr_or_tmp())
        }

        return assuming_dict

    @override
    def visitExpr_or_tmp(self, ctx: ParserRTGL.Expr_or_tmpContext) -> dict | ParsedValue:
        r"""Visit a temporal OR expression.

        Build a left-associative tree of OR operations.
        For single expressions, returns the expression directly.
        For multiple OR expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_or_tmpContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_and_tmp()) == 1:
            return self._rule2value(ctx.expr_and_tmp(0), unwrap=True)

        # build left-associative OR tree
        expr_dict = self._rule2value(ctx.expr_and_tmp(0), unwrap=True)
        for i in range(1, len(ctx.expr_and_tmp())):
            expr_dict = {
                "Op": self._node2value(ctx.OR(i - 1)),
                "LeftExpr": expr_dict,
                "RightExpr": self._rule2value(ctx.expr_and_tmp(i), unwrap=True)
            }

        return expr_dict

    @override
    def visitExpr_or_stat(self, ctx: ParserRTGL.Expr_or_statContext) -> dict | ParsedValue:
        r"""Visit a static OR expression.

        Build a left-associative tree of OR operations.
        For single expressions, returns the expression directly.
        For multiple OR expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_or_statContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_and_stat()) == 1:
            return self._rule2value(ctx.expr_and_stat(0), unwrap=True)

        # build left-associative OR tree
        expr_dict = self._rule2value(ctx.expr_and_stat(0), unwrap=True)
        for i in range(1, len(ctx.expr_and_stat())):
            expr_dict = {
                "Op": self._node2value(ctx.OR(i - 1)),
                "LeftExpr": expr_dict,
                "RightExpr": self._rule2value(ctx.expr_and_stat(i), unwrap=True)
            }

        return expr_dict

    @override
    def visitExpr_and_tmp(self, ctx: ParserRTGL.Expr_and_tmpContext) -> dict | ParsedValue:
        r"""Visit a temporal AND expression.

        Build a left-associative tree of AND operations.
        For single expressions, returns the expression directly.
        For multiple AND expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_and_tmpContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_term_tmp()) == 1:
            return self._rule2value(ctx.expr_term_tmp(0), unwrap=True)

        # build left-associative AND tree
        expr_dict = self._rule2value(ctx.expr_term_tmp(0), unwrap=True)
        for i in range(1, len(ctx.expr_term_tmp())):
            expr_dict = {
                "Op": self._node2value(ctx.AND(i - 1)),
                "LeftExpr": expr_dict,
                "RightExpr": self._rule2value(ctx.expr_term_tmp(i), unwrap=True)
            }

        return expr_dict

    @override
    def visitExpr_and_stat(self, ctx: ParserRTGL.Expr_and_statContext) -> dict | ParsedValue:
        r"""Visit a static AND expression.

        Build a left-associative tree of AND operations.
        For single expressions, returns the expression directly.
        For multiple AND expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_and_statContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_term_stat()) == 1:
            return self._rule2value(ctx.expr_term_stat(0), unwrap=True)

        # build left-associative AND tree
        expr_dict = self._rule2value(ctx.expr_term_stat(0), unwrap=True)
        for i in range(1, len(ctx.expr_term_stat())):
            expr_dict = {
                "Op": self._node2value(ctx.AND(i - 1)),
                "LeftExpr": expr_dict,
                "RightExpr": self._rule2value(ctx.expr_term_stat(i), unwrap=True)
            }

        return expr_dict

    @override
    def visitExpr_term_tmp(self, ctx: ParserRTGL.Expr_term_tmpContext) -> dict | ParsedValue:
        r"""Visit a temporal term expression (base case or parenthesized expr).

        Args:
            ctx (ParserRTGL.Expr_term_tmpContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        if ctx.condition_tmp():
            return self._rule2value(ctx.condition_tmp())
        elif ctx.expr_or_tmp():
            return self._rule2value(ctx.expr_or_tmp(), unwrap=True)

    @override
    def visitExpr_term_stat(self, ctx: ParserRTGL.Expr_term_statContext) -> dict | ParsedValue:
        r"""Visit a static term expression (base case or parenthesized expr).

        Args:
            ctx (ParserRTGL.Expr_term_statContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        if ctx.condition_stat():
            return self._rule2value(ctx.condition_stat())
        elif ctx.expr_or_stat():
            return self._rule2value(ctx.expr_or_stat(), unwrap=True)

    @override
    def visitCondition_tmp(self, ctx: ParserRTGL.Condition_tmpContext) -> dict:
        r"""Visit a temporal condition.

        Args:
            ctx (ParserRTGL.Condition_tmpContext): Parse tree context.

        Returns:
            condition_dict (dict): Dictionary with temporal condition components.
        """
        if ctx.num_condition():
            cond_dict = self._rule2value(ctx.num_condition(), unwrap=True)
        elif ctx.str_condition():
            cond_dict = self._rule2value(ctx.str_condition(), unwrap=True)
        elif ctx.null_check_condition():
            cond_dict = self._rule2value(ctx.null_check_condition(), unwrap=True)

        cond_dict.update({
            "CondType": "aggregation",
            "NOT": self._node2value(ctx.NOT()),
            "Aggregation": self._rule2value(ctx.aggregation_tmp())
        })

        return cond_dict

    @override
    def visitCondition_stat(self, ctx: ParserRTGL.Condition_statContext) -> dict:
        r"""Visit a static condition.

        Args:
            ctx (ParserRTGL.Condition_statContext): Parse tree context.

        Returns:
            condition_dict (dict): Dictionary with static condition components.
        """
        cond_type = "aggregation" if ctx.aggregation_stat() else "id_dot_id"

        if ctx.num_condition():
            cond_dict = self._rule2value(ctx.num_condition(), unwrap=True)
        elif ctx.str_condition():
            cond_dict = self._rule2value(ctx.str_condition(), unwrap=True)
        elif ctx.null_check_condition():
            cond_dict = self._rule2value(ctx.null_check_condition(), unwrap=True)

        cond_dict.update({
            "CondType": cond_type,
            "NOT": self._node2value(ctx.NOT()),
            "Aggregation": self._rule2value(ctx.aggregation_stat()),
            "Table": self._rule2value(ctx.table_stat(), unwrap=True),
            "Column": self._rule2value(ctx.column(), unwrap=True)
        })

        return cond_dict

    @override
    def visitNum_condition(self, ctx: ParserRTGL.Num_conditionContext) -> dict:
        r"""Visit a numerical condition.

        Args:
            ctx (ParserRTGL.Num_conditionContext): Parse tree context.

        Returns:
            num_cond_dict (dict): Dictionary with numerical condition components.
        """
        if ctx.DATETIME():
            n = self._node2value(ctx.DATETIME())
        elif ctx.FLOAT():
            n = self._node2value(ctx.FLOAT())
        elif ctx.INT():
            n = self._node2value(ctx.INT())

        num_cond_dict = {
            "CType": "num",
            "CompOp": self._node2value(ctx.NUM_COMP_OP()),
            "N": n
        }

        return num_cond_dict

    @override
    def visitStr_condition(self, ctx: ParserRTGL.Str_conditionContext) -> dict:
        r"""Visit a string condition.

        Args:
            ctx (ParserRTGL.Str_conditionContext): Parse tree context.

        Returns:
            str_cond_dict (dict): Dictionary with string condition components.
        """
        str_cond_dict = {
            "CType": "str",
            "CompOp": self._node2value(ctx.STR_COMP_OP()),
            "String": self._node2value(ctx.STRING(), preserve_case=True)
        }

        return str_cond_dict

    @override
    def visitNull_check_condition(self, ctx: ParserRTGL.Null_check_conditionContext) -> dict:
        r"""Visit a null check condition.

        Args:
            ctx (ParserRTGL.Null_check_conditionContext): Parse tree context.

        Returns:
            null_cond_dict (dict): Dictionary with null check condition components.
        """
        null_cond_dict = {
            "CType": "null",
            "CheckOp": self._node2value(ctx.NULL_CHECK_OP())
        }

        return null_cond_dict

    @override
    def visitAggregation_tmp(self, ctx: ParserRTGL.Aggregation_tmpContext) -> dict:
        r"""Visit a temporal aggregation.

        Args:
            ctx (ParserRTGL.Aggregation_tmpContext): Parse tree context.

        Returns:
            aggr_dict (dict): Dictionary with temporal aggregation components.
        """
        table = self._rule2value(ctx.table_tmp(), unwrap=True)

        where = self._rule2value(ctx.where_stat())
        if where:
            where.value["IsSimple"] = self._is_where_simple(where, table.value)

        aggr_dict = {
            "AggrType": self._node2value(ctx.AGGR_FUNC()),
            "Table": table,
            "Column": self._rule2value(ctx.column(), unwrap=True),
            "Where": where,
            "Start": self._node2value(ctx.start),
            "End": self._node2value(ctx.end),
            "MeasureUnit": self._node2value(ctx.TIME_MEASURE_UNIT())
        }

        return aggr_dict

    @override
    def visitAggregation_stat(self, ctx: ParserRTGL.Aggregation_statContext) -> dict:
        r"""Visit a stat aggregation.

        Args:
            ctx (ParserRTGL.Aggregation_statContext): Parse tree context.

        Returns:
            aggr_dict (dict): Dictionary with static aggregation components.
        """
        table = self._rule2value(ctx.table_stat(), unwrap=True)

        where = self._rule2value(ctx.where_stat())
        if where:
            where.value["IsSimple"] = self._is_where_simple(where, table.value)

        aggr_dict = {
            "AggrType": self._node2value(ctx.AGGR_FUNC()),
            "Table": table,
            "Column": self._rule2value(ctx.column(), unwrap=True),
            "Where": where
        }

        return aggr_dict

    @override
    def visitSql_injection_tmp(self, ctx: ParserRTGL.Sql_injection_tmpContext) -> ParsedValue:
        r"""Visit a temporal SQL injection.

        Create a ParsedValue for the SQL injection and store its components.

        Args:
            ctx (ParserRTGL.Sql_injection_tmpContext): Parse tree context.

        Returns:
            name (str): Name of the SQL injection.
        """
        body = ctx.SQL_INJECTION_BODY().getSymbol().text[1:-1]
        name = self._node2value(ctx.table)
        pkey_col = self._node2value(ctx.pkey_col, unwrap=True)
        time_col = self._node2value(ctx.time_col, unwrap=True)

        fkey_col_to_pkey_table = {}
        for fkey_ctx in ctx.fkey_col_to_pkey_table():
            fkey_col, pkey_table = self._rule2value(fkey_ctx, unwrap=True)
            fkey_col_to_pkey_table[fkey_col] = pkey_table

        fkey_table_to_fkey_col = {}
        for fkey_ctx in ctx.fkey_table_to_fkey_col():
            fkey_table, fkey_col = self._rule2value(fkey_ctx, unwrap=True)
            fkey_table_to_fkey_col[fkey_table] = fkey_col

        self.injections.append(
            (body, name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col, time_col)
        )

        return name

    @override
    def visitSql_injection_stat(self, ctx: ParserRTGL.Sql_injection_statContext) -> ParsedValue:
        r"""Visit a static SQL injection.

        Create a ParsedValue for the SQL injection and store its components.

        Args:
            ctx (ParserRTGL.Sql_injection_statContext): Parse tree context.

        Returns:
            name (str): Name of the SQL injection.
        """
        body = ctx.SQL_INJECTION_BODY().getSymbol().text[1:-1]
        name = self._node2value(ctx.table)
        pkey_col = self._node2value(ctx.pkey_col, unwrap=True)

        fkey_col_to_pkey_table = {}
        for fkey_ctx in ctx.fkey_col_to_pkey_table():
            fkey_col, pkey_table = self._rule2value(fkey_ctx, unwrap=True)
            fkey_col_to_pkey_table[fkey_col] = pkey_table

        fkey_table_to_fkey_col = {}
        for fkey_ctx in ctx.fkey_table_to_fkey_col():
            fkey_table, fkey_col = self._rule2value(fkey_ctx, unwrap=True)
            fkey_table_to_fkey_col[fkey_table] = fkey_col

        self.injections.append(
            (body, name, pkey_col, fkey_col_to_pkey_table, fkey_table_to_fkey_col)
        )

        return name

    @override
    def visitPath_node(self, ctx:ParserRTGL.Path_nodeContext) -> tuple[ParsedValue, ParsedValue, ParsedValue | None]:
        r"""Visit a single hop of a Common Path Expression.

        Args:
            ctx (ParserRTGL.Path_nodeContext): Parse tree context.

        Returns:
            out (tuple[ParsedValue, ParsedValue, ParsedValue | None]): Tuple of (table, left_key, right_key).
        """
        table = self._node2value(ctx.table, unwrap=True)
        left_key = self._node2value(ctx.left_key, unwrap=True)
        right_key = self._node2value(ctx.right_key, unwrap=True)

        return table, left_key, right_key

    @override
    def visitFkey_col_to_pkey_table(
            self,
            ctx:ParserRTGL.Fkey_col_to_pkey_tableContext
        ) -> tuple[ParsedValue, ParsedValue]:
        r"""Visit a single `fkey_col->pkey_table` entry of a SQL injection's key declarations.

        Args:
            ctx (ParserRTGL.Fkey_col_to_pkey_tableContext): Parse tree context.

        Returns:
            out (tuple[ParsedValue, ParsedValue]): Tuple of (foreign key column, parent table).
        """
        return self._node2value(ctx.fkey_col), self._node2value(ctx.pkey_table)

    @override
    def visitFkey_table_to_fkey_col(
            self,
            ctx:ParserRTGL.Fkey_table_to_fkey_colContext
        ) -> tuple[ParsedValue, ParsedValue]:
        r"""Visit a single `other_table.fkey_col` entry of a SQL injection's key declarations.

        Args:
            ctx (ParserRTGL.Fkey_table_to_fkey_colContext): Parse tree context.

        Returns:
            out (tuple[ParsedValue, ParsedValue]): Tuple of (referencing table, its foreign key column).
        """
        return self._node2value(ctx.fkey_table), self._node2value(ctx.fkey_col)

    @override
    def visitTable_tmp(self, ctx:ParserRTGL.Table_tmpContext) -> ParsedValue:
        r"""Visit a temporal table reference: either a plain table/path name or a SQL injection.

        Args:
            ctx (ParserRTGL.Table_tmpContext): Parse tree context.

        Returns:
            out (ParsedValue): The table/path name, or the SQL injection's assigned table name.
        """
        return self._node2value(ctx.ID()) if ctx.ID() else self._rule2value(ctx.sql_injection_tmp(), unwrap=True)

    @override
    def visitTable_stat(self, ctx:ParserRTGL.Table_statContext) -> ParsedValue:
        r"""Visit a static table reference: either a plain table/path name or a SQL injection.

        Args:
            ctx (ParserRTGL.Table_statContext): Parse tree context.

        Returns:
            out (ParsedValue): The table/path name, or the SQL injection's assigned table name.
        """
        return self._node2value(ctx.ID()) if ctx.ID() else self._rule2value(ctx.sql_injection_stat(), unwrap=True)

    @override
    def visitColumn(self, ctx:ParserRTGL.ColumnContext) -> ParsedValue:
        r"""Visit a column reference: either a plain column name or the `*` wildcard.

        Args:
            ctx (ParserRTGL.ColumnContext): Parse tree context.

        Returns:
            out (ParsedValue): The column name, or "*".
        """
        return self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID())

    ################## Helper methods ##################

    def _node2value(
            self,
            node: TerminalNode | None,
            unwrap: bool=False,
            preserve_case: bool=False
        ) -> ParsedValue | str | None:
        r"""Convert a terminal node (token) to *`ParsedValue`*.

        Extract the text and position information from an ANTLR terminal node.

        Args:
            node (TerminalNode | None): ANTLR terminal node, or None.
            unwrap (bool): If True, return the raw value instead of the *`ParsedValue`* wrapper.
                Default = False.
            preserve_case (bool): If True, preserve the original case of the token text.

        Returns:
            out (ParsedValue | str | None): Wrapped value with location, or the raw string if unwrap=True,
                or None if node is None.
        """
        if not node:
            return None

        token = node.getSymbol() if hasattr(node, "getSymbol") else node
        parsed_value = ParsedValue(
            value=token.text if preserve_case else token.text.lower(),
            line=token.line,
            column=token.column
        )

        return parsed_value.value if unwrap else parsed_value

    def _rule2value(self, ctx: ParserRuleContext | None, unwrap: bool=False) -> ParsedValue | None:
        r"""Convert a rule context to *`ParsedValue`*.

        Visit the rule context and wrap the result with location info.

        Args:
            ctx (ParserRuleContext | None): ANTLR rule context, or None.
            unwrap (bool): If True, return the raw visit result instead of the *`ParsedValue`*
                wrapper. Default = False.

        Returns:
            out (ParsedValue | None): Wrapped visit result with location, or the raw value if unwrap=True,
                or None if ctx is None.
        """
        if not ctx:
            return None

        parsed_value = ParsedValue(value=self.visit(ctx), line=ctx.start.line, column=ctx.start.column)

        return parsed_value.value if unwrap else parsed_value

    def _is_where_simple(self, where: ParsedValue, parent_table: str) -> bool:
        r"""Check whether a WHERE expression is simple.

        A WHERE is simple only if every leaf condition is a plain table.column
        reference to the parent table itself: aggregation conditions always need
        a subquery (even when they aggregate over the parent table), so any
        aggregation leaf makes the WHERE non-simple.

        Args:
            where (ParsedValue): Parsed WHERE clause.
            parent_table (str): Name of the table the WHERE is being evaluated against.

        Returns:
            out (bool): True if the WHERE is simple.
        """
        expr = where.value["Expr"].value

        def _is_simple(node: dict | ParsedValue) -> bool:
            if isinstance(node, dict) and "Op" in node:
                return _is_simple(node["LeftExpr"]) and _is_simple(node["RightExpr"])

            leaf = node.value
            return leaf["CondType"] == "id_dot_id" and leaf["Table"].value == parent_table

        return _is_simple(expr)
