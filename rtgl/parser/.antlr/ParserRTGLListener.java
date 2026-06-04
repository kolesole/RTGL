// Generated from /home/kolesiko/CTU/BT/BT/RTGL/rtgl/parser/ParserRTGL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ParserRTGL}.
 */
public interface ParserRTGLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#query}.
	 * @param ctx the parse tree
	 */
	void enterQuery(ParserRTGL.QueryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#query}.
	 * @param ctx the parse tree
	 */
	void exitQuery(ParserRTGL.QueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#query_tmp}.
	 * @param ctx the parse tree
	 */
	void enterQuery_tmp(ParserRTGL.Query_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#query_tmp}.
	 * @param ctx the parse tree
	 */
	void exitQuery_tmp(ParserRTGL.Query_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#query_stat}.
	 * @param ctx the parse tree
	 */
	void enterQuery_stat(ParserRTGL.Query_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#query_stat}.
	 * @param ctx the parse tree
	 */
	void exitQuery_stat(ParserRTGL.Query_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#for_each}.
	 * @param ctx the parse tree
	 */
	void enterFor_each(ParserRTGL.For_eachContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#for_each}.
	 * @param ctx the parse tree
	 */
	void exitFor_each(ParserRTGL.For_eachContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#predict_tmp}.
	 * @param ctx the parse tree
	 */
	void enterPredict_tmp(ParserRTGL.Predict_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#predict_tmp}.
	 * @param ctx the parse tree
	 */
	void exitPredict_tmp(ParserRTGL.Predict_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#predict_stat}.
	 * @param ctx the parse tree
	 */
	void enterPredict_stat(ParserRTGL.Predict_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#predict_stat}.
	 * @param ctx the parse tree
	 */
	void exitPredict_stat(ParserRTGL.Predict_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#assuming}.
	 * @param ctx the parse tree
	 */
	void enterAssuming(ParserRTGL.AssumingContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#assuming}.
	 * @param ctx the parse tree
	 */
	void exitAssuming(ParserRTGL.AssumingContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#where_tmp}.
	 * @param ctx the parse tree
	 */
	void enterWhere_tmp(ParserRTGL.Where_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#where_tmp}.
	 * @param ctx the parse tree
	 */
	void exitWhere_tmp(ParserRTGL.Where_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#where_stat}.
	 * @param ctx the parse tree
	 */
	void enterWhere_stat(ParserRTGL.Where_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#where_stat}.
	 * @param ctx the parse tree
	 */
	void exitWhere_stat(ParserRTGL.Where_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#expr_or_tmp}.
	 * @param ctx the parse tree
	 */
	void enterExpr_or_tmp(ParserRTGL.Expr_or_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#expr_or_tmp}.
	 * @param ctx the parse tree
	 */
	void exitExpr_or_tmp(ParserRTGL.Expr_or_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#expr_or_stat}.
	 * @param ctx the parse tree
	 */
	void enterExpr_or_stat(ParserRTGL.Expr_or_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#expr_or_stat}.
	 * @param ctx the parse tree
	 */
	void exitExpr_or_stat(ParserRTGL.Expr_or_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#expr_and_tmp}.
	 * @param ctx the parse tree
	 */
	void enterExpr_and_tmp(ParserRTGL.Expr_and_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#expr_and_tmp}.
	 * @param ctx the parse tree
	 */
	void exitExpr_and_tmp(ParserRTGL.Expr_and_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#expr_and_stat}.
	 * @param ctx the parse tree
	 */
	void enterExpr_and_stat(ParserRTGL.Expr_and_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#expr_and_stat}.
	 * @param ctx the parse tree
	 */
	void exitExpr_and_stat(ParserRTGL.Expr_and_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#expr_term_tmp}.
	 * @param ctx the parse tree
	 */
	void enterExpr_term_tmp(ParserRTGL.Expr_term_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#expr_term_tmp}.
	 * @param ctx the parse tree
	 */
	void exitExpr_term_tmp(ParserRTGL.Expr_term_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#expr_term_stat}.
	 * @param ctx the parse tree
	 */
	void enterExpr_term_stat(ParserRTGL.Expr_term_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#expr_term_stat}.
	 * @param ctx the parse tree
	 */
	void exitExpr_term_stat(ParserRTGL.Expr_term_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#condition_tmp}.
	 * @param ctx the parse tree
	 */
	void enterCondition_tmp(ParserRTGL.Condition_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#condition_tmp}.
	 * @param ctx the parse tree
	 */
	void exitCondition_tmp(ParserRTGL.Condition_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#condition_stat}.
	 * @param ctx the parse tree
	 */
	void enterCondition_stat(ParserRTGL.Condition_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#condition_stat}.
	 * @param ctx the parse tree
	 */
	void exitCondition_stat(ParserRTGL.Condition_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#num_condition}.
	 * @param ctx the parse tree
	 */
	void enterNum_condition(ParserRTGL.Num_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#num_condition}.
	 * @param ctx the parse tree
	 */
	void exitNum_condition(ParserRTGL.Num_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#str_condition}.
	 * @param ctx the parse tree
	 */
	void enterStr_condition(ParserRTGL.Str_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#str_condition}.
	 * @param ctx the parse tree
	 */
	void exitStr_condition(ParserRTGL.Str_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#null_check_condition}.
	 * @param ctx the parse tree
	 */
	void enterNull_check_condition(ParserRTGL.Null_check_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#null_check_condition}.
	 * @param ctx the parse tree
	 */
	void exitNull_check_condition(ParserRTGL.Null_check_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#aggregation_tmp}.
	 * @param ctx the parse tree
	 */
	void enterAggregation_tmp(ParserRTGL.Aggregation_tmpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#aggregation_tmp}.
	 * @param ctx the parse tree
	 */
	void exitAggregation_tmp(ParserRTGL.Aggregation_tmpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ParserRTGL#aggregation_stat}.
	 * @param ctx the parse tree
	 */
	void enterAggregation_stat(ParserRTGL.Aggregation_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ParserRTGL#aggregation_stat}.
	 * @param ctx the parse tree
	 */
	void exitAggregation_stat(ParserRTGL.Aggregation_statContext ctx);
}