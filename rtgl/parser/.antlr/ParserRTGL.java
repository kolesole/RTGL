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
		RULE_path_node = 27, RULE_fkey_col_to_pkey_table = 28, RULE_fkey_table_to_fkey_col = 29, 
		RULE_table_tmp = 30, RULE_table_stat = 31, RULE_column = 32;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "query_tmp", "query_stat", "common_path_exprs", "common_path_expr", 
			"for_each_tmp", "for_each_stat", "predict_tmp", "predict_stat", "where_tmp", 
			"where_stat", "assuming", "expr_or_tmp", "expr_or_stat", "expr_and_tmp", 
			"expr_and_stat", "expr_term_tmp", "expr_term_stat", "condition_tmp", 
			"condition_stat", "num_condition", "str_condition", "null_check_condition", 
			"aggregation_tmp", "aggregation_stat", "sql_injection_tmp", "sql_injection_stat", 
			"path_node", "fkey_col_to_pkey_table", "fkey_table_to_fkey_col", "table_tmp", 
			"table_stat", "column"
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
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				query_tmp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(67);
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
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(70);
				common_path_exprs();
				}
			}

			setState(73);
			predict_tmp();
			setState(74);
			for_each_tmp();
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(75);
				where_tmp();
				}
			}

			setState(79);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSUMING) {
				{
				setState(78);
				assuming();
				}
			}

			setState(81);
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
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(83);
				common_path_exprs();
				}
			}

			setState(86);
			predict_stat();
			setState(87);
			for_each_stat();
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(88);
				where_stat();
				}
			}

			setState(91);
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
			setState(93);
			match(WITH);
			setState(94);
			common_path_expr();
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(95);
				match(COMMA);
				setState(96);
				common_path_expr();
				}
				}
				setState(101);
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
		public Token path_name;
		public Path_nodeContext path_node;
		public List<Path_nodeContext> steps = new ArrayList<Path_nodeContext>();
		public TerminalNode AS() { return getToken(ParserRTGL.AS, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserRTGL.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public TerminalNode ID() { return getToken(ParserRTGL.ID, 0); }
		public List<Path_nodeContext> path_node() {
			return getRuleContexts(Path_nodeContext.class);
		}
		public Path_nodeContext path_node(int i) {
			return getRuleContext(Path_nodeContext.class,i);
		}
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
			setState(102);
			((Common_path_exprContext)_localctx).path_name = match(ID);
			setState(103);
			match(AS);
			setState(104);
			match(OPEN_PAREN);
			setState(105);
			((Common_path_exprContext)_localctx).path_node = path_node();
			((Common_path_exprContext)_localctx).steps.add(((Common_path_exprContext)_localctx).path_node);
			setState(108); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(106);
				match(ARROW);
				setState(107);
				((Common_path_exprContext)_localctx).path_node = path_node();
				((Common_path_exprContext)_localctx).steps.add(((Common_path_exprContext)_localctx).path_node);
				}
				}
				setState(110); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ARROW );
			setState(112);
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
			setState(114);
			match(FOR_EACH);
			setState(115);
			table_tmp();
			setState(116);
			match(DOT);
			setState(117);
			column();
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(118);
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
			setState(121);
			match(FOR_EACH);
			setState(122);
			table_stat();
			setState(123);
			match(DOT);
			setState(124);
			column();
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(125);
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
			setState(137);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(128);
				match(PREDICT);
				setState(129);
				aggregation_tmp();
				setState(133);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(130);
					match(RANK_TOP);
					setState(131);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(132);
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
				setState(135);
				match(PREDICT);
				setState(136);
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
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				match(PREDICT);
				setState(140);
				aggregation_stat();
				setState(144);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(141);
					match(RANK_TOP);
					setState(142);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(143);
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
				setState(146);
				match(PREDICT);
				setState(147);
				expr_or_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(148);
				match(PREDICT);
				setState(149);
				table_stat();
				setState(150);
				match(DOT);
				setState(151);
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
			setState(155);
			match(WHERE);
			setState(156);
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
			setState(158);
			match(WHERE);
			setState(159);
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
			setState(161);
			match(ASSUMING);
			setState(162);
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
			setState(164);
			expr_and_tmp();
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(165);
				match(OR);
				setState(166);
				expr_and_tmp();
				}
				}
				setState(171);
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
			setState(172);
			expr_and_stat();
			setState(177);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(173);
				match(OR);
				setState(174);
				expr_and_stat();
				}
				}
				setState(179);
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
			setState(180);
			expr_term_tmp();
			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(181);
				match(AND);
				setState(182);
				expr_term_tmp();
				}
				}
				setState(187);
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
			setState(188);
			expr_term_stat();
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(189);
				match(AND);
				setState(190);
				expr_term_stat();
				}
				}
				setState(195);
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
			setState(201);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				condition_tmp();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(197);
				match(OPEN_PAREN);
				setState(198);
				expr_or_tmp();
				setState(199);
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
			setState(208);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
			case ID:
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 1);
				{
				setState(203);
				condition_stat();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(204);
				match(OPEN_PAREN);
				setState(205);
				expr_or_stat();
				setState(206);
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
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(210);
				match(NOT);
				}
			}

			setState(213);
			aggregation_tmp();
			setState(217);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(214);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(215);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(216);
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
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(219);
				match(NOT);
				}
			}

			setState(227);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
				{
				setState(222);
				aggregation_stat();
				}
				break;
			case ID:
			case SQL_INJECTION_BODY:
				{
				setState(223);
				table_stat();
				setState(224);
				match(DOT);
				setState(225);
				column();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(229);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(230);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(231);
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
			setState(234);
			match(NUM_COMP_OP);
			setState(235);
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
			setState(237);
			match(STR_COMP_OP);
			setState(238);
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
			setState(240);
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
		public Token start;
		public Token end;
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
		public TerminalNode TIME_MEASURE_UNIT() { return getToken(ParserRTGL.TIME_MEASURE_UNIT, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public List<TerminalNode> INT() { return getTokens(ParserRTGL.INT); }
		public TerminalNode INT(int i) {
			return getToken(ParserRTGL.INT, i);
		}
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
			setState(242);
			match(AGGR_FUNC);
			setState(243);
			match(OPEN_PAREN);
			setState(244);
			table_tmp();
			setState(245);
			match(DOT);
			setState(246);
			column();
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(247);
				where_stat();
				}
			}

			setState(250);
			match(COMMA);
			setState(251);
			((Aggregation_tmpContext)_localctx).start = match(INT);
			setState(252);
			match(COMMA);
			setState(253);
			((Aggregation_tmpContext)_localctx).end = match(INT);
			setState(254);
			match(COMMA);
			setState(255);
			match(TIME_MEASURE_UNIT);
			setState(256);
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
			setState(258);
			match(AGGR_FUNC);
			setState(259);
			match(OPEN_PAREN);
			setState(260);
			table_stat();
			setState(261);
			match(DOT);
			setState(262);
			column();
			setState(264);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(263);
				where_stat();
				}
			}

			setState(266);
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
		public Token table;
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
		public List<Fkey_table_to_fkey_colContext> fkey_table_to_fkey_col() {
			return getRuleContexts(Fkey_table_to_fkey_colContext.class);
		}
		public Fkey_table_to_fkey_colContext fkey_table_to_fkey_col(int i) {
			return getRuleContext(Fkey_table_to_fkey_colContext.class,i);
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
			setState(268);
			match(SQL_INJECTION_BODY);
			setState(269);
			match(OPEN_BRACE);
			setState(270);
			((Sql_injection_tmpContext)_localctx).table = match(ID);
			setState(271);
			match(CLOSE_BRACE);
			setState(272);
			match(OPEN_BRACE);
			setState(274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(273);
				((Sql_injection_tmpContext)_localctx).pkey_col = match(ID);
				}
			}

			setState(276);
			match(CLOSE_BRACE);
			setState(277);
			match(OPEN_BRACE);
			setState(287);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(283);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(278);
						fkey_col_to_pkey_table();
						setState(279);
						match(COMMA);
						}
						} 
					}
					setState(285);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
				}
				setState(286);
				fkey_col_to_pkey_table();
				}
			}

			setState(289);
			match(CLOSE_BRACE);
			setState(290);
			match(OPEN_BRACE);
			setState(300);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(296);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(291);
						fkey_table_to_fkey_col();
						setState(292);
						match(COMMA);
						}
						} 
					}
					setState(298);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
				}
				setState(299);
				fkey_table_to_fkey_col();
				}
			}

			setState(302);
			match(CLOSE_BRACE);
			setState(303);
			match(OPEN_BRACE);
			setState(305);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(304);
				((Sql_injection_tmpContext)_localctx).time_col = match(ID);
				}
			}

			setState(307);
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
		public Token table;
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
		public List<Fkey_table_to_fkey_colContext> fkey_table_to_fkey_col() {
			return getRuleContexts(Fkey_table_to_fkey_colContext.class);
		}
		public Fkey_table_to_fkey_colContext fkey_table_to_fkey_col(int i) {
			return getRuleContext(Fkey_table_to_fkey_colContext.class,i);
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
			setState(309);
			match(SQL_INJECTION_BODY);
			setState(310);
			match(OPEN_BRACE);
			setState(311);
			((Sql_injection_statContext)_localctx).table = match(ID);
			setState(312);
			match(CLOSE_BRACE);
			setState(313);
			match(OPEN_BRACE);
			setState(315);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(314);
				((Sql_injection_statContext)_localctx).pkey_col = match(ID);
				}
			}

			setState(317);
			match(CLOSE_BRACE);
			setState(318);
			match(OPEN_BRACE);
			setState(327);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(319);
				fkey_col_to_pkey_table();
				setState(324);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(320);
					match(COMMA);
					setState(321);
					fkey_col_to_pkey_table();
					}
					}
					setState(326);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(329);
			match(CLOSE_BRACE);
			setState(330);
			match(OPEN_BRACE);
			setState(339);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(331);
				fkey_table_to_fkey_col();
				setState(336);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(332);
					match(COMMA);
					setState(333);
					fkey_table_to_fkey_col();
					}
					}
					setState(338);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(341);
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
	public static class Path_nodeContext extends ParserRuleContext {
		public Token table;
		public Token left_key;
		public Token right_key;
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode COLON() { return getToken(ParserRTGL.COLON, 0); }
		public Path_nodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_path_node; }
	}

	public final Path_nodeContext path_node() throws RecognitionException {
		Path_nodeContext _localctx = new Path_nodeContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_path_node);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(343);
			((Path_nodeContext)_localctx).table = match(ID);
			setState(344);
			match(DOT);
			setState(345);
			((Path_nodeContext)_localctx).left_key = match(ID);
			setState(348);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(346);
				match(COLON);
				setState(347);
				((Path_nodeContext)_localctx).right_key = match(ID);
				}
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
	public static class Fkey_col_to_pkey_tableContext extends ParserRuleContext {
		public Token fkey_col;
		public Token pkey_table;
		public TerminalNode ARROW() { return getToken(ParserRTGL.ARROW, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public Fkey_col_to_pkey_tableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fkey_col_to_pkey_table; }
	}

	public final Fkey_col_to_pkey_tableContext fkey_col_to_pkey_table() throws RecognitionException {
		Fkey_col_to_pkey_tableContext _localctx = new Fkey_col_to_pkey_tableContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_fkey_col_to_pkey_table);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			((Fkey_col_to_pkey_tableContext)_localctx).fkey_col = match(ID);
			setState(351);
			match(ARROW);
			setState(352);
			((Fkey_col_to_pkey_tableContext)_localctx).pkey_table = match(ID);
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
	public static class Fkey_table_to_fkey_colContext extends ParserRuleContext {
		public Token fkey_table;
		public Token fkey_col;
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public Fkey_table_to_fkey_colContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fkey_table_to_fkey_col; }
	}

	public final Fkey_table_to_fkey_colContext fkey_table_to_fkey_col() throws RecognitionException {
		Fkey_table_to_fkey_colContext _localctx = new Fkey_table_to_fkey_colContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_fkey_table_to_fkey_col);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			((Fkey_table_to_fkey_colContext)_localctx).fkey_table = match(ID);
			setState(355);
			match(DOT);
			setState(356);
			((Fkey_table_to_fkey_colContext)_localctx).fkey_col = match(ID);
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
		enterRule(_localctx, 60, RULE_table_tmp);
		try {
			setState(360);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(358);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 2);
				{
				setState(359);
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
		enterRule(_localctx, 62, RULE_table_stat);
		try {
			setState(364);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(362);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 2);
				{
				setState(363);
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
		enterRule(_localctx, 64, RULE_column);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
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

	public static final String _serializedATN =
		"\u0004\u00015\u0171\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0001\u0000\u0003\u0000"+
		"E\b\u0000\u0001\u0001\u0003\u0001H\b\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001M\b\u0001\u0001\u0001\u0003\u0001P\b\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0003\u0002U\b\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002Z\b\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003b\b\u0003\n\u0003\f\u0003"+
		"e\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0004\u0004m\b\u0004\u000b\u0004\f\u0004n\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005x\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006\u007f\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007\u0086\b\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007\u008a\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0091"+
		"\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u009a"+
		"\b\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u00a8\b\f\n\f\f\f\u00ab"+
		"\t\f\u0001\r\u0001\r\u0001\r\u0005\r\u00b0\b\r\n\r\f\r\u00b3\t\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00b8\b\u000e\n\u000e\f\u000e"+
		"\u00bb\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00c0\b"+
		"\u000f\n\u000f\f\u000f\u00c3\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0003\u0010\u00ca\b\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00d1\b\u0011\u0001\u0012"+
		"\u0003\u0012\u00d4\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0003\u0012\u00da\b\u0012\u0001\u0013\u0003\u0013\u00dd\b\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00e4"+
		"\b\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00e9\b\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u00f9\b\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u0109\b\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u0113\b\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019"+
		"\u011a\b\u0019\n\u0019\f\u0019\u011d\t\u0019\u0001\u0019\u0003\u0019\u0120"+
		"\b\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0005"+
		"\u0019\u0127\b\u0019\n\u0019\f\u0019\u012a\t\u0019\u0001\u0019\u0003\u0019"+
		"\u012d\b\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u0132\b"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u013c\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u0143\b\u001a\n"+
		"\u001a\f\u001a\u0146\t\u001a\u0003\u001a\u0148\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u014f\b\u001a\n"+
		"\u001a\f\u001a\u0152\t\u001a\u0003\u001a\u0154\b\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003"+
		"\u001b\u015d\b\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0003"+
		"\u001e\u0169\b\u001e\u0001\u001f\u0001\u001f\u0003\u001f\u016d\b\u001f"+
		"\u0001 \u0001 \u0001 \u0000\u0000!\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@\u0000"+
		"\u0002\u0001\u0000-/\u0002\u0000&&22\u017d\u0000D\u0001\u0000\u0000\u0000"+
		"\u0002G\u0001\u0000\u0000\u0000\u0004T\u0001\u0000\u0000\u0000\u0006]"+
		"\u0001\u0000\u0000\u0000\bf\u0001\u0000\u0000\u0000\nr\u0001\u0000\u0000"+
		"\u0000\fy\u0001\u0000\u0000\u0000\u000e\u0089\u0001\u0000\u0000\u0000"+
		"\u0010\u0099\u0001\u0000\u0000\u0000\u0012\u009b\u0001\u0000\u0000\u0000"+
		"\u0014\u009e\u0001\u0000\u0000\u0000\u0016\u00a1\u0001\u0000\u0000\u0000"+
		"\u0018\u00a4\u0001\u0000\u0000\u0000\u001a\u00ac\u0001\u0000\u0000\u0000"+
		"\u001c\u00b4\u0001\u0000\u0000\u0000\u001e\u00bc\u0001\u0000\u0000\u0000"+
		" \u00c9\u0001\u0000\u0000\u0000\"\u00d0\u0001\u0000\u0000\u0000$\u00d3"+
		"\u0001\u0000\u0000\u0000&\u00dc\u0001\u0000\u0000\u0000(\u00ea\u0001\u0000"+
		"\u0000\u0000*\u00ed\u0001\u0000\u0000\u0000,\u00f0\u0001\u0000\u0000\u0000"+
		".\u00f2\u0001\u0000\u0000\u00000\u0102\u0001\u0000\u0000\u00002\u010c"+
		"\u0001\u0000\u0000\u00004\u0135\u0001\u0000\u0000\u00006\u0157\u0001\u0000"+
		"\u0000\u00008\u015e\u0001\u0000\u0000\u0000:\u0162\u0001\u0000\u0000\u0000"+
		"<\u0168\u0001\u0000\u0000\u0000>\u016c\u0001\u0000\u0000\u0000@\u016e"+
		"\u0001\u0000\u0000\u0000BE\u0003\u0002\u0001\u0000CE\u0003\u0004\u0002"+
		"\u0000DB\u0001\u0000\u0000\u0000DC\u0001\u0000\u0000\u0000E\u0001\u0001"+
		"\u0000\u0000\u0000FH\u0003\u0006\u0003\u0000GF\u0001\u0000\u0000\u0000"+
		"GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IJ\u0003\u000e\u0007"+
		"\u0000JL\u0003\n\u0005\u0000KM\u0003\u0012\t\u0000LK\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MO\u0001\u0000\u0000\u0000NP\u0003\u0016"+
		"\u000b\u0000ON\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PQ\u0001"+
		"\u0000\u0000\u0000QR\u0005\'\u0000\u0000R\u0003\u0001\u0000\u0000\u0000"+
		"SU\u0003\u0006\u0003\u0000TS\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000VW\u0003\u0010\b\u0000WY\u0003\f\u0006"+
		"\u0000XZ\u0003\u0014\n\u0000YX\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000Z[\u0001\u0000\u0000\u0000[\\\u0005\'\u0000\u0000\\\u0005\u0001"+
		"\u0000\u0000\u0000]^\u0005\u0001\u0000\u0000^c\u0003\b\u0004\u0000_`\u0005"+
		"\u001f\u0000\u0000`b\u0003\b\u0004\u0000a_\u0001\u0000\u0000\u0000be\u0001"+
		"\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000"+
		"d\u0007\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000fg\u00052\u0000"+
		"\u0000gh\u0005\u0006\u0000\u0000hi\u0005 \u0000\u0000il\u00036\u001b\u0000"+
		"jk\u0005(\u0000\u0000km\u00036\u001b\u0000lj\u0001\u0000\u0000\u0000m"+
		"n\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000no\u0001\u0000\u0000"+
		"\u0000op\u0001\u0000\u0000\u0000pq\u0005!\u0000\u0000q\t\u0001\u0000\u0000"+
		"\u0000rs\u0005\u0002\u0000\u0000st\u0003<\u001e\u0000tu\u0005\u001e\u0000"+
		"\u0000uw\u0003@ \u0000vx\u0003\u0014\n\u0000wv\u0001\u0000\u0000\u0000"+
		"wx\u0001\u0000\u0000\u0000x\u000b\u0001\u0000\u0000\u0000yz\u0005\u0002"+
		"\u0000\u0000z{\u0003>\u001f\u0000{|\u0005\u001e\u0000\u0000|~\u0003@ "+
		"\u0000}\u007f\u0003\u0014\n\u0000~}\u0001\u0000\u0000\u0000~\u007f\u0001"+
		"\u0000\u0000\u0000\u007f\r\u0001\u0000\u0000\u0000\u0080\u0081\u0005\u0003"+
		"\u0000\u0000\u0081\u0085\u0003.\u0017\u0000\u0082\u0083\u0005\b\u0000"+
		"\u0000\u0083\u0086\u0005/\u0000\u0000\u0084\u0086\u0005\u0007\u0000\u0000"+
		"\u0085\u0082\u0001\u0000\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u008a\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0005\u0003\u0000\u0000\u0088\u008a\u0003\u0018\f\u0000\u0089"+
		"\u0080\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a"+
		"\u000f\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u0003\u0000\u0000\u008c"+
		"\u0090\u00030\u0018\u0000\u008d\u008e\u0005\b\u0000\u0000\u008e\u0091"+
		"\u0005/\u0000\u0000\u008f\u0091\u0005\u0007\u0000\u0000\u0090\u008d\u0001"+
		"\u0000\u0000\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0090\u0091\u0001"+
		"\u0000\u0000\u0000\u0091\u009a\u0001\u0000\u0000\u0000\u0092\u0093\u0005"+
		"\u0003\u0000\u0000\u0093\u009a\u0003\u001a\r\u0000\u0094\u0095\u0005\u0003"+
		"\u0000\u0000\u0095\u0096\u0003>\u001f\u0000\u0096\u0097\u0005\u001e\u0000"+
		"\u0000\u0097\u0098\u0003@ \u0000\u0098\u009a\u0001\u0000\u0000\u0000\u0099"+
		"\u008b\u0001\u0000\u0000\u0000\u0099\u0092\u0001\u0000\u0000\u0000\u0099"+
		"\u0094\u0001\u0000\u0000\u0000\u009a\u0011\u0001\u0000\u0000\u0000\u009b"+
		"\u009c\u0005\u0004\u0000\u0000\u009c\u009d\u0003\u0018\f\u0000\u009d\u0013"+
		"\u0001\u0000\u0000\u0000\u009e\u009f\u0005\u0004\u0000\u0000\u009f\u00a0"+
		"\u0003\u001a\r\u0000\u00a0\u0015\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005"+
		"\u0005\u0000\u0000\u00a2\u00a3\u0003\u0018\f\u0000\u00a3\u0017\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a9\u0003\u001c\u000e\u0000\u00a5\u00a6\u0005+\u0000"+
		"\u0000\u00a6\u00a8\u0003\u001c\u000e\u0000\u00a7\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a8\u00ab\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000"+
		"\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u0019\u0001\u0000\u0000"+
		"\u0000\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ac\u00b1\u0003\u001e\u000f"+
		"\u0000\u00ad\u00ae\u0005+\u0000\u0000\u00ae\u00b0\u0003\u001e\u000f\u0000"+
		"\u00af\u00ad\u0001\u0000\u0000\u0000\u00b0\u00b3\u0001\u0000\u0000\u0000"+
		"\u00b1\u00af\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001\u0000\u0000\u0000"+
		"\u00b2\u001b\u0001\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000"+
		"\u00b4\u00b9\u0003 \u0010\u0000\u00b5\u00b6\u0005*\u0000\u0000\u00b6\u00b8"+
		"\u0003 \u0010\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b8\u00bb\u0001"+
		"\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001"+
		"\u0000\u0000\u0000\u00ba\u001d\u0001\u0000\u0000\u0000\u00bb\u00b9\u0001"+
		"\u0000\u0000\u0000\u00bc\u00c1\u0003\"\u0011\u0000\u00bd\u00be\u0005*"+
		"\u0000\u0000\u00be\u00c0\u0003\"\u0011\u0000\u00bf\u00bd\u0001\u0000\u0000"+
		"\u0000\u00c0\u00c3\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000"+
		"\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2\u001f\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c4\u00ca\u0003$\u0012\u0000"+
		"\u00c5\u00c6\u0005 \u0000\u0000\u00c6\u00c7\u0003\u0018\f\u0000\u00c7"+
		"\u00c8\u0005!\u0000\u0000\u00c8\u00ca\u0001\u0000\u0000\u0000\u00c9\u00c4"+
		"\u0001\u0000\u0000\u0000\u00c9\u00c5\u0001\u0000\u0000\u0000\u00ca!\u0001"+
		"\u0000\u0000\u0000\u00cb\u00d1\u0003&\u0013\u0000\u00cc\u00cd\u0005 \u0000"+
		"\u0000\u00cd\u00ce\u0003\u001a\r\u0000\u00ce\u00cf\u0005!\u0000\u0000"+
		"\u00cf\u00d1\u0001\u0000\u0000\u0000\u00d0\u00cb\u0001\u0000\u0000\u0000"+
		"\u00d0\u00cc\u0001\u0000\u0000\u0000\u00d1#\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d4\u0005,\u0000\u0000\u00d3\u00d2\u0001\u0000\u0000\u0000\u00d3\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000\u0000\u00d5\u00d9"+
		"\u0003.\u0017\u0000\u00d6\u00da\u0003(\u0014\u0000\u00d7\u00da\u0003*"+
		"\u0015\u0000\u00d8\u00da\u0003,\u0016\u0000\u00d9\u00d6\u0001\u0000\u0000"+
		"\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00d9\u00d8\u0001\u0000\u0000"+
		"\u0000\u00da%\u0001\u0000\u0000\u0000\u00db\u00dd\u0005,\u0000\u0000\u00dc"+
		"\u00db\u0001\u0000\u0000\u0000\u00dc\u00dd\u0001\u0000\u0000\u0000\u00dd"+
		"\u00e3\u0001\u0000\u0000\u0000\u00de\u00e4\u00030\u0018\u0000\u00df\u00e0"+
		"\u0003>\u001f\u0000\u00e0\u00e1\u0005\u001e\u0000\u0000\u00e1\u00e2\u0003"+
		"@ \u0000\u00e2\u00e4\u0001\u0000\u0000\u0000\u00e3\u00de\u0001\u0000\u0000"+
		"\u0000\u00e3\u00df\u0001\u0000\u0000\u0000\u00e4\u00e8\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e9\u0003(\u0014\u0000\u00e6\u00e9\u0003*\u0015\u0000\u00e7"+
		"\u00e9\u0003,\u0016\u0000\u00e8\u00e5\u0001\u0000\u0000\u0000\u00e8\u00e6"+
		"\u0001\u0000\u0000\u0000\u00e8\u00e7\u0001\u0000\u0000\u0000\u00e9\'\u0001"+
		"\u0000\u0000\u0000\u00ea\u00eb\u0005\u0013\u0000\u0000\u00eb\u00ec\u0007"+
		"\u0000\u0000\u0000\u00ec)\u0001\u0000\u0000\u0000\u00ed\u00ee\u0005\u0014"+
		"\u0000\u0000\u00ee\u00ef\u00051\u0000\u0000\u00ef+\u0001\u0000\u0000\u0000"+
		"\u00f0\u00f1\u0005\u001b\u0000\u0000\u00f1-\u0001\u0000\u0000\u0000\u00f2"+
		"\u00f3\u0005\t\u0000\u0000\u00f3\u00f4\u0005 \u0000\u0000\u00f4\u00f5"+
		"\u0003<\u001e\u0000\u00f5\u00f6\u0005\u001e\u0000\u0000\u00f6\u00f8\u0003"+
		"@ \u0000\u00f7\u00f9\u0003\u0014\n\u0000\u00f8\u00f7\u0001\u0000\u0000"+
		"\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9\u00fa\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0005\u001f\u0000\u0000\u00fb\u00fc\u0005/\u0000\u0000"+
		"\u00fc\u00fd\u0005\u001f\u0000\u0000\u00fd\u00fe\u0005/\u0000\u0000\u00fe"+
		"\u00ff\u0005\u001f\u0000\u0000\u00ff\u0100\u00050\u0000\u0000\u0100\u0101"+
		"\u0005!\u0000\u0000\u0101/\u0001\u0000\u0000\u0000\u0102\u0103\u0005\t"+
		"\u0000\u0000\u0103\u0104\u0005 \u0000\u0000\u0104\u0105\u0003>\u001f\u0000"+
		"\u0105\u0106\u0005\u001e\u0000\u0000\u0106\u0108\u0003@ \u0000\u0107\u0109"+
		"\u0003\u0014\n\u0000\u0108\u0107\u0001\u0000\u0000\u0000\u0108\u0109\u0001"+
		"\u0000\u0000\u0000\u0109\u010a\u0001\u0000\u0000\u0000\u010a\u010b\u0005"+
		"!\u0000\u0000\u010b1\u0001\u0000\u0000\u0000\u010c\u010d\u00053\u0000"+
		"\u0000\u010d\u010e\u0005$\u0000\u0000\u010e\u010f\u00052\u0000\u0000\u010f"+
		"\u0110\u0005%\u0000\u0000\u0110\u0112\u0005$\u0000\u0000\u0111\u0113\u0005"+
		"2\u0000\u0000\u0112\u0111\u0001\u0000\u0000\u0000\u0112\u0113\u0001\u0000"+
		"\u0000\u0000\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0115\u0005%\u0000"+
		"\u0000\u0115\u011f\u0005$\u0000\u0000\u0116\u0117\u00038\u001c\u0000\u0117"+
		"\u0118\u0005\u001f\u0000\u0000\u0118\u011a\u0001\u0000\u0000\u0000\u0119"+
		"\u0116\u0001\u0000\u0000\u0000\u011a\u011d\u0001\u0000\u0000\u0000\u011b"+
		"\u0119\u0001\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c"+
		"\u011e\u0001\u0000\u0000\u0000\u011d\u011b\u0001\u0000\u0000\u0000\u011e"+
		"\u0120\u00038\u001c\u0000\u011f\u011b\u0001\u0000\u0000\u0000\u011f\u0120"+
		"\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000\u0000\u0121\u0122"+
		"\u0005%\u0000\u0000\u0122\u012c\u0005$\u0000\u0000\u0123\u0124\u0003:"+
		"\u001d\u0000\u0124\u0125\u0005\u001f\u0000\u0000\u0125\u0127\u0001\u0000"+
		"\u0000\u0000\u0126\u0123\u0001\u0000\u0000\u0000\u0127\u012a\u0001\u0000"+
		"\u0000\u0000\u0128\u0126\u0001\u0000\u0000\u0000\u0128\u0129\u0001\u0000"+
		"\u0000\u0000\u0129\u012b\u0001\u0000\u0000\u0000\u012a\u0128\u0001\u0000"+
		"\u0000\u0000\u012b\u012d\u0003:\u001d\u0000\u012c\u0128\u0001\u0000\u0000"+
		"\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d\u012e\u0001\u0000\u0000"+
		"\u0000\u012e\u012f\u0005%\u0000\u0000\u012f\u0131\u0005$\u0000\u0000\u0130"+
		"\u0132\u00052\u0000\u0000\u0131\u0130\u0001\u0000\u0000\u0000\u0131\u0132"+
		"\u0001\u0000\u0000\u0000\u0132\u0133\u0001\u0000\u0000\u0000\u0133\u0134"+
		"\u0005%\u0000\u0000\u01343\u0001\u0000\u0000\u0000\u0135\u0136\u00053"+
		"\u0000\u0000\u0136\u0137\u0005$\u0000\u0000\u0137\u0138\u00052\u0000\u0000"+
		"\u0138\u0139\u0005%\u0000\u0000\u0139\u013b\u0005$\u0000\u0000\u013a\u013c"+
		"\u00052\u0000\u0000\u013b\u013a\u0001\u0000\u0000\u0000\u013b\u013c\u0001"+
		"\u0000\u0000\u0000\u013c\u013d\u0001\u0000\u0000\u0000\u013d\u013e\u0005"+
		"%\u0000\u0000\u013e\u0147\u0005$\u0000\u0000\u013f\u0144\u00038\u001c"+
		"\u0000\u0140\u0141\u0005\u001f\u0000\u0000\u0141\u0143\u00038\u001c\u0000"+
		"\u0142\u0140\u0001\u0000\u0000\u0000\u0143\u0146\u0001\u0000\u0000\u0000"+
		"\u0144\u0142\u0001\u0000\u0000\u0000\u0144\u0145\u0001\u0000\u0000\u0000"+
		"\u0145\u0148\u0001\u0000\u0000\u0000\u0146\u0144\u0001\u0000\u0000\u0000"+
		"\u0147\u013f\u0001\u0000\u0000\u0000\u0147\u0148\u0001\u0000\u0000\u0000"+
		"\u0148\u0149\u0001\u0000\u0000\u0000\u0149\u014a\u0005%\u0000\u0000\u014a"+
		"\u0153\u0005$\u0000\u0000\u014b\u0150\u0003:\u001d\u0000\u014c\u014d\u0005"+
		"\u001f\u0000\u0000\u014d\u014f\u0003:\u001d\u0000\u014e\u014c\u0001\u0000"+
		"\u0000\u0000\u014f\u0152\u0001\u0000\u0000\u0000\u0150\u014e\u0001\u0000"+
		"\u0000\u0000\u0150\u0151\u0001\u0000\u0000\u0000\u0151\u0154\u0001\u0000"+
		"\u0000\u0000\u0152\u0150\u0001\u0000\u0000\u0000\u0153\u014b\u0001\u0000"+
		"\u0000\u0000\u0153\u0154\u0001\u0000\u0000\u0000\u0154\u0155\u0001\u0000"+
		"\u0000\u0000\u0155\u0156\u0005%\u0000\u0000\u01565\u0001\u0000\u0000\u0000"+
		"\u0157\u0158\u00052\u0000\u0000\u0158\u0159\u0005\u001e\u0000\u0000\u0159"+
		"\u015c\u00052\u0000\u0000\u015a\u015b\u0005)\u0000\u0000\u015b\u015d\u0005"+
		"2\u0000\u0000\u015c\u015a\u0001\u0000\u0000\u0000\u015c\u015d\u0001\u0000"+
		"\u0000\u0000\u015d7\u0001\u0000\u0000\u0000\u015e\u015f\u00052\u0000\u0000"+
		"\u015f\u0160\u0005(\u0000\u0000\u0160\u0161\u00052\u0000\u0000\u01619"+
		"\u0001\u0000\u0000\u0000\u0162\u0163\u00052\u0000\u0000\u0163\u0164\u0005"+
		"\u001e\u0000\u0000\u0164\u0165\u00052\u0000\u0000\u0165;\u0001\u0000\u0000"+
		"\u0000\u0166\u0169\u00052\u0000\u0000\u0167\u0169\u00032\u0019\u0000\u0168"+
		"\u0166\u0001\u0000\u0000\u0000\u0168\u0167\u0001\u0000\u0000\u0000\u0169"+
		"=\u0001\u0000\u0000\u0000\u016a\u016d\u00052\u0000\u0000\u016b\u016d\u0003"+
		"4\u001a\u0000\u016c\u016a\u0001\u0000\u0000\u0000\u016c\u016b\u0001\u0000"+
		"\u0000\u0000\u016d?\u0001\u0000\u0000\u0000\u016e\u016f\u0007\u0001\u0000"+
		"\u0000\u016fA\u0001\u0000\u0000\u0000)DGLOTYcnw~\u0085\u0089\u0090\u0099"+
		"\u00a9\u00b1\u00b9\u00c1\u00c9\u00d0\u00d3\u00d9\u00dc\u00e3\u00e8\u00f8"+
		"\u0108\u0112\u011b\u011f\u0128\u012c\u0131\u013b\u0144\u0147\u0150\u0153"+
		"\u015c\u0168\u016c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}