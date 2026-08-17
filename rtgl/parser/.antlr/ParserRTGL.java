// Generated from /home/kolesiko/CTU/BT/BT/RTGL/rtgl/parser/ParserRTGL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ParserRTGL extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WITH=1, FOR_EACH=2, PREDICT=3, WHERE=4, ASSUMING=5, AS=6, CLASSIFY=7, 
		RANK_TOP=8, AGGR_FUNC=9, AVG=10, COUNT=11, COUNT_DISTINCT=12, FIRST=13, 
		LAST=14, LIST_DISTINCT=15, MAX=16, MIN=17, SUM=18, NUM_COMP_OP=19, STR_COMP_OP=20, 
		NOT_LIKE=21, NOT_CONTAINS=22, ENDS_WITH=23, STARTS_WITH=24, LIKE=25, CONTAINS=26, 
		NULL_CHECK_OP=27, IS_NOT_NULL=28, IS_NULL=29, DOT=30, COMMA=31, OPEN_PAREN=32, 
		CLOSE_PAREN=33, OPEN_BRACKET=34, CLOSE_BRACKET=35, OPEN_BRACE=36, CLOSE_BRACE=37, 
		STAR=38, SEMICOLON=39, ARROW=40, COLON=41, AND=42, OR=43, NOT=44, DATETIME=45, 
		FLOAT=46, INT=47, TIME_MEASURE_UNIT=48, STRING=49, ID=50, SQL_INJECTION_BODY=51, 
		WS_SKIP=52, ANY=53;
	public static final int
		RULE_query = 0, RULE_query_tmp = 1, RULE_query_stat = 2, RULE_common_path_exprs = 3, 
		RULE_common_path_expr = 4, RULE_for_each_tmp = 5, RULE_for_each_stat = 6, 
		RULE_predict_tmp = 7, RULE_predict_stat = 8, RULE_where_tmp = 9, RULE_where_stat = 10, 
		RULE_assuming = 11, RULE_expr_or_tmp = 12, RULE_expr_or_stat = 13, RULE_expr_and_tmp = 14, 
		RULE_expr_and_stat = 15, RULE_expr_term_tmp = 16, RULE_expr_term_stat = 17, 
		RULE_condition_tmp = 18, RULE_condition_stat = 19, RULE_num_condition = 20, 
		RULE_str_condition = 21, RULE_null_check_condition = 22, RULE_aggregation_tmp = 23, 
		RULE_aggregation_stat = 24, RULE_sql_injection_tmp = 25, RULE_sql_injection_stat = 26, 
		RULE_fkey_col_to_pkey_table = 27, RULE_table_tmp = 28, RULE_table_stat = 29, 
		RULE_column = 30, RULE_id_dot_id = 31;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "query_tmp", "query_stat", "common_path_exprs", "common_path_expr", 
			"for_each_tmp", "for_each_stat", "predict_tmp", "predict_stat", "where_tmp", 
			"where_stat", "assuming", "expr_or_tmp", "expr_or_stat", "expr_and_tmp", 
			"expr_and_stat", "expr_term_tmp", "expr_term_stat", "condition_tmp", 
			"condition_stat", "num_condition", "str_condition", "null_check_condition", 
			"aggregation_tmp", "aggregation_stat", "sql_injection_tmp", "sql_injection_stat", 
			"fkey_col_to_pkey_table", "table_tmp", "table_stat", "column", "id_dot_id"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "'.'", "','", "'('", "')'", "'['", 
			"']'", "'{'", "'}'", "'*'", "';'", "'->'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WITH", "FOR_EACH", "PREDICT", "WHERE", "ASSUMING", "AS", "CLASSIFY", 
			"RANK_TOP", "AGGR_FUNC", "AVG", "COUNT", "COUNT_DISTINCT", "FIRST", "LAST", 
			"LIST_DISTINCT", "MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", "NOT_LIKE", 
			"NOT_CONTAINS", "ENDS_WITH", "STARTS_WITH", "LIKE", "CONTAINS", "NULL_CHECK_OP", 
			"IS_NOT_NULL", "IS_NULL", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", 
			"OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "STAR", 
			"SEMICOLON", "ARROW", "COLON", "AND", "OR", "NOT", "DATETIME", "FLOAT", 
			"INT", "TIME_MEASURE_UNIT", "STRING", "ID", "SQL_INJECTION_BODY", "WS_SKIP", 
			"ANY"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ParserRTGL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ParserRTGL(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public Query_tmpContext query_tmp() {
			return getRuleContext(Query_tmpContext.class,0);
		}
		public Query_statContext query_stat() {
			return getRuleContext(Query_statContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_query);
		try {
			setState(66);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				query_tmp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(65);
				query_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Query_tmpContext extends ParserRuleContext {
		public Predict_tmpContext predict_tmp() {
			return getRuleContext(Predict_tmpContext.class,0);
		}
		public For_each_tmpContext for_each_tmp() {
			return getRuleContext(For_each_tmpContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(ParserRTGL.SEMICOLON, 0); }
		public Common_path_exprsContext common_path_exprs() {
			return getRuleContext(Common_path_exprsContext.class,0);
		}
		public Where_tmpContext where_tmp() {
			return getRuleContext(Where_tmpContext.class,0);
		}
		public AssumingContext assuming() {
			return getRuleContext(AssumingContext.class,0);
		}
		public Query_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query_tmp; }
	}

	public final Query_tmpContext query_tmp() throws RecognitionException {
		Query_tmpContext _localctx = new Query_tmpContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_query_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(68);
				common_path_exprs();
				}
			}

			setState(71);
			predict_tmp();
			setState(72);
			for_each_tmp();
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(73);
				where_tmp();
				}
			}

			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSUMING) {
				{
				setState(76);
				assuming();
				}
			}

			setState(79);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Query_statContext extends ParserRuleContext {
		public Predict_statContext predict_stat() {
			return getRuleContext(Predict_statContext.class,0);
		}
		public For_each_statContext for_each_stat() {
			return getRuleContext(For_each_statContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(ParserRTGL.SEMICOLON, 0); }
		public Common_path_exprsContext common_path_exprs() {
			return getRuleContext(Common_path_exprsContext.class,0);
		}
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public Query_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query_stat; }
	}

	public final Query_statContext query_stat() throws RecognitionException {
		Query_statContext _localctx = new Query_statContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_query_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(81);
				common_path_exprs();
				}
			}

			setState(84);
			predict_stat();
			setState(85);
			for_each_stat();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(86);
				where_stat();
				}
			}

			setState(89);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Common_path_exprsContext extends ParserRuleContext {
		public TerminalNode WITH() { return getToken(ParserRTGL.WITH, 0); }
		public List<Common_path_exprContext> common_path_expr() {
			return getRuleContexts(Common_path_exprContext.class);
		}
		public Common_path_exprContext common_path_expr(int i) {
			return getRuleContext(Common_path_exprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserRTGL.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserRTGL.COMMA, i);
		}
		public Common_path_exprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_common_path_exprs; }
	}

	public final Common_path_exprsContext common_path_exprs() throws RecognitionException {
		Common_path_exprsContext _localctx = new Common_path_exprsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_common_path_exprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(WITH);
			setState(92);
			common_path_expr();
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(93);
				match(COMMA);
				setState(94);
				common_path_expr();
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Common_path_exprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ParserRTGL.ID, 0); }
		public TerminalNode AS() { return getToken(ParserRTGL.AS, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserRTGL.OPEN_PAREN, 0); }
		public List<Id_dot_idContext> id_dot_id() {
			return getRuleContexts(Id_dot_idContext.class);
		}
		public Id_dot_idContext id_dot_id(int i) {
			return getRuleContext(Id_dot_idContext.class,i);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public List<TerminalNode> ARROW() { return getTokens(ParserRTGL.ARROW); }
		public TerminalNode ARROW(int i) {
			return getToken(ParserRTGL.ARROW, i);
		}
		public Common_path_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_common_path_expr; }
	}

	public final Common_path_exprContext common_path_expr() throws RecognitionException {
		Common_path_exprContext _localctx = new Common_path_exprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_common_path_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(ID);
			setState(101);
			match(AS);
			setState(102);
			match(OPEN_PAREN);
			setState(103);
			id_dot_id();
			setState(106); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(104);
				match(ARROW);
				setState(105);
				id_dot_id();
				}
				}
				setState(108); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ARROW );
			setState(110);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_each_tmpContext extends ParserRuleContext {
		public TerminalNode FOR_EACH() { return getToken(ParserRTGL.FOR_EACH, 0); }
		public Table_tmpContext table_tmp() {
			return getRuleContext(Table_tmpContext.class,0);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public For_each_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_each_tmp; }
	}

	public final For_each_tmpContext for_each_tmp() throws RecognitionException {
		For_each_tmpContext _localctx = new For_each_tmpContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_for_each_tmp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(FOR_EACH);
			setState(113);
			table_tmp();
			setState(114);
			match(DOT);
			setState(115);
			column();
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(116);
				where_stat();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_each_statContext extends ParserRuleContext {
		public TerminalNode FOR_EACH() { return getToken(ParserRTGL.FOR_EACH, 0); }
		public Table_statContext table_stat() {
			return getRuleContext(Table_statContext.class,0);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public For_each_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_each_stat; }
	}

	public final For_each_statContext for_each_stat() throws RecognitionException {
		For_each_statContext _localctx = new For_each_statContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_for_each_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(FOR_EACH);
			setState(120);
			table_stat();
			setState(121);
			match(DOT);
			setState(122);
			column();
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(123);
				where_stat();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Predict_tmpContext extends ParserRuleContext {
		public TerminalNode PREDICT() { return getToken(ParserRTGL.PREDICT, 0); }
		public Aggregation_tmpContext aggregation_tmp() {
			return getRuleContext(Aggregation_tmpContext.class,0);
		}
		public TerminalNode RANK_TOP() { return getToken(ParserRTGL.RANK_TOP, 0); }
		public TerminalNode INT() { return getToken(ParserRTGL.INT, 0); }
		public TerminalNode CLASSIFY() { return getToken(ParserRTGL.CLASSIFY, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public Predict_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict_tmp; }
	}

	public final Predict_tmpContext predict_tmp() throws RecognitionException {
		Predict_tmpContext _localctx = new Predict_tmpContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_predict_tmp);
		try {
			setState(135);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				match(PREDICT);
				setState(127);
				aggregation_tmp();
				setState(131);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(128);
					match(RANK_TOP);
					setState(129);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(130);
					match(CLASSIFY);
					}
					break;
				case FOR_EACH:
					break;
				default:
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				match(PREDICT);
				setState(134);
				expr_or_tmp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Predict_statContext extends ParserRuleContext {
		public TerminalNode PREDICT() { return getToken(ParserRTGL.PREDICT, 0); }
		public Aggregation_statContext aggregation_stat() {
			return getRuleContext(Aggregation_statContext.class,0);
		}
		public TerminalNode RANK_TOP() { return getToken(ParserRTGL.RANK_TOP, 0); }
		public TerminalNode INT() { return getToken(ParserRTGL.INT, 0); }
		public TerminalNode CLASSIFY() { return getToken(ParserRTGL.CLASSIFY, 0); }
		public Expr_or_statContext expr_or_stat() {
			return getRuleContext(Expr_or_statContext.class,0);
		}
		public Table_statContext table_stat() {
			return getRuleContext(Table_statContext.class,0);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public Predict_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict_stat; }
	}

	public final Predict_statContext predict_stat() throws RecognitionException {
		Predict_statContext _localctx = new Predict_statContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_predict_stat);
		try {
			setState(151);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				match(PREDICT);
				setState(138);
				aggregation_stat();
				setState(142);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(139);
					match(RANK_TOP);
					setState(140);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(141);
					match(CLASSIFY);
					}
					break;
				case FOR_EACH:
					break;
				default:
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				match(PREDICT);
				setState(145);
				expr_or_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(146);
				match(PREDICT);
				setState(147);
				table_stat();
				setState(148);
				match(DOT);
				setState(149);
				column();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Where_tmpContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(ParserRTGL.WHERE, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public Where_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_tmp; }
	}

	public final Where_tmpContext where_tmp() throws RecognitionException {
		Where_tmpContext _localctx = new Where_tmpContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_where_tmp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(WHERE);
			setState(154);
			expr_or_tmp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Where_statContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(ParserRTGL.WHERE, 0); }
		public Expr_or_statContext expr_or_stat() {
			return getRuleContext(Expr_or_statContext.class,0);
		}
		public Where_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_stat; }
	}

	public final Where_statContext where_stat() throws RecognitionException {
		Where_statContext _localctx = new Where_statContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_where_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(WHERE);
			setState(157);
			expr_or_stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssumingContext extends ParserRuleContext {
		public TerminalNode ASSUMING() { return getToken(ParserRTGL.ASSUMING, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public AssumingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assuming; }
	}

	public final AssumingContext assuming() throws RecognitionException {
		AssumingContext _localctx = new AssumingContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assuming);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(ASSUMING);
			setState(160);
			expr_or_tmp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_or_tmpContext extends ParserRuleContext {
		public List<Expr_and_tmpContext> expr_and_tmp() {
			return getRuleContexts(Expr_and_tmpContext.class);
		}
		public Expr_and_tmpContext expr_and_tmp(int i) {
			return getRuleContext(Expr_and_tmpContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(ParserRTGL.OR); }
		public TerminalNode OR(int i) {
			return getToken(ParserRTGL.OR, i);
		}
		public Expr_or_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_or_tmp; }
	}

	public final Expr_or_tmpContext expr_or_tmp() throws RecognitionException {
		Expr_or_tmpContext _localctx = new Expr_or_tmpContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expr_or_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			expr_and_tmp();
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(163);
				match(OR);
				setState(164);
				expr_and_tmp();
				}
				}
				setState(169);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_or_statContext extends ParserRuleContext {
		public List<Expr_and_statContext> expr_and_stat() {
			return getRuleContexts(Expr_and_statContext.class);
		}
		public Expr_and_statContext expr_and_stat(int i) {
			return getRuleContext(Expr_and_statContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(ParserRTGL.OR); }
		public TerminalNode OR(int i) {
			return getToken(ParserRTGL.OR, i);
		}
		public Expr_or_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_or_stat; }
	}

	public final Expr_or_statContext expr_or_stat() throws RecognitionException {
		Expr_or_statContext _localctx = new Expr_or_statContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expr_or_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			expr_and_stat();
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(171);
				match(OR);
				setState(172);
				expr_and_stat();
				}
				}
				setState(177);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_and_tmpContext extends ParserRuleContext {
		public List<Expr_term_tmpContext> expr_term_tmp() {
			return getRuleContexts(Expr_term_tmpContext.class);
		}
		public Expr_term_tmpContext expr_term_tmp(int i) {
			return getRuleContext(Expr_term_tmpContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(ParserRTGL.AND); }
		public TerminalNode AND(int i) {
			return getToken(ParserRTGL.AND, i);
		}
		public Expr_and_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_and_tmp; }
	}

	public final Expr_and_tmpContext expr_and_tmp() throws RecognitionException {
		Expr_and_tmpContext _localctx = new Expr_and_tmpContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expr_and_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			expr_term_tmp();
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(179);
				match(AND);
				setState(180);
				expr_term_tmp();
				}
				}
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_and_statContext extends ParserRuleContext {
		public List<Expr_term_statContext> expr_term_stat() {
			return getRuleContexts(Expr_term_statContext.class);
		}
		public Expr_term_statContext expr_term_stat(int i) {
			return getRuleContext(Expr_term_statContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(ParserRTGL.AND); }
		public TerminalNode AND(int i) {
			return getToken(ParserRTGL.AND, i);
		}
		public Expr_and_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_and_stat; }
	}

	public final Expr_and_statContext expr_and_stat() throws RecognitionException {
		Expr_and_statContext _localctx = new Expr_and_statContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expr_and_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			expr_term_stat();
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(187);
				match(AND);
				setState(188);
				expr_term_stat();
				}
				}
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_tmpContext extends ParserRuleContext {
		public Condition_tmpContext condition_tmp() {
			return getRuleContext(Condition_tmpContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(ParserRTGL.OPEN_PAREN, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public Expr_term_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_term_tmp; }
	}

	public final Expr_term_tmpContext expr_term_tmp() throws RecognitionException {
		Expr_term_tmpContext _localctx = new Expr_term_tmpContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expr_term_tmp);
		try {
			setState(199);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(194);
				condition_tmp();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(195);
				match(OPEN_PAREN);
				setState(196);
				expr_or_tmp();
				setState(197);
				match(CLOSE_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_statContext extends ParserRuleContext {
		public Condition_statContext condition_stat() {
			return getRuleContext(Condition_statContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(ParserRTGL.OPEN_PAREN, 0); }
		public Expr_or_statContext expr_or_stat() {
			return getRuleContext(Expr_or_statContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public Expr_term_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_term_stat; }
	}

	public final Expr_term_statContext expr_term_stat() throws RecognitionException {
		Expr_term_statContext _localctx = new Expr_term_statContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_expr_term_stat);
		try {
			setState(206);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
			case ID:
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 1);
				{
				setState(201);
				condition_stat();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(202);
				match(OPEN_PAREN);
				setState(203);
				expr_or_stat();
				setState(204);
				match(CLOSE_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_tmpContext extends ParserRuleContext {
		public Aggregation_tmpContext aggregation_tmp() {
			return getRuleContext(Aggregation_tmpContext.class,0);
		}
		public Num_conditionContext num_condition() {
			return getRuleContext(Num_conditionContext.class,0);
		}
		public Str_conditionContext str_condition() {
			return getRuleContext(Str_conditionContext.class,0);
		}
		public Null_check_conditionContext null_check_condition() {
			return getRuleContext(Null_check_conditionContext.class,0);
		}
		public TerminalNode NOT() { return getToken(ParserRTGL.NOT, 0); }
		public Condition_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_tmp; }
	}

	public final Condition_tmpContext condition_tmp() throws RecognitionException {
		Condition_tmpContext _localctx = new Condition_tmpContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_condition_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(208);
				match(NOT);
				}
			}

			setState(211);
			aggregation_tmp();
			setState(215);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(212);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(213);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(214);
				null_check_condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_statContext extends ParserRuleContext {
		public Aggregation_statContext aggregation_stat() {
			return getRuleContext(Aggregation_statContext.class,0);
		}
		public Table_statContext table_stat() {
			return getRuleContext(Table_statContext.class,0);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public Num_conditionContext num_condition() {
			return getRuleContext(Num_conditionContext.class,0);
		}
		public Str_conditionContext str_condition() {
			return getRuleContext(Str_conditionContext.class,0);
		}
		public Null_check_conditionContext null_check_condition() {
			return getRuleContext(Null_check_conditionContext.class,0);
		}
		public TerminalNode NOT() { return getToken(ParserRTGL.NOT, 0); }
		public Condition_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_stat; }
	}

	public final Condition_statContext condition_stat() throws RecognitionException {
		Condition_statContext _localctx = new Condition_statContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_condition_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(217);
				match(NOT);
				}
			}

			setState(225);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
				{
				setState(220);
				aggregation_stat();
				}
				break;
			case ID:
			case SQL_INJECTION_BODY:
				{
				setState(221);
				table_stat();
				setState(222);
				match(DOT);
				setState(223);
				column();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(227);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(228);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(229);
				null_check_condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Num_conditionContext extends ParserRuleContext {
		public TerminalNode NUM_COMP_OP() { return getToken(ParserRTGL.NUM_COMP_OP, 0); }
		public TerminalNode DATETIME() { return getToken(ParserRTGL.DATETIME, 0); }
		public TerminalNode FLOAT() { return getToken(ParserRTGL.FLOAT, 0); }
		public TerminalNode INT() { return getToken(ParserRTGL.INT, 0); }
		public Num_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num_condition; }
	}

	public final Num_conditionContext num_condition() throws RecognitionException {
		Num_conditionContext _localctx = new Num_conditionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_num_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(NUM_COMP_OP);
			setState(233);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 246290604621824L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Str_conditionContext extends ParserRuleContext {
		public TerminalNode STR_COMP_OP() { return getToken(ParserRTGL.STR_COMP_OP, 0); }
		public TerminalNode STRING() { return getToken(ParserRTGL.STRING, 0); }
		public Str_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str_condition; }
	}

	public final Str_conditionContext str_condition() throws RecognitionException {
		Str_conditionContext _localctx = new Str_conditionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_str_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(STR_COMP_OP);
			setState(236);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Null_check_conditionContext extends ParserRuleContext {
		public TerminalNode NULL_CHECK_OP() { return getToken(ParserRTGL.NULL_CHECK_OP, 0); }
		public Null_check_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_null_check_condition; }
	}

	public final Null_check_conditionContext null_check_condition() throws RecognitionException {
		Null_check_conditionContext _localctx = new Null_check_conditionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_null_check_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(NULL_CHECK_OP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Aggregation_tmpContext extends ParserRuleContext {
		public TerminalNode AGGR_FUNC() { return getToken(ParserRTGL.AGGR_FUNC, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserRTGL.OPEN_PAREN, 0); }
		public Table_tmpContext table_tmp() {
			return getRuleContext(Table_tmpContext.class,0);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserRTGL.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserRTGL.COMMA, i);
		}
		public List<TerminalNode> INT() { return getTokens(ParserRTGL.INT); }
		public TerminalNode INT(int i) {
			return getToken(ParserRTGL.INT, i);
		}
		public TerminalNode TIME_MEASURE_UNIT() { return getToken(ParserRTGL.TIME_MEASURE_UNIT, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public Aggregation_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregation_tmp; }
	}

	public final Aggregation_tmpContext aggregation_tmp() throws RecognitionException {
		Aggregation_tmpContext _localctx = new Aggregation_tmpContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_aggregation_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(AGGR_FUNC);
			setState(241);
			match(OPEN_PAREN);
			setState(242);
			table_tmp();
			setState(243);
			match(DOT);
			setState(244);
			column();
			setState(246);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(245);
				where_stat();
				}
			}

			setState(248);
			match(COMMA);
			setState(249);
			match(INT);
			setState(250);
			match(COMMA);
			setState(251);
			match(INT);
			setState(252);
			match(COMMA);
			setState(253);
			match(TIME_MEASURE_UNIT);
			setState(254);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Aggregation_statContext extends ParserRuleContext {
		public TerminalNode AGGR_FUNC() { return getToken(ParserRTGL.AGGR_FUNC, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserRTGL.OPEN_PAREN, 0); }
		public Table_statContext table_stat() {
			return getRuleContext(Table_statContext.class,0);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public Aggregation_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregation_stat; }
	}

	public final Aggregation_statContext aggregation_stat() throws RecognitionException {
		Aggregation_statContext _localctx = new Aggregation_statContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_aggregation_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			match(AGGR_FUNC);
			setState(257);
			match(OPEN_PAREN);
			setState(258);
			table_stat();
			setState(259);
			match(DOT);
			setState(260);
			column();
			setState(262);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(261);
				where_stat();
				}
			}

			setState(264);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Sql_injection_tmpContext extends ParserRuleContext {
		public Token table_name;
		public Token pkey_col;
		public Token time_col;
		public TerminalNode SQL_INJECTION_BODY() { return getToken(ParserRTGL.SQL_INJECTION_BODY, 0); }
		public List<TerminalNode> OPEN_BRACE() { return getTokens(ParserRTGL.OPEN_BRACE); }
		public TerminalNode OPEN_BRACE(int i) {
			return getToken(ParserRTGL.OPEN_BRACE, i);
		}
		public List<TerminalNode> CLOSE_BRACE() { return getTokens(ParserRTGL.CLOSE_BRACE); }
		public TerminalNode CLOSE_BRACE(int i) {
			return getToken(ParserRTGL.CLOSE_BRACE, i);
		}
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public List<Fkey_col_to_pkey_tableContext> fkey_col_to_pkey_table() {
			return getRuleContexts(Fkey_col_to_pkey_tableContext.class);
		}
		public Fkey_col_to_pkey_tableContext fkey_col_to_pkey_table(int i) {
			return getRuleContext(Fkey_col_to_pkey_tableContext.class,i);
		}
		public List<Id_dot_idContext> id_dot_id() {
			return getRuleContexts(Id_dot_idContext.class);
		}
		public Id_dot_idContext id_dot_id(int i) {
			return getRuleContext(Id_dot_idContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserRTGL.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserRTGL.COMMA, i);
		}
		public Sql_injection_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sql_injection_tmp; }
	}

	public final Sql_injection_tmpContext sql_injection_tmp() throws RecognitionException {
		Sql_injection_tmpContext _localctx = new Sql_injection_tmpContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_sql_injection_tmp);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			match(SQL_INJECTION_BODY);
			setState(267);
			match(OPEN_BRACE);
			setState(268);
			((Sql_injection_tmpContext)_localctx).table_name = match(ID);
			setState(269);
			match(CLOSE_BRACE);
			setState(270);
			match(OPEN_BRACE);
			setState(272);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(271);
				((Sql_injection_tmpContext)_localctx).pkey_col = match(ID);
				}
			}

			setState(274);
			match(CLOSE_BRACE);
			setState(275);
			match(OPEN_BRACE);
			setState(285);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(281);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(276);
						fkey_col_to_pkey_table();
						setState(277);
						match(COMMA);
						}
						} 
					}
					setState(283);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
				}
				setState(284);
				fkey_col_to_pkey_table();
				}
			}

			setState(287);
			match(CLOSE_BRACE);
			setState(288);
			match(OPEN_BRACE);
			setState(298);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(294);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(289);
						id_dot_id();
						setState(290);
						match(COMMA);
						}
						} 
					}
					setState(296);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
				}
				setState(297);
				id_dot_id();
				}
			}

			setState(300);
			match(CLOSE_BRACE);
			setState(301);
			match(OPEN_BRACE);
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(302);
				((Sql_injection_tmpContext)_localctx).time_col = match(ID);
				}
			}

			setState(305);
			match(CLOSE_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Sql_injection_statContext extends ParserRuleContext {
		public Token table_name;
		public Token pkey_col;
		public TerminalNode SQL_INJECTION_BODY() { return getToken(ParserRTGL.SQL_INJECTION_BODY, 0); }
		public List<TerminalNode> OPEN_BRACE() { return getTokens(ParserRTGL.OPEN_BRACE); }
		public TerminalNode OPEN_BRACE(int i) {
			return getToken(ParserRTGL.OPEN_BRACE, i);
		}
		public List<TerminalNode> CLOSE_BRACE() { return getTokens(ParserRTGL.CLOSE_BRACE); }
		public TerminalNode CLOSE_BRACE(int i) {
			return getToken(ParserRTGL.CLOSE_BRACE, i);
		}
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public List<Fkey_col_to_pkey_tableContext> fkey_col_to_pkey_table() {
			return getRuleContexts(Fkey_col_to_pkey_tableContext.class);
		}
		public Fkey_col_to_pkey_tableContext fkey_col_to_pkey_table(int i) {
			return getRuleContext(Fkey_col_to_pkey_tableContext.class,i);
		}
		public List<Id_dot_idContext> id_dot_id() {
			return getRuleContexts(Id_dot_idContext.class);
		}
		public Id_dot_idContext id_dot_id(int i) {
			return getRuleContext(Id_dot_idContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserRTGL.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserRTGL.COMMA, i);
		}
		public Sql_injection_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sql_injection_stat; }
	}

	public final Sql_injection_statContext sql_injection_stat() throws RecognitionException {
		Sql_injection_statContext _localctx = new Sql_injection_statContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_sql_injection_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(SQL_INJECTION_BODY);
			setState(308);
			match(OPEN_BRACE);
			setState(309);
			((Sql_injection_statContext)_localctx).table_name = match(ID);
			setState(310);
			match(CLOSE_BRACE);
			setState(311);
			match(OPEN_BRACE);
			setState(313);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(312);
				((Sql_injection_statContext)_localctx).pkey_col = match(ID);
				}
			}

			setState(315);
			match(CLOSE_BRACE);
			setState(316);
			match(OPEN_BRACE);
			setState(325);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(317);
				fkey_col_to_pkey_table();
				setState(322);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(318);
					match(COMMA);
					setState(319);
					fkey_col_to_pkey_table();
					}
					}
					setState(324);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(327);
			match(CLOSE_BRACE);
			setState(328);
			match(OPEN_BRACE);
			setState(337);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(329);
				id_dot_id();
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(330);
					match(COMMA);
					setState(331);
					id_dot_id();
					}
					}
					setState(336);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(339);
			match(CLOSE_BRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Fkey_col_to_pkey_tableContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode ARROW() { return getToken(ParserRTGL.ARROW, 0); }
		public Fkey_col_to_pkey_tableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fkey_col_to_pkey_table; }
	}

	public final Fkey_col_to_pkey_tableContext fkey_col_to_pkey_table() throws RecognitionException {
		Fkey_col_to_pkey_tableContext _localctx = new Fkey_col_to_pkey_tableContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_fkey_col_to_pkey_table);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			match(ID);
			setState(342);
			match(ARROW);
			setState(343);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Table_tmpContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ParserRTGL.ID, 0); }
		public Sql_injection_tmpContext sql_injection_tmp() {
			return getRuleContext(Sql_injection_tmpContext.class,0);
		}
		public Table_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table_tmp; }
	}

	public final Table_tmpContext table_tmp() throws RecognitionException {
		Table_tmpContext _localctx = new Table_tmpContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_table_tmp);
		try {
			setState(347);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(345);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 2);
				{
				setState(346);
				sql_injection_tmp();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Table_statContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ParserRTGL.ID, 0); }
		public Sql_injection_statContext sql_injection_stat() {
			return getRuleContext(Sql_injection_statContext.class,0);
		}
		public Table_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table_stat; }
	}

	public final Table_statContext table_stat() throws RecognitionException {
		Table_statContext _localctx = new Table_statContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_table_stat);
		try {
			setState(351);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(349);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 2);
				{
				setState(350);
				sql_injection_stat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ColumnContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ParserRTGL.ID, 0); }
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public ColumnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_column; }
	}

	public final ColumnContext column() throws RecognitionException {
		ColumnContext _localctx = new ColumnContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_column);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Id_dot_idContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public Id_dot_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_dot_id; }
	}

	public final Id_dot_idContext id_dot_id() throws RecognitionException {
		Id_dot_idContext _localctx = new Id_dot_idContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_id_dot_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			match(ID);
			setState(356);
			match(DOT);
			setState(357);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00015\u0168\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0001\u0000\u0001\u0000\u0003\u0000C\b\u0000"+
		"\u0001\u0001\u0003\u0001F\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001K\b\u0001\u0001\u0001\u0003\u0001N\b\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0003\u0002S\b\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002X\b\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0005\u0003`\b\u0003\n\u0003\f\u0003c\t"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0004\u0004k\b\u0004\u000b\u0004\f\u0004l\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"v\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006}\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007\u0084\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"\u0088\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u008f\b"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0098"+
		"\b\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u00a6\b\f\n\f\f\f\u00a9"+
		"\t\f\u0001\r\u0001\r\u0001\r\u0005\r\u00ae\b\r\n\r\f\r\u00b1\t\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00b6\b\u000e\n\u000e\f\u000e"+
		"\u00b9\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00be\b"+
		"\u000f\n\u000f\f\u000f\u00c1\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0003\u0010\u00c8\b\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00cf\b\u0011\u0001\u0012"+
		"\u0003\u0012\u00d2\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0003\u0012\u00d8\b\u0012\u0001\u0013\u0003\u0013\u00db\b\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00e2"+
		"\b\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00e7\b\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u00f7\b\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u0107\b\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u0111\b\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019"+
		"\u0118\b\u0019\n\u0019\f\u0019\u011b\t\u0019\u0001\u0019\u0003\u0019\u011e"+
		"\b\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005"+
		"\u0019\u0125\b\u0019\n\u0019\f\u0019\u0128\t\u0019\u0001\u0019\u0003\u0019"+
		"\u012b\b\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u0130\b"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u013a\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u0141\b\u001a\n"+
		"\u001a\f\u001a\u0144\t\u001a\u0003\u001a\u0146\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u014d\b\u001a\n"+
		"\u001a\f\u001a\u0150\t\u001a\u0003\u001a\u0152\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0003\u001c\u015c\b\u001c\u0001\u001d\u0001\u001d\u0003\u001d\u0160"+
		"\b\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0000\u0000 \u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>\u0000\u0002"+
		"\u0001\u0000-/\u0002\u0000&&22\u0174\u0000B\u0001\u0000\u0000\u0000\u0002"+
		"E\u0001\u0000\u0000\u0000\u0004R\u0001\u0000\u0000\u0000\u0006[\u0001"+
		"\u0000\u0000\u0000\bd\u0001\u0000\u0000\u0000\np\u0001\u0000\u0000\u0000"+
		"\fw\u0001\u0000\u0000\u0000\u000e\u0087\u0001\u0000\u0000\u0000\u0010"+
		"\u0097\u0001\u0000\u0000\u0000\u0012\u0099\u0001\u0000\u0000\u0000\u0014"+
		"\u009c\u0001\u0000\u0000\u0000\u0016\u009f\u0001\u0000\u0000\u0000\u0018"+
		"\u00a2\u0001\u0000\u0000\u0000\u001a\u00aa\u0001\u0000\u0000\u0000\u001c"+
		"\u00b2\u0001\u0000\u0000\u0000\u001e\u00ba\u0001\u0000\u0000\u0000 \u00c7"+
		"\u0001\u0000\u0000\u0000\"\u00ce\u0001\u0000\u0000\u0000$\u00d1\u0001"+
		"\u0000\u0000\u0000&\u00da\u0001\u0000\u0000\u0000(\u00e8\u0001\u0000\u0000"+
		"\u0000*\u00eb\u0001\u0000\u0000\u0000,\u00ee\u0001\u0000\u0000\u0000."+
		"\u00f0\u0001\u0000\u0000\u00000\u0100\u0001\u0000\u0000\u00002\u010a\u0001"+
		"\u0000\u0000\u00004\u0133\u0001\u0000\u0000\u00006\u0155\u0001\u0000\u0000"+
		"\u00008\u015b\u0001\u0000\u0000\u0000:\u015f\u0001\u0000\u0000\u0000<"+
		"\u0161\u0001\u0000\u0000\u0000>\u0163\u0001\u0000\u0000\u0000@C\u0003"+
		"\u0002\u0001\u0000AC\u0003\u0004\u0002\u0000B@\u0001\u0000\u0000\u0000"+
		"BA\u0001\u0000\u0000\u0000C\u0001\u0001\u0000\u0000\u0000DF\u0003\u0006"+
		"\u0003\u0000ED\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FG\u0001"+
		"\u0000\u0000\u0000GH\u0003\u000e\u0007\u0000HJ\u0003\n\u0005\u0000IK\u0003"+
		"\u0012\t\u0000JI\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KM\u0001"+
		"\u0000\u0000\u0000LN\u0003\u0016\u000b\u0000ML\u0001\u0000\u0000\u0000"+
		"MN\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OP\u0005\'\u0000\u0000"+
		"P\u0003\u0001\u0000\u0000\u0000QS\u0003\u0006\u0003\u0000RQ\u0001\u0000"+
		"\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TU\u0003"+
		"\u0010\b\u0000UW\u0003\f\u0006\u0000VX\u0003\u0014\n\u0000WV\u0001\u0000"+
		"\u0000\u0000WX\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0005"+
		"\'\u0000\u0000Z\u0005\u0001\u0000\u0000\u0000[\\\u0005\u0001\u0000\u0000"+
		"\\a\u0003\b\u0004\u0000]^\u0005\u001f\u0000\u0000^`\u0003\b\u0004\u0000"+
		"_]\u0001\u0000\u0000\u0000`c\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000"+
		"\u0000ab\u0001\u0000\u0000\u0000b\u0007\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000de\u00052\u0000\u0000ef\u0005\u0006\u0000\u0000fg\u0005"+
		" \u0000\u0000gj\u0003>\u001f\u0000hi\u0005(\u0000\u0000ik\u0003>\u001f"+
		"\u0000jh\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000lj\u0001\u0000"+
		"\u0000\u0000lm\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000no\u0005"+
		"!\u0000\u0000o\t\u0001\u0000\u0000\u0000pq\u0005\u0002\u0000\u0000qr\u0003"+
		"8\u001c\u0000rs\u0005\u001e\u0000\u0000su\u0003<\u001e\u0000tv\u0003\u0014"+
		"\n\u0000ut\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000v\u000b\u0001"+
		"\u0000\u0000\u0000wx\u0005\u0002\u0000\u0000xy\u0003:\u001d\u0000yz\u0005"+
		"\u001e\u0000\u0000z|\u0003<\u001e\u0000{}\u0003\u0014\n\u0000|{\u0001"+
		"\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\r\u0001\u0000\u0000\u0000"+
		"~\u007f\u0005\u0003\u0000\u0000\u007f\u0083\u0003.\u0017\u0000\u0080\u0081"+
		"\u0005\b\u0000\u0000\u0081\u0084\u0005/\u0000\u0000\u0082\u0084\u0005"+
		"\u0007\u0000\u0000\u0083\u0080\u0001\u0000\u0000\u0000\u0083\u0082\u0001"+
		"\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0088\u0001"+
		"\u0000\u0000\u0000\u0085\u0086\u0005\u0003\u0000\u0000\u0086\u0088\u0003"+
		"\u0018\f\u0000\u0087~\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000"+
		"\u0000\u0000\u0088\u000f\u0001\u0000\u0000\u0000\u0089\u008a\u0005\u0003"+
		"\u0000\u0000\u008a\u008e\u00030\u0018\u0000\u008b\u008c\u0005\b\u0000"+
		"\u0000\u008c\u008f\u0005/\u0000\u0000\u008d\u008f\u0005\u0007\u0000\u0000"+
		"\u008e\u008b\u0001\u0000\u0000\u0000\u008e\u008d\u0001\u0000\u0000\u0000"+
		"\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0098\u0001\u0000\u0000\u0000"+
		"\u0090\u0091\u0005\u0003\u0000\u0000\u0091\u0098\u0003\u001a\r\u0000\u0092"+
		"\u0093\u0005\u0003\u0000\u0000\u0093\u0094\u0003:\u001d\u0000\u0094\u0095"+
		"\u0005\u001e\u0000\u0000\u0095\u0096\u0003<\u001e\u0000\u0096\u0098\u0001"+
		"\u0000\u0000\u0000\u0097\u0089\u0001\u0000\u0000\u0000\u0097\u0090\u0001"+
		"\u0000\u0000\u0000\u0097\u0092\u0001\u0000\u0000\u0000\u0098\u0011\u0001"+
		"\u0000\u0000\u0000\u0099\u009a\u0005\u0004\u0000\u0000\u009a\u009b\u0003"+
		"\u0018\f\u0000\u009b\u0013\u0001\u0000\u0000\u0000\u009c\u009d\u0005\u0004"+
		"\u0000\u0000\u009d\u009e\u0003\u001a\r\u0000\u009e\u0015\u0001\u0000\u0000"+
		"\u0000\u009f\u00a0\u0005\u0005\u0000\u0000\u00a0\u00a1\u0003\u0018\f\u0000"+
		"\u00a1\u0017\u0001\u0000\u0000\u0000\u00a2\u00a7\u0003\u001c\u000e\u0000"+
		"\u00a3\u00a4\u0005+\u0000\u0000\u00a4\u00a6\u0003\u001c\u000e\u0000\u00a5"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8"+
		"\u0019\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00aa"+
		"\u00af\u0003\u001e\u000f\u0000\u00ab\u00ac\u0005+\u0000\u0000\u00ac\u00ae"+
		"\u0003\u001e\u000f\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000\u00ae\u00b1"+
		"\u0001\u0000\u0000\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af\u00b0"+
		"\u0001\u0000\u0000\u0000\u00b0\u001b\u0001\u0000\u0000\u0000\u00b1\u00af"+
		"\u0001\u0000\u0000\u0000\u00b2\u00b7\u0003 \u0010\u0000\u00b3\u00b4\u0005"+
		"*\u0000\u0000\u00b4\u00b6\u0003 \u0010\u0000\u00b5\u00b3\u0001\u0000\u0000"+
		"\u0000\u00b6\u00b9\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u001d\u0001\u0000\u0000"+
		"\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00ba\u00bf\u0003\"\u0011\u0000"+
		"\u00bb\u00bc\u0005*\u0000\u0000\u00bc\u00be\u0003\"\u0011\u0000\u00bd"+
		"\u00bb\u0001\u0000\u0000\u0000\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf"+
		"\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0"+
		"\u001f\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2"+
		"\u00c8\u0003$\u0012\u0000\u00c3\u00c4\u0005 \u0000\u0000\u00c4\u00c5\u0003"+
		"\u0018\f\u0000\u00c5\u00c6\u0005!\u0000\u0000\u00c6\u00c8\u0001\u0000"+
		"\u0000\u0000\u00c7\u00c2\u0001\u0000\u0000\u0000\u00c7\u00c3\u0001\u0000"+
		"\u0000\u0000\u00c8!\u0001\u0000\u0000\u0000\u00c9\u00cf\u0003&\u0013\u0000"+
		"\u00ca\u00cb\u0005 \u0000\u0000\u00cb\u00cc\u0003\u001a\r\u0000\u00cc"+
		"\u00cd\u0005!\u0000\u0000\u00cd\u00cf\u0001\u0000\u0000\u0000\u00ce\u00c9"+
		"\u0001\u0000\u0000\u0000\u00ce\u00ca\u0001\u0000\u0000\u0000\u00cf#\u0001"+
		"\u0000\u0000\u0000\u00d0\u00d2\u0005,\u0000\u0000\u00d1\u00d0\u0001\u0000"+
		"\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0001\u0000"+
		"\u0000\u0000\u00d3\u00d7\u0003.\u0017\u0000\u00d4\u00d8\u0003(\u0014\u0000"+
		"\u00d5\u00d8\u0003*\u0015\u0000\u00d6\u00d8\u0003,\u0016\u0000\u00d7\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001\u0000\u0000\u0000\u00d7\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d8%\u0001\u0000\u0000\u0000\u00d9\u00db\u0005"+
		",\u0000\u0000\u00da\u00d9\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000"+
		"\u0000\u0000\u00db\u00e1\u0001\u0000\u0000\u0000\u00dc\u00e2\u00030\u0018"+
		"\u0000\u00dd\u00de\u0003:\u001d\u0000\u00de\u00df\u0005\u001e\u0000\u0000"+
		"\u00df\u00e0\u0003<\u001e\u0000\u00e0\u00e2\u0001\u0000\u0000\u0000\u00e1"+
		"\u00dc\u0001\u0000\u0000\u0000\u00e1\u00dd\u0001\u0000\u0000\u0000\u00e2"+
		"\u00e6\u0001\u0000\u0000\u0000\u00e3\u00e7\u0003(\u0014\u0000\u00e4\u00e7"+
		"\u0003*\u0015\u0000\u00e5\u00e7\u0003,\u0016\u0000\u00e6\u00e3\u0001\u0000"+
		"\u0000\u0000\u00e6\u00e4\u0001\u0000\u0000\u0000\u00e6\u00e5\u0001\u0000"+
		"\u0000\u0000\u00e7\'\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005\u0013\u0000"+
		"\u0000\u00e9\u00ea\u0007\u0000\u0000\u0000\u00ea)\u0001\u0000\u0000\u0000"+
		"\u00eb\u00ec\u0005\u0014\u0000\u0000\u00ec\u00ed\u00051\u0000\u0000\u00ed"+
		"+\u0001\u0000\u0000\u0000\u00ee\u00ef\u0005\u001b\u0000\u0000\u00ef-\u0001"+
		"\u0000\u0000\u0000\u00f0\u00f1\u0005\t\u0000\u0000\u00f1\u00f2\u0005 "+
		"\u0000\u0000\u00f2\u00f3\u00038\u001c\u0000\u00f3\u00f4\u0005\u001e\u0000"+
		"\u0000\u00f4\u00f6\u0003<\u001e\u0000\u00f5\u00f7\u0003\u0014\n\u0000"+
		"\u00f6\u00f5\u0001\u0000\u0000\u0000\u00f6\u00f7\u0001\u0000\u0000\u0000"+
		"\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u00f9\u0005\u001f\u0000\u0000"+
		"\u00f9\u00fa\u0005/\u0000\u0000\u00fa\u00fb\u0005\u001f\u0000\u0000\u00fb"+
		"\u00fc\u0005/\u0000\u0000\u00fc\u00fd\u0005\u001f\u0000\u0000\u00fd\u00fe"+
		"\u00050\u0000\u0000\u00fe\u00ff\u0005!\u0000\u0000\u00ff/\u0001\u0000"+
		"\u0000\u0000\u0100\u0101\u0005\t\u0000\u0000\u0101\u0102\u0005 \u0000"+
		"\u0000\u0102\u0103\u0003:\u001d\u0000\u0103\u0104\u0005\u001e\u0000\u0000"+
		"\u0104\u0106\u0003<\u001e\u0000\u0105\u0107\u0003\u0014\n\u0000\u0106"+
		"\u0105\u0001\u0000\u0000\u0000\u0106\u0107\u0001\u0000\u0000\u0000\u0107"+
		"\u0108\u0001\u0000\u0000\u0000\u0108\u0109\u0005!\u0000\u0000\u01091\u0001"+
		"\u0000\u0000\u0000\u010a\u010b\u00053\u0000\u0000\u010b\u010c\u0005$\u0000"+
		"\u0000\u010c\u010d\u00052\u0000\u0000\u010d\u010e\u0005%\u0000\u0000\u010e"+
		"\u0110\u0005$\u0000\u0000\u010f\u0111\u00052\u0000\u0000\u0110\u010f\u0001"+
		"\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111\u0112\u0001"+
		"\u0000\u0000\u0000\u0112\u0113\u0005%\u0000\u0000\u0113\u011d\u0005$\u0000"+
		"\u0000\u0114\u0115\u00036\u001b\u0000\u0115\u0116\u0005\u001f\u0000\u0000"+
		"\u0116\u0118\u0001\u0000\u0000\u0000\u0117\u0114\u0001\u0000\u0000\u0000"+
		"\u0118\u011b\u0001\u0000\u0000\u0000\u0119\u0117\u0001\u0000\u0000\u0000"+
		"\u0119\u011a\u0001\u0000\u0000\u0000\u011a\u011c\u0001\u0000\u0000\u0000"+
		"\u011b\u0119\u0001\u0000\u0000\u0000\u011c\u011e\u00036\u001b\u0000\u011d"+
		"\u0119\u0001\u0000\u0000\u0000\u011d\u011e\u0001\u0000\u0000\u0000\u011e"+
		"\u011f\u0001\u0000\u0000\u0000\u011f\u0120\u0005%\u0000\u0000\u0120\u012a"+
		"\u0005$\u0000\u0000\u0121\u0122\u0003>\u001f\u0000\u0122\u0123\u0005\u001f"+
		"\u0000\u0000\u0123\u0125\u0001\u0000\u0000\u0000\u0124\u0121\u0001\u0000"+
		"\u0000\u0000\u0125\u0128\u0001\u0000\u0000\u0000\u0126\u0124\u0001\u0000"+
		"\u0000\u0000\u0126\u0127\u0001\u0000\u0000\u0000\u0127\u0129\u0001\u0000"+
		"\u0000\u0000\u0128\u0126\u0001\u0000\u0000\u0000\u0129\u012b\u0003>\u001f"+
		"\u0000\u012a\u0126\u0001\u0000\u0000\u0000\u012a\u012b\u0001\u0000\u0000"+
		"\u0000\u012b\u012c\u0001\u0000\u0000\u0000\u012c\u012d\u0005%\u0000\u0000"+
		"\u012d\u012f\u0005$\u0000\u0000\u012e\u0130\u00052\u0000\u0000\u012f\u012e"+
		"\u0001\u0000\u0000\u0000\u012f\u0130\u0001\u0000\u0000\u0000\u0130\u0131"+
		"\u0001\u0000\u0000\u0000\u0131\u0132\u0005%\u0000\u0000\u01323\u0001\u0000"+
		"\u0000\u0000\u0133\u0134\u00053\u0000\u0000\u0134\u0135\u0005$\u0000\u0000"+
		"\u0135\u0136\u00052\u0000\u0000\u0136\u0137\u0005%\u0000\u0000\u0137\u0139"+
		"\u0005$\u0000\u0000\u0138\u013a\u00052\u0000\u0000\u0139\u0138\u0001\u0000"+
		"\u0000\u0000\u0139\u013a\u0001\u0000\u0000\u0000\u013a\u013b\u0001\u0000"+
		"\u0000\u0000\u013b\u013c\u0005%\u0000\u0000\u013c\u0145\u0005$\u0000\u0000"+
		"\u013d\u0142\u00036\u001b\u0000\u013e\u013f\u0005\u001f\u0000\u0000\u013f"+
		"\u0141\u00036\u001b\u0000\u0140\u013e\u0001\u0000\u0000\u0000\u0141\u0144"+
		"\u0001\u0000\u0000\u0000\u0142\u0140\u0001\u0000\u0000\u0000\u0142\u0143"+
		"\u0001\u0000\u0000\u0000\u0143\u0146\u0001\u0000\u0000\u0000\u0144\u0142"+
		"\u0001\u0000\u0000\u0000\u0145\u013d\u0001\u0000\u0000\u0000\u0145\u0146"+
		"\u0001\u0000\u0000\u0000\u0146\u0147\u0001\u0000\u0000\u0000\u0147\u0148"+
		"\u0005%\u0000\u0000\u0148\u0151\u0005$\u0000\u0000\u0149\u014e\u0003>"+
		"\u001f\u0000\u014a\u014b\u0005\u001f\u0000\u0000\u014b\u014d\u0003>\u001f"+
		"\u0000\u014c\u014a\u0001\u0000\u0000\u0000\u014d\u0150\u0001\u0000\u0000"+
		"\u0000\u014e\u014c\u0001\u0000\u0000\u0000\u014e\u014f\u0001\u0000\u0000"+
		"\u0000\u014f\u0152\u0001\u0000\u0000\u0000\u0150\u014e\u0001\u0000\u0000"+
		"\u0000\u0151\u0149\u0001\u0000\u0000\u0000\u0151\u0152\u0001\u0000\u0000"+
		"\u0000\u0152\u0153\u0001\u0000\u0000\u0000\u0153\u0154\u0005%\u0000\u0000"+
		"\u01545\u0001\u0000\u0000\u0000\u0155\u0156\u00052\u0000\u0000\u0156\u0157"+
		"\u0005(\u0000\u0000\u0157\u0158\u00052\u0000\u0000\u01587\u0001\u0000"+
		"\u0000\u0000\u0159\u015c\u00052\u0000\u0000\u015a\u015c\u00032\u0019\u0000"+
		"\u015b\u0159\u0001\u0000\u0000\u0000\u015b\u015a\u0001\u0000\u0000\u0000"+
		"\u015c9\u0001\u0000\u0000\u0000\u015d\u0160\u00052\u0000\u0000\u015e\u0160"+
		"\u00034\u001a\u0000\u015f\u015d\u0001\u0000\u0000\u0000\u015f\u015e\u0001"+
		"\u0000\u0000\u0000\u0160;\u0001\u0000\u0000\u0000\u0161\u0162\u0007\u0001"+
		"\u0000\u0000\u0162=\u0001\u0000\u0000\u0000\u0163\u0164\u00052\u0000\u0000"+
		"\u0164\u0165\u0005\u001e\u0000\u0000\u0165\u0166\u00052\u0000\u0000\u0166"+
		"?\u0001\u0000\u0000\u0000(BEJMRWalu|\u0083\u0087\u008e\u0097\u00a7\u00af"+
		"\u00b7\u00bf\u00c7\u00ce\u00d1\u00d7\u00da\u00e1\u00e6\u00f6\u0106\u0110"+
		"\u0119\u011d\u0126\u012a\u012f\u0139\u0142\u0145\u014e\u0151\u015b\u015f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}