# Generated from ParserRTGL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserRTGL import ParserRTGL
else:
    from ParserRTGL import ParserRTGL

# This class defines a complete generic visitor for a parse tree produced by ParserRTGL.

class ParserRTGLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserRTGL#query.
    def visitQuery(self, ctx:ParserRTGL.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#query_tmp.
    def visitQuery_tmp(self, ctx:ParserRTGL.Query_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#query_stat.
    def visitQuery_stat(self, ctx:ParserRTGL.Query_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#for_each_tmp.
    def visitFor_each_tmp(self, ctx:ParserRTGL.For_each_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#for_each_stat.
    def visitFor_each_stat(self, ctx:ParserRTGL.For_each_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#predict_tmp.
    def visitPredict_tmp(self, ctx:ParserRTGL.Predict_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#predict_stat.
    def visitPredict_stat(self, ctx:ParserRTGL.Predict_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#assuming.
    def visitAssuming(self, ctx:ParserRTGL.AssumingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#where_tmp.
    def visitWhere_tmp(self, ctx:ParserRTGL.Where_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#where_stat.
    def visitWhere_stat(self, ctx:ParserRTGL.Where_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#expr_or_tmp.
    def visitExpr_or_tmp(self, ctx:ParserRTGL.Expr_or_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#expr_or_stat.
    def visitExpr_or_stat(self, ctx:ParserRTGL.Expr_or_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#expr_and_tmp.
    def visitExpr_and_tmp(self, ctx:ParserRTGL.Expr_and_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#expr_and_stat.
    def visitExpr_and_stat(self, ctx:ParserRTGL.Expr_and_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#expr_term_tmp.
    def visitExpr_term_tmp(self, ctx:ParserRTGL.Expr_term_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#expr_term_stat.
    def visitExpr_term_stat(self, ctx:ParserRTGL.Expr_term_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#condition_tmp.
    def visitCondition_tmp(self, ctx:ParserRTGL.Condition_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#condition_stat.
    def visitCondition_stat(self, ctx:ParserRTGL.Condition_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#num_condition.
    def visitNum_condition(self, ctx:ParserRTGL.Num_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#str_condition.
    def visitStr_condition(self, ctx:ParserRTGL.Str_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#null_check_condition.
    def visitNull_check_condition(self, ctx:ParserRTGL.Null_check_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#aggregation_tmp.
    def visitAggregation_tmp(self, ctx:ParserRTGL.Aggregation_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#aggregation_stat.
    def visitAggregation_stat(self, ctx:ParserRTGL.Aggregation_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#sql_injection_tmp.
    def visitSql_injection_tmp(self, ctx:ParserRTGL.Sql_injection_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#sql_injection_stat.
    def visitSql_injection_stat(self, ctx:ParserRTGL.Sql_injection_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#fk_col_to_pk_table.
    def visitFk_col_to_pk_table(self, ctx:ParserRTGL.Fk_col_to_pk_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserRTGL#fk_table_col.
    def visitFk_table_col(self, ctx:ParserRTGL.Fk_table_colContext):
        return self.visitChildren(ctx)



del ParserRTGL