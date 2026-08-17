"""Visitor implementation for traversing RTGL parse trees."""

from typing import override

from antlr4 import ParserRuleContext, TerminalNode

from rtgl.parser import ParserRTGL, ParserRTGLVisitor
from rtgl.visitor.parsed_value import ParsedValue


class Visitor(ParserRTGLVisitor):
    r"""Visitor class for converting RTGL parse trees to dictionaries.

    Implements the visitor pattern to traverse ANTLR-generated parse trees
    and convert them into structured Python dictionaries. Each visit method
    corresponds to a grammar rule and extracts relevant information while
    preserving source location data for error reporting.

    The visitor wraps parsed values in ParsedValue objects that track
    their line and column positions in the source query.
    """

    def __init__(self):
        super().__init__()
        self.injections = []  # store SQL injections for later use
        self.predefined_paths = {}

    @override
    def visitQuery(self, ctx: ParserRTGL.QueryContext) -> tuple[dict, list, dict]:
        r"""Visits the top-level query rule.

        Extracts both temporal and static query components (only one will be non-None).

        Args:
            ctx (ParserRTGL.QueryContext): Parse tree context.

        Returns:
            query_dict (dict): Dictionary with 'QueryTmp' and 'QueryStat' keys.
        """
        query_tmp = self._rule2value(ctx.query_tmp())
        query_stat = self._rule2value(ctx.query_stat())

        query_dict = {"QueryTmp": query_tmp, "QueryStat": query_stat}

        injections = self.injections
        self.injections = []  # reset injections for next query

        predefined_paths = self.predefined_paths
        self.predefined_paths = {}  # reset preredefined paths for next query

        return query_dict, injections, predefined_paths

    @override
    def visitQuery_tmp(self, ctx: ParserRTGL.Query_tmpContext) -> dict:
        r"""Visits a temporal query rule.

        Args:
            ctx (ParserRTGL.Query_tmpContext): Parse tree context.

        Returns:
            query_dict (dict): Dictionary with temporal query components.
        """
        self._rule2value(ctx.common_path_exprs())
        predict = self._rule2value(ctx.predict_tmp())
        for_each = self._rule2value(ctx.for_each_tmp())
        where = self._rule2value(ctx.where_tmp())
        assuming = self._rule2value(ctx.assuming())

        query_dict = {"Predict": predict, "ForEach": for_each, "Where": where, "Assuming": assuming}
        return query_dict

    @override
    def visitQuery_stat(self, ctx: ParserRTGL.Query_statContext) -> dict:
        r"""Visits a static query rule.

        Args:
            ctx (ParserRTGL.Query_statContext): Parse tree context.

        Returns:
            query_dict (dict): Dictionary with static query components.
        """
        self._rule2value(ctx.common_path_exprs())
        predict = self._rule2value(ctx.predict_stat())
        for_each = self._rule2value(ctx.for_each_stat())
        where = self._rule2value(ctx.where_stat())

        query_dict = {"Predict": predict, "ForEach": for_each, "Where": where}
        return query_dict

    @override
    def visitCommon_path_exprs(self, ctx:ParserRTGL.Common_path_exprsContext):
        for common_path_expr in ctx.common_path_expr():
            self.visit(common_path_expr)

    @override
    def visitCommon_path_expr(self, ctx:ParserRTGL.Common_path_exprContext):
        path = []
        for id_dot_id in ctx.id_dot_id():
            table, column = self._rule2value(id_dot_id).value
            path.append((column, table))
    
        self.predefined_paths[self._node2value(ctx.ID())] = path

    @override
    def visitFor_each_tmp(self, ctx: ParserRTGL.For_each_tmpContext) -> dict:
        r"""Visits temporal FOR EACH clause.

        Args:
            ctx (ParserRTGL.For_each_tmpContext): Parse tree context.

        Returns:
            for_each_dict (dict): Dictionary with FOR EACH components.
        """
        table = self._rule2value(ctx.table_tmp()).value
        column = self._rule2value(ctx.column()).value
        where = self._rule2value(ctx.where_stat())

        for_each_dict = {"Table": table, "Column": column, "Where": where}
        return for_each_dict
    
    @override
    def visitFor_each_stat(self, ctx: ParserRTGL.For_each_statContext) -> dict:
        r"""Visits static FOR EACH clause.

        Args:
            ctx (ParserRTGL.For_each_statContext): Parse tree context.

        Returns:
            for_each_dict (dict): Dictionary with FOR EACH components.
        """
        table = self._rule2value(ctx.table_stat()).value
        column = self._rule2value(ctx.column()).value
        where = self._rule2value(ctx.where_stat())

        for_each_dict = {"Table": table, "Column": column, "Where": where}
        return for_each_dict

    @override
    def visitPredict_tmp(self, ctx: ParserRTGL.Predict_tmpContext) -> dict:
        r"""Visits temporal PREDICT clause.

        Args:
            ctx (ParserRTGL.Predict_tmpContext): Parse tree context.

        Returns:
            predict_dict (dict): Dictionary with temporal PREDICT components.
        """
        if ctx.aggregation_tmp():
            pred_type = "aggregation"
        elif ctx.expr_or_tmp():
            pred_type = "expr"
    
        aggregation = self._rule2value(ctx.aggregation_tmp())
        expr = self._rule2value(ctx.expr_or_tmp())

        rank_top = self._node2value(ctx.RANK_TOP())
        k = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {
            "PredType": pred_type,
            "Aggregation": aggregation,
            "Expr": expr,
            "RankTop": rank_top,
            "K": k,
            "Classify": classify,
        }
        return predict_dict

    @override
    def visitPredict_stat(self, ctx: ParserRTGL.Predict_statContext) -> dict:
        r"""Visits static PREDICT clause.

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

        aggregation = self._rule2value(ctx.aggregation_stat())
        expr = self._rule2value(ctx.expr_or_stat())
        table = self._rule2value(ctx.table_stat()).value
        column = self._rule2value(ctx.column()).value

        rank_top = self._node2value(ctx.RANK_TOP())
        k = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {
            "PredType": pred_type,
            "Aggregation": aggregation,
            "Expr": expr,
            "Table": table,
            "Column": column,
            "RankTop": rank_top,
            "K": k,
            "Classify": classify,
        }
        return predict_dict

    @override
    def visitWhere_tmp(self, ctx: ParserRTGL.Where_tmpContext) -> dict:
        r"""Visits temporal WHERE clause.

        Args:
            ctx (ctx:ParserRTGL.Where_tmpContext): Parse tree context.

        Returns:
            where_dict (dict): Dictionary with temporal WHERE components.
        """
        expr = self._rule2value(ctx.expr_or_tmp())

        where_dict = {"Expr": expr}
        return where_dict

    @override
    def visitWhere_stat(self, ctx: ParserRTGL.Where_statContext) -> dict:
        r"""Visits static WHERE clause.

        Args:
            ctx (ctx:ParserRTGL.Where_statContext): Parse tree context.

        Returns:
            where_dict (dict): Dictionary with static WHERE components.
        """
        expr = self._rule2value(ctx.expr_or_stat())
        is_simple, table = self._is_expr_simple(expr.value)

        where_dict = {"Expr": expr,
                      "IsSimple": is_simple,
                      "Table": table}
        return where_dict

    @override
    def visitAssuming(self, ctx: ParserRTGL.AssumingContext) -> dict:
        r"""Visits ASSUMING clause.
    
        Args:
            ctx (ctx:ParserRTGL.AssumingContext): Parse tree context.
    
        Returns:
            assuming_dict (dict): Dictionary with ASSUMING components.
        """
        expr = self._rule2value(ctx.expr_or_tmp())
    
        assuming_dict = {"Expr": expr}
        return assuming_dict

    # @override
    # def visitIn_path(self, ctx:ParserRTGL.In_pathContext):
    #     path = []
    #     for id_dot_id in ctx.id_dot_id():
    #         table, column = self._rule2value(id_dot_id).value
    #         path.append((column.value, table.value))

    #     path_alias = self._rule2value(ctx.path_alias()).value if ctx.path_alias() else "__PREDICT_PATH__"
    #     self.predefined_paths[path_alias] = path

    #     return path_alias
    
    @override
    def visitExpr_or_tmp(self, ctx: ParserRTGL.Expr_or_tmpContext) -> dict | ParsedValue:
        r"""Visits a temporal OR expression.

        Builds a left-associative tree of OR operations.
        For single expressions, returns the expression directly.
        For multiple OR expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_or_tmpContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_and_tmp()) == 1:
            return self.visit(ctx.expr_and_tmp(0))

        # build left-associative OR tree
        expr_dict = self.visit(ctx.expr_and_tmp(0))
        for i in range(1, len(ctx.expr_and_tmp())):
            right = self.visit(ctx.expr_and_tmp(i))
            expr_dict = {"Op": self._node2value(ctx.OR(i - 1)), "LeftExpr": expr_dict, "RightExpr": right}

        return expr_dict

    @override
    def visitExpr_or_stat(self, ctx: ParserRTGL.Expr_or_statContext):
        r"""Visits a static OR expression.

        Builds a left-associative tree of OR operations.
        For single expressions, returns the expression directly.
        For multiple OR expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_or_statContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_and_stat()) == 1:
            return self.visit(ctx.expr_and_stat(0))

        # build left-associative OR tree
        expr_dict = self.visit(ctx.expr_and_stat(0))
        for i in range(1, len(ctx.expr_and_stat())):
            right = self.visit(ctx.expr_and_stat(i))
            expr_dict = {"Op": self._node2value(ctx.OR(i - 1)), "LeftExpr": expr_dict, "RightExpr": right}

        return expr_dict

    @override
    def visitExpr_and_tmp(self, ctx: ParserRTGL.Expr_and_tmpContext) -> dict | ParsedValue:
        r"""Visits a temporal AND expression.

        Builds a left-associative tree of AND operations.
        For single expressions, returns the expression directly.
        For multiple AND expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_and_tmpContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_term_tmp()) == 1:
            return self.visit(ctx.expr_term_tmp(0))

        # build left-associative AND tree
        expr_dict = self.visit(ctx.expr_term_tmp(0))
        for i in range(1, len(ctx.expr_term_tmp())):
            right = self.visit(ctx.expr_term_tmp(i))
            expr_dict = {"Op": self._node2value(ctx.AND(i - 1)), "LeftExpr": expr_dict, "RightExpr": right}

        return expr_dict

    @override
    def visitExpr_and_stat(self, ctx: ParserRTGL.Expr_and_statContext) -> dict | ParsedValue:
        r"""Visits a static AND expression.

        Builds a left-associative tree of AND operations.
        For single expressions, returns the expression directly.
        For multiple AND expressions, creates a nested dictionary structure.

        Args:
            ctx (ParserRTGL.Expr_and_statContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_term_stat()) == 1:
            return self.visit(ctx.expr_term_stat(0))

        # build left-associative AND tree
        expr_dict = self.visit(ctx.expr_term_stat(0))
        for i in range(1, len(ctx.expr_term_stat())):
            right = self.visit(ctx.expr_term_stat(i))
            expr_dict = {"Op": self._node2value(ctx.AND(i - 1)), "LeftExpr": expr_dict, "RightExpr": right}

        return expr_dict

    @override
    def visitExpr_term_tmp(self, ctx: ParserRTGL.Expr_term_tmpContext) -> dict | ParsedValue:
        """Visits a temporal term expression (base case or parenthesized expr).

        Args:
            ctx (ParserRTGL.Expr_term_tmpContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        if ctx.condition_tmp():
            return self._rule2value(ctx.condition_tmp())
        elif ctx.expr_or_tmp():
            return self.visit(ctx.expr_or_tmp())

    @override
    def visitExpr_term_stat(self, ctx: ParserRTGL.Expr_term_statContext) -> dict | ParsedValue:
        """Visits a static term expression (base case or parenthesized expr).

        Args:
            ctx (ParserRTGL.Expr_term_statContext): Parse tree context.

        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        if ctx.condition_stat():
            return self._rule2value(ctx.condition_stat())
        elif ctx.expr_or_stat():
            return self.visit(ctx.expr_or_stat())

    @override
    def visitCondition_tmp(self, ctx: ParserRTGL.Condition_tmpContext) -> dict:
        r"""Visits a temporal condition.

        Args:
            ctx (ParserRTGL.Condition_tmpContext): Parse tree context.

        Returns:
            condition_dict (dict): Dictionary with temporal condition components.
        """
        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())

        cond_dict["CondType"] = "aggregation"
        cond_dict["NOT"] = self._node2value(ctx.NOT())
        cond_dict["Aggregation"] = self._rule2value(ctx.aggregation_tmp())
        return cond_dict

    @override
    def visitCondition_stat(self, ctx: ParserRTGL.Condition_statContext):
        r"""Visits a static condition.

        Args:
            ctx (ParserRTGL.Condition_statContext): Parse tree context.

        Returns:
            condition_dict (dict): Dictionary with static condition components.
        """
        cond_type = "aggregation" if ctx.aggregation_stat() else "id_dot_id"

        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())
        
        cond_dict["CondType"] = cond_type
        cond_dict["NOT"] = self._node2value(ctx.NOT())
        cond_dict["Aggregation"] = self._rule2value(ctx.aggregation_stat())
        cond_dict["Table"] = self._rule2value(ctx.table_stat()).value
        cond_dict["Column"] = self._rule2value(ctx.column()).value
        return cond_dict

    @override
    def visitNum_condition(self, ctx: ParserRTGL.Num_conditionContext) -> dict:
        r"""Visits a numerical condition.

        Args:
            ctx (ParserRTGL.Num_conditionContext): Parse tree context.

        Returns:
            num_cond_dict (dict): Dictionary with numerical condition components.
        """
        ctype = "num"
        comp_op = self._node2value(ctx.NUM_COMP_OP())

        if ctx.DATETIME():
            n = self._node2value(ctx.DATETIME())
        elif ctx.FLOAT():
            n = self._node2value(ctx.FLOAT())
        elif ctx.INT():
            n = self._node2value(ctx.INT())

        num_cond_dict = {"CType": ctype, "CompOp": comp_op, "N": n}
        return num_cond_dict

    @override
    def visitStr_condition(self, ctx: ParserRTGL.Str_conditionContext) -> dict:
        r"""Visits a string condition.

        Args:
            ctx (ParserRTGL.Str_conditionContext): Parse tree context.

        Returns:
            str_cond_dict (dict): Dictionary with string condition components.
        """
        ctype = "str"
        comp_op = self._node2value(ctx.STR_COMP_OP())
        string = self._node2value(ctx.STRING())

        str_cond_dict = {"CType": ctype, "CompOp": comp_op, "String": string}
        return str_cond_dict

    @override
    def visitNull_check_condition(self, ctx: ParserRTGL.Null_check_conditionContext) -> dict:
        r"""Visits a null check condition.

        Args:
            ctx (ParserRTGL.Null_check_conditionContext): Parse tree context.

        Returns:
            null_cond_dict (dict): Dictionary with null check condition components.
        """
        ctype = "null"
        check_op = self._node2value(ctx.NULL_CHECK_OP())

        null_cond_dict = {"CType": ctype, "CheckOp": check_op}
        return null_cond_dict

    @override
    def visitAggregation_tmp(self, ctx: ParserRTGL.Aggregation_tmpContext) -> dict:
        r"""Visits a temporal aggregation.

        Args:
            ctx (ParserRTGL.Aggregation_tmpContext): Parse tree context.

        Returns:
            aggr_dict (dict): Dictionary with temporal aggregation components.
        """
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._rule2value(ctx.table_tmp()).value
        column = self._rule2value(ctx.column()).value
        where = self._rule2value(ctx.where_stat())
        start = self._node2value(ctx.INT(0))
        end = self._node2value(ctx.INT(1))
        measure_unit = self._node2value(ctx.TIME_MEASURE_UNIT())

        aggr_dict = {
            "AggrType": aggr_type,
            "Table": table,
            "Column": column,
            "Where": where,
            "Start": start,
            "End": end,
            "MeasureUnit": measure_unit,
        }
        return aggr_dict

    @override
    def visitAggregation_stat(self, ctx: ParserRTGL.Aggregation_statContext) -> dict:
        r"""Visits a stat aggregation.

        Args:
            ctx (ParserRTGL.Aggregation_statContext): Parse tree context.

        Returns:
            aggr_dict (dict): Dictionary with static aggregation components.
        """
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._rule2value(ctx.table_stat()).value
        column = self._rule2value(ctx.column()).value
        where = self._rule2value(ctx.where_stat())

        aggr_dict = {
            "AggrType": aggr_type,
            "Table": table,
            "Column": column,
            "Where": where,
        }
        return aggr_dict

    @override
    def visitSql_injection_tmp(self, ctx: ParserRTGL.Sql_injection_tmpContext) -> ParsedValue:
        r"""Visits a temporal SQL injection.
        
        Creates a ParsedValue for the SQL injection and stores its components.

        Args:
            ctx (ParserRTGL.Sql_injection_tmpContext): Parse tree context.
        
        Returns:
            name (str): Name of the SQL injection.
        """
        body = ctx.SQL_INJECTION_BODY().getSymbol().text[1:-1]
        name = self._node2value(ctx.table_name)

        pkey_col = self._node2value(ctx.pkey_col).value
        time_col = self._node2value(ctx.time_col).value  

        fkey_col_to_pkey_table = {}
        for fkey_ctx in ctx.fkey_col_to_pkey_table():
            fkey, table = self._rule2value(fkey_ctx).value
            fkey_col_to_pkey_table[fkey] = table
        
        fkey_table_col = {}
        for id_dot_id_ctx in ctx.id_dot_id():
            table, fkey = self._rule2value(id_dot_id_ctx).value
            fkey_table_col[table] = fkey

        self.injections.append(
            (body, name.value, pkey_col, fkey_col_to_pkey_table, fkey_table_col, time_col)
        )

        return name

    @override
    def visitSql_injection_stat(self, ctx: ParserRTGL.Sql_injection_statContext) -> ParsedValue:
        r"""Visits a static SQL injection.
        
        Creates a ParsedValue for the SQL injection and stores its components.
        
        Args:
            ctx (ParserRTGL.Sql_injection_statContext): Parse tree context.
        
        Returns:
            name (str): Name of the SQL injection.
        """
        body = ctx.SQL_INJECTION_BODY().getSymbol().text[1:-1]
        name = self._node2value(ctx.table_name)
        pkey_col = self._node2value(ctx.pkey_col).value
        
        fkey_col_to_pkey_table = {}
        for fkey_ctx in ctx.fkey_col_to_pkey_table():
            fkey, table = self._rule2value(fkey_ctx).value
            fkey_col_to_pkey_table[fkey] = table
        
        fkey_table_col = {}
        for id_dot_id_ctx in ctx.id_dot_id():
            table, fkey = self._rule2value(id_dot_id_ctx).value
            fkey_table_col[table] = fkey

        self.injections.append(
            (body, name.value, pkey_col, fkey_col_to_pkey_table, fkey_table_col)
        )

        return name
    
    @override
    def visitFkey_col_to_pkey_table(self, ctx:ParserRTGL.Fk_col_to_pk_tableContext):
        return self._node2value(ctx.ID(0)), self._node2value(ctx.ID(1))

    @override
    def visitTable_tmp(self, ctx:ParserRTGL.Table_tmpContext):
        return self.visit(ctx.sql_injection_tmp()) if ctx.sql_injection_tmp() else self._node2value(ctx.ID())
    
    @override
    def visitTable_stat(self, ctx:ParserRTGL.Table_statContext):
        return self.visit(ctx.sql_injection_stat()) if ctx.sql_injection_stat() else self._node2value(ctx.ID())
    
    @override    
    def visitColumn(self, ctx:ParserRTGL.ColumnContext):
        return self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID())

    @override
    def visitId_dot_id(self, ctx:ParserRTGL.Id_dot_idContext):
        return self._node2value(ctx.ID(0)), self._node2value(ctx.ID(1))

    ################## Helper methods ##################

    def _node2value(self, node: TerminalNode | None) -> ParsedValue | None:
        r"""Converts a terminal node (token) to *`ParsedValue`*.

        Extracts the text and position information from an ANTLR terminal node.

        Args:
            node (TerminalNode | None): ANTLR terminal node, or None.

        Returns:
            out (ParsedValue | None): Wrapped value with location, or None if node is None.
        """
        if not node:
            return None

        token = node.getSymbol()
        return ParsedValue(value=token.text.lower(), line=token.line, column=token.column)

    def _rule2value(self, ctx: ParserRuleContext | None) -> ParsedValue | None:
        r"""Converts a rule context to *`ParsedValue`*.

        Visits the rule context and wraps the result with location info.

        Args:
            ctx (ParserRuleContext | None): ANTLR rule context, or None.

        Returns:
            out (ParsedValue | None): Wrapped visit result with location, or None if ctx is None.
        """
        if not ctx:
            return None

        return ParsedValue(value=self.visit(ctx), line=ctx.start.line, column=ctx.start.column)

    def _is_expr_simple(self, expr) -> tuple[bool, str]:
        def _extract_tables(node: dict | ParsedValue):
            if isinstance(node, dict) and "Op" in node:
                yield from _extract_tables(node["LeftExpr"])
                yield from _extract_tables(node["RightExpr"])
            else:
                node = node.value
                leaf = node["Aggregation"].value if node["CondType"] == "aggregation" else node
                yield leaf["Table"].value
        unique_tables = set(_extract_tables(expr))
    
        return len(unique_tables) <= 1, unique_tables.pop()
