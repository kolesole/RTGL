# Generated from ParserRTGL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserRTGL import ParserRTGL
else:
    from ParserRTGL import ParserRTGL

# This class defines a complete listener for a parse tree produced by ParserRTGL.
class ParserRTGLListener(ParseTreeListener):

    # Enter a parse tree produced by ParserRTGL#query.
    def enterQuery(self, ctx:ParserRTGL.QueryContext):
        pass

    # Exit a parse tree produced by ParserRTGL#query.
    def exitQuery(self, ctx:ParserRTGL.QueryContext):
        pass


    # Enter a parse tree produced by ParserRTGL#query_tmp.
    def enterQuery_tmp(self, ctx:ParserRTGL.Query_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#query_tmp.
    def exitQuery_tmp(self, ctx:ParserRTGL.Query_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#query_stat.
    def enterQuery_stat(self, ctx:ParserRTGL.Query_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#query_stat.
    def exitQuery_stat(self, ctx:ParserRTGL.Query_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#for_each_tmp.
    def enterFor_each_tmp(self, ctx:ParserRTGL.For_each_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#for_each_tmp.
    def exitFor_each_tmp(self, ctx:ParserRTGL.For_each_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#for_each_stat.
    def enterFor_each_stat(self, ctx:ParserRTGL.For_each_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#for_each_stat.
    def exitFor_each_stat(self, ctx:ParserRTGL.For_each_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#predict_tmp.
    def enterPredict_tmp(self, ctx:ParserRTGL.Predict_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#predict_tmp.
    def exitPredict_tmp(self, ctx:ParserRTGL.Predict_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#predict_stat.
    def enterPredict_stat(self, ctx:ParserRTGL.Predict_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#predict_stat.
    def exitPredict_stat(self, ctx:ParserRTGL.Predict_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#assuming.
    def enterAssuming(self, ctx:ParserRTGL.AssumingContext):
        pass

    # Exit a parse tree produced by ParserRTGL#assuming.
    def exitAssuming(self, ctx:ParserRTGL.AssumingContext):
        pass


    # Enter a parse tree produced by ParserRTGL#where_tmp.
    def enterWhere_tmp(self, ctx:ParserRTGL.Where_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#where_tmp.
    def exitWhere_tmp(self, ctx:ParserRTGL.Where_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#where_stat.
    def enterWhere_stat(self, ctx:ParserRTGL.Where_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#where_stat.
    def exitWhere_stat(self, ctx:ParserRTGL.Where_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#expr_or_tmp.
    def enterExpr_or_tmp(self, ctx:ParserRTGL.Expr_or_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#expr_or_tmp.
    def exitExpr_or_tmp(self, ctx:ParserRTGL.Expr_or_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#expr_or_stat.
    def enterExpr_or_stat(self, ctx:ParserRTGL.Expr_or_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#expr_or_stat.
    def exitExpr_or_stat(self, ctx:ParserRTGL.Expr_or_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#expr_and_tmp.
    def enterExpr_and_tmp(self, ctx:ParserRTGL.Expr_and_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#expr_and_tmp.
    def exitExpr_and_tmp(self, ctx:ParserRTGL.Expr_and_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#expr_and_stat.
    def enterExpr_and_stat(self, ctx:ParserRTGL.Expr_and_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#expr_and_stat.
    def exitExpr_and_stat(self, ctx:ParserRTGL.Expr_and_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#expr_term_tmp.
    def enterExpr_term_tmp(self, ctx:ParserRTGL.Expr_term_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#expr_term_tmp.
    def exitExpr_term_tmp(self, ctx:ParserRTGL.Expr_term_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#expr_term_stat.
    def enterExpr_term_stat(self, ctx:ParserRTGL.Expr_term_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#expr_term_stat.
    def exitExpr_term_stat(self, ctx:ParserRTGL.Expr_term_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#condition_tmp.
    def enterCondition_tmp(self, ctx:ParserRTGL.Condition_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#condition_tmp.
    def exitCondition_tmp(self, ctx:ParserRTGL.Condition_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#condition_stat.
    def enterCondition_stat(self, ctx:ParserRTGL.Condition_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#condition_stat.
    def exitCondition_stat(self, ctx:ParserRTGL.Condition_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#num_condition.
    def enterNum_condition(self, ctx:ParserRTGL.Num_conditionContext):
        pass

    # Exit a parse tree produced by ParserRTGL#num_condition.
    def exitNum_condition(self, ctx:ParserRTGL.Num_conditionContext):
        pass


    # Enter a parse tree produced by ParserRTGL#str_condition.
    def enterStr_condition(self, ctx:ParserRTGL.Str_conditionContext):
        pass

    # Exit a parse tree produced by ParserRTGL#str_condition.
    def exitStr_condition(self, ctx:ParserRTGL.Str_conditionContext):
        pass


    # Enter a parse tree produced by ParserRTGL#null_check_condition.
    def enterNull_check_condition(self, ctx:ParserRTGL.Null_check_conditionContext):
        pass

    # Exit a parse tree produced by ParserRTGL#null_check_condition.
    def exitNull_check_condition(self, ctx:ParserRTGL.Null_check_conditionContext):
        pass


    # Enter a parse tree produced by ParserRTGL#aggregation_tmp.
    def enterAggregation_tmp(self, ctx:ParserRTGL.Aggregation_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#aggregation_tmp.
    def exitAggregation_tmp(self, ctx:ParserRTGL.Aggregation_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#aggregation_stat.
    def enterAggregation_stat(self, ctx:ParserRTGL.Aggregation_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#aggregation_stat.
    def exitAggregation_stat(self, ctx:ParserRTGL.Aggregation_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#sql_injection_tmp.
    def enterSql_injection_tmp(self, ctx:ParserRTGL.Sql_injection_tmpContext):
        pass

    # Exit a parse tree produced by ParserRTGL#sql_injection_tmp.
    def exitSql_injection_tmp(self, ctx:ParserRTGL.Sql_injection_tmpContext):
        pass


    # Enter a parse tree produced by ParserRTGL#sql_injection_stat.
    def enterSql_injection_stat(self, ctx:ParserRTGL.Sql_injection_statContext):
        pass

    # Exit a parse tree produced by ParserRTGL#sql_injection_stat.
    def exitSql_injection_stat(self, ctx:ParserRTGL.Sql_injection_statContext):
        pass


    # Enter a parse tree produced by ParserRTGL#fk_col_to_pk_table.
    def enterFk_col_to_pk_table(self, ctx:ParserRTGL.Fk_col_to_pk_tableContext):
        pass

    # Exit a parse tree produced by ParserRTGL#fk_col_to_pk_table.
    def exitFk_col_to_pk_table(self, ctx:ParserRTGL.Fk_col_to_pk_tableContext):
        pass


    # Enter a parse tree produced by ParserRTGL#fk_table_col.
    def enterFk_table_col(self, ctx:ParserRTGL.Fk_table_colContext):
        pass

    # Exit a parse tree produced by ParserRTGL#fk_table_col.
    def exitFk_table_col(self, ctx:ParserRTGL.Fk_table_colContext):
        pass



del ParserRTGL