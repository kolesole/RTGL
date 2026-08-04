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
		ASSUMING=1, FOR_EACH=2, PREDICT=3, WHERE=4, CLASSIFY=5, RANK_TOP=6, AGGR_FUNC=7, 
		AVG=8, COUNT=9, COUNT_DISTINCT=10, FIRST=11, LAST=12, LIST_DISTINCT=13, 
		MAX=14, MIN=15, SUM=16, NUM_COMP_OP=17, STR_COMP_OP=18, NOT_LIKE=19, NOT_CONTAINS=20, 
		ENDS_WITH=21, STARTS_WITH=22, LIKE=23, CONTAINS=24, NULL_CHECK_OP=25, 
		IS_NOT_NULL=26, IS_NULL=27, DOT=28, COMMA=29, OPEN_PAREN=30, CLOSE_PAREN=31, 
		OPEN_BRACKET=32, CLOSE_BRACKET=33, OPEN_BRACE=34, CLOSE_BRACE=35, STAR=36, 
		SEMICOLON=37, ARROW=38, COLON=39, AND=40, OR=41, NOT=42, DATETIME=43, 
		FLOAT=44, INT=45, TIME_MEASURE_UNIT=46, STRING=47, ID=48, SQL_INJECTION_BODY=49, 
		WS_SKIP=50, ANY=51;
	public static final int
		RULE_query = 0, RULE_query_tmp = 1, RULE_query_stat = 2, RULE_for_each_tmp = 3, 
		RULE_for_each_stat = 4, RULE_predict_tmp = 5, RULE_predict_stat = 6, RULE_assuming = 7, 
		RULE_where_tmp = 8, RULE_where_stat = 9, RULE_expr_or_tmp = 10, RULE_expr_or_stat = 11, 
		RULE_expr_and_tmp = 12, RULE_expr_and_stat = 13, RULE_expr_term_tmp = 14, 
		RULE_expr_term_stat = 15, RULE_condition_tmp = 16, RULE_condition_stat = 17, 
		RULE_num_condition = 18, RULE_str_condition = 19, RULE_null_check_condition = 20, 
		RULE_aggregation_tmp = 21, RULE_aggregation_stat = 22, RULE_sql_injection_tmp = 23, 
		RULE_sql_injection_stat = 24, RULE_fk_col_to_pk_table = 25, RULE_fk_table_col = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "query_tmp", "query_stat", "for_each_tmp", "for_each_stat", 
			"predict_tmp", "predict_stat", "assuming", "where_tmp", "where_stat", 
			"expr_or_tmp", "expr_or_stat", "expr_and_tmp", "expr_and_stat", "expr_term_tmp", 
			"expr_term_stat", "condition_tmp", "condition_stat", "num_condition", 
			"str_condition", "null_check_condition", "aggregation_tmp", "aggregation_stat", 
			"sql_injection_tmp", "sql_injection_stat", "fk_col_to_pk_table", "fk_table_col"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "'.'", "','", "'('", "')'", "'['", "']'", "'{'", 
			"'}'", "'*'", "';'", "'->'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSUMING", "FOR_EACH", "PREDICT", "WHERE", "CLASSIFY", "RANK_TOP", 
			"AGGR_FUNC", "AVG", "COUNT", "COUNT_DISTINCT", "FIRST", "LAST", "LIST_DISTINCT", 
			"MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", "NOT_LIKE", "NOT_CONTAINS", 
			"ENDS_WITH", "STARTS_WITH", "LIKE", "CONTAINS", "NULL_CHECK_OP", "IS_NOT_NULL", 
			"IS_NULL", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACKET", 
			"CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "STAR", "SEMICOLON", "ARROW", 
			"COLON", "AND", "OR", "NOT", "DATETIME", "FLOAT", "INT", "TIME_MEASURE_UNIT", 
			"STRING", "ID", "SQL_INJECTION_BODY", "WS_SKIP", "ANY"
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
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				query_tmp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
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
			setState(58);
			predict_tmp();
			setState(59);
			for_each_tmp();
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(60);
				where_tmp();
				}
			}

			setState(64);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSUMING) {
				{
				setState(63);
				assuming();
				}
			}

			setState(66);
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
			setState(68);
			predict_stat();
			setState(69);
			for_each_stat();
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(70);
				where_stat();
				}
			}

			setState(73);
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
	public static class For_each_tmpContext extends ParserRuleContext {
		public TerminalNode FOR_EACH() { return getToken(ParserRTGL.FOR_EACH, 0); }
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public Sql_injection_tmpContext sql_injection_tmp() {
			return getRuleContext(Sql_injection_tmpContext.class,0);
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
		enterRule(_localctx, 6, RULE_for_each_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(FOR_EACH);
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(76);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				{
				setState(77);
				sql_injection_tmp();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(80);
			match(DOT);
			setState(81);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(82);
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
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public Sql_injection_statContext sql_injection_stat() {
			return getRuleContext(Sql_injection_statContext.class,0);
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
		enterRule(_localctx, 8, RULE_for_each_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(FOR_EACH);
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(86);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				{
				setState(87);
				sql_injection_stat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(90);
			match(DOT);
			setState(91);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(92);
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
		enterRule(_localctx, 10, RULE_predict_tmp);
		try {
			setState(104);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				match(PREDICT);
				setState(96);
				aggregation_tmp();
				setState(100);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(97);
					match(RANK_TOP);
					setState(98);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(99);
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
				setState(102);
				match(PREDICT);
				setState(103);
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
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public Sql_injection_statContext sql_injection_stat() {
			return getRuleContext(Sql_injection_statContext.class,0);
		}
		public Predict_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict_stat; }
	}

	public final Predict_statContext predict_stat() throws RecognitionException {
		Predict_statContext _localctx = new Predict_statContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_predict_stat);
		int _la;
		try {
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				match(PREDICT);
				setState(107);
				aggregation_stat();
				setState(111);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(108);
					match(RANK_TOP);
					setState(109);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(110);
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
				setState(113);
				match(PREDICT);
				setState(114);
				expr_or_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(115);
				match(PREDICT);
				setState(118);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(116);
					match(ID);
					}
					break;
				case SQL_INJECTION_BODY:
					{
					setState(117);
					sql_injection_stat();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(120);
				match(DOT);
				setState(121);
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
		enterRule(_localctx, 14, RULE_assuming);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(ASSUMING);
			setState(125);
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
		enterRule(_localctx, 16, RULE_where_tmp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(WHERE);
			setState(128);
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
		enterRule(_localctx, 18, RULE_where_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(WHERE);
			setState(131);
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
		enterRule(_localctx, 20, RULE_expr_or_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			expr_and_tmp();
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(134);
				match(OR);
				setState(135);
				expr_and_tmp();
				}
				}
				setState(140);
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
		enterRule(_localctx, 22, RULE_expr_or_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			expr_and_stat();
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(142);
				match(OR);
				setState(143);
				expr_and_stat();
				}
				}
				setState(148);
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
		enterRule(_localctx, 24, RULE_expr_and_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			expr_term_tmp();
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(150);
				match(AND);
				setState(151);
				expr_term_tmp();
				}
				}
				setState(156);
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
		enterRule(_localctx, 26, RULE_expr_and_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			expr_term_stat();
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(158);
				match(AND);
				setState(159);
				expr_term_stat();
				}
				}
				setState(164);
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
		enterRule(_localctx, 28, RULE_expr_term_tmp);
		try {
			setState(170);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(165);
				condition_tmp();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(166);
				match(OPEN_PAREN);
				setState(167);
				expr_or_tmp();
				setState(168);
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
		enterRule(_localctx, 30, RULE_expr_term_stat);
		try {
			setState(177);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
			case ID:
			case SQL_INJECTION_BODY:
				enterOuterAlt(_localctx, 1);
				{
				setState(172);
				condition_stat();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(173);
				match(OPEN_PAREN);
				setState(174);
				expr_or_stat();
				setState(175);
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
		enterRule(_localctx, 32, RULE_condition_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(179);
				match(NOT);
				}
			}

			setState(182);
			aggregation_tmp();
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(183);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(184);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(185);
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
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
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
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public Sql_injection_statContext sql_injection_stat() {
			return getRuleContext(Sql_injection_statContext.class,0);
		}
		public Condition_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_stat; }
	}

	public final Condition_statContext condition_stat() throws RecognitionException {
		Condition_statContext _localctx = new Condition_statContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_condition_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(188);
				match(NOT);
				}
			}

			setState(198);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
				{
				setState(191);
				aggregation_stat();
				}
				break;
			case ID:
			case SQL_INJECTION_BODY:
				{
				setState(194);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(192);
					match(ID);
					}
					break;
				case SQL_INJECTION_BODY:
					{
					setState(193);
					sql_injection_stat();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(196);
				match(DOT);
				setState(197);
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
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(203);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(200);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(201);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(202);
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
		enterRule(_localctx, 36, RULE_num_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(NUM_COMP_OP);
			setState(206);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 61572651155456L) != 0)) ) {
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
		enterRule(_localctx, 38, RULE_str_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(STR_COMP_OP);
			setState(209);
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
		enterRule(_localctx, 40, RULE_null_check_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
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
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
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
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public Sql_injection_tmpContext sql_injection_tmp() {
			return getRuleContext(Sql_injection_tmpContext.class,0);
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
		enterRule(_localctx, 42, RULE_aggregation_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(AGGR_FUNC);
			setState(214);
			match(OPEN_PAREN);
			setState(217);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(215);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				{
				setState(216);
				sql_injection_tmp();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(219);
			match(DOT);
			setState(220);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(221);
				where_stat();
				}
			}

			setState(224);
			match(COMMA);
			setState(225);
			match(INT);
			setState(226);
			match(COMMA);
			setState(227);
			match(INT);
			setState(228);
			match(COMMA);
			setState(229);
			match(TIME_MEASURE_UNIT);
			setState(230);
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
		public TerminalNode DOT() { return getToken(ParserRTGL.DOT, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserRTGL.CLOSE_PAREN, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode STAR() { return getToken(ParserRTGL.STAR, 0); }
		public Sql_injection_statContext sql_injection_stat() {
			return getRuleContext(Sql_injection_statContext.class,0);
		}
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
		enterRule(_localctx, 44, RULE_aggregation_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(AGGR_FUNC);
			setState(233);
			match(OPEN_PAREN);
			setState(236);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(234);
				match(ID);
				}
				break;
			case SQL_INJECTION_BODY:
				{
				setState(235);
				sql_injection_stat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(238);
			match(DOT);
			setState(239);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(240);
				where_stat();
				}
			}

			setState(243);
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
		public TerminalNode SQL_INJECTION_BODY() { return getToken(ParserRTGL.SQL_INJECTION_BODY, 0); }
		public List<TerminalNode> OPEN_BRACE() { return getTokens(ParserRTGL.OPEN_BRACE); }
		public TerminalNode OPEN_BRACE(int i) {
			return getToken(ParserRTGL.OPEN_BRACE, i);
		}
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public List<TerminalNode> CLOSE_BRACE() { return getTokens(ParserRTGL.CLOSE_BRACE); }
		public TerminalNode CLOSE_BRACE(int i) {
			return getToken(ParserRTGL.CLOSE_BRACE, i);
		}
		public List<Fk_col_to_pk_tableContext> fk_col_to_pk_table() {
			return getRuleContexts(Fk_col_to_pk_tableContext.class);
		}
		public Fk_col_to_pk_tableContext fk_col_to_pk_table(int i) {
			return getRuleContext(Fk_col_to_pk_tableContext.class,i);
		}
		public List<Fk_table_colContext> fk_table_col() {
			return getRuleContexts(Fk_table_colContext.class);
		}
		public Fk_table_colContext fk_table_col(int i) {
			return getRuleContext(Fk_table_colContext.class,i);
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
		enterRule(_localctx, 46, RULE_sql_injection_tmp);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(SQL_INJECTION_BODY);
			setState(246);
			match(OPEN_BRACE);
			setState(247);
			match(ID);
			setState(248);
			match(CLOSE_BRACE);
			setState(249);
			match(OPEN_BRACE);
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(250);
				match(ID);
				}
			}

			setState(253);
			match(CLOSE_BRACE);
			setState(254);
			match(OPEN_BRACE);
			setState(264);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(260);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(255);
						fk_col_to_pk_table();
						setState(256);
						match(COMMA);
						}
						} 
					}
					setState(262);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
				}
				setState(263);
				fk_col_to_pk_table();
				}
			}

			setState(266);
			match(CLOSE_BRACE);
			setState(267);
			match(OPEN_BRACE);
			setState(277);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(273);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(268);
						fk_table_col();
						setState(269);
						match(COMMA);
						}
						} 
					}
					setState(275);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
				}
				setState(276);
				fk_table_col();
				}
			}

			setState(279);
			match(CLOSE_BRACE);
			setState(280);
			match(OPEN_BRACE);
			setState(281);
			match(ID);
			setState(282);
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
		public TerminalNode SQL_INJECTION_BODY() { return getToken(ParserRTGL.SQL_INJECTION_BODY, 0); }
		public List<TerminalNode> OPEN_BRACE() { return getTokens(ParserRTGL.OPEN_BRACE); }
		public TerminalNode OPEN_BRACE(int i) {
			return getToken(ParserRTGL.OPEN_BRACE, i);
		}
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public List<TerminalNode> CLOSE_BRACE() { return getTokens(ParserRTGL.CLOSE_BRACE); }
		public TerminalNode CLOSE_BRACE(int i) {
			return getToken(ParserRTGL.CLOSE_BRACE, i);
		}
		public List<Fk_col_to_pk_tableContext> fk_col_to_pk_table() {
			return getRuleContexts(Fk_col_to_pk_tableContext.class);
		}
		public Fk_col_to_pk_tableContext fk_col_to_pk_table(int i) {
			return getRuleContext(Fk_col_to_pk_tableContext.class,i);
		}
		public List<Fk_table_colContext> fk_table_col() {
			return getRuleContexts(Fk_table_colContext.class);
		}
		public Fk_table_colContext fk_table_col(int i) {
			return getRuleContext(Fk_table_colContext.class,i);
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
		enterRule(_localctx, 48, RULE_sql_injection_stat);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(SQL_INJECTION_BODY);
			setState(285);
			match(OPEN_BRACE);
			setState(286);
			match(ID);
			setState(287);
			match(CLOSE_BRACE);
			setState(288);
			match(OPEN_BRACE);
			setState(290);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(289);
				match(ID);
				}
			}

			setState(292);
			match(CLOSE_BRACE);
			setState(293);
			match(OPEN_BRACE);
			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(299);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(294);
						fk_col_to_pk_table();
						setState(295);
						match(COMMA);
						}
						} 
					}
					setState(301);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
				}
				setState(302);
				fk_col_to_pk_table();
				}
			}

			setState(305);
			match(CLOSE_BRACE);
			setState(306);
			match(OPEN_BRACE);
			setState(316);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(312);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(307);
						fk_table_col();
						setState(308);
						match(COMMA);
						}
						} 
					}
					setState(314);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
				}
				setState(315);
				fk_table_col();
				}
			}

			setState(318);
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
	public static class Fk_col_to_pk_tableContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode ARROW() { return getToken(ParserRTGL.ARROW, 0); }
		public Fk_col_to_pk_tableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fk_col_to_pk_table; }
	}

	public final Fk_col_to_pk_tableContext fk_col_to_pk_table() throws RecognitionException {
		Fk_col_to_pk_tableContext _localctx = new Fk_col_to_pk_tableContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_fk_col_to_pk_table);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
			match(ID);
			setState(321);
			match(ARROW);
			setState(322);
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
	public static class Fk_table_colContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ParserRTGL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserRTGL.ID, i);
		}
		public TerminalNode COLON() { return getToken(ParserRTGL.COLON, 0); }
		public Fk_table_colContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fk_table_col; }
	}

	public final Fk_table_colContext fk_table_col() throws RecognitionException {
		Fk_table_colContext _localctx = new Fk_table_colContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_fk_table_col);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			match(ID);
			setState(325);
			match(COLON);
			setState(326);
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
		"\u0004\u00013\u0149\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0001\u0000\u0001\u0000"+
		"\u0003\u00009\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		">\b\u0001\u0001\u0001\u0003\u0001A\b\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002H\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003O\b\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003T\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004Y\b\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u0004^\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u0005e\b\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005i\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006p\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006w\b\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006{\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\n\u0089\b\n\n"+
		"\n\f\n\u008c\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u0091"+
		"\b\u000b\n\u000b\f\u000b\u0094\t\u000b\u0001\f\u0001\f\u0001\f\u0005\f"+
		"\u0099\b\f\n\f\f\f\u009c\t\f\u0001\r\u0001\r\u0001\r\u0005\r\u00a1\b\r"+
		"\n\r\f\r\u00a4\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u00ab\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u00b2\b\u000f\u0001\u0010\u0003\u0010\u00b5"+
		"\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00bb"+
		"\b\u0010\u0001\u0011\u0003\u0011\u00be\b\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u00c3\b\u0011\u0001\u0011\u0001\u0011\u0003\u0011"+
		"\u00c7\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00cc\b"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0003\u0015\u00da\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003"+
		"\u0015\u00df\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0003\u0016\u00ed\b\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0003\u0016\u00f2\b\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00fc"+
		"\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005"+
		"\u0017\u0103\b\u0017\n\u0017\f\u0017\u0106\t\u0017\u0001\u0017\u0003\u0017"+
		"\u0109\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0005\u0017\u0110\b\u0017\n\u0017\f\u0017\u0113\t\u0017\u0001\u0017\u0003"+
		"\u0017\u0116\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0003\u0018\u0123\b\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0005\u0018\u012a\b\u0018\n\u0018\f\u0018\u012d\t\u0018"+
		"\u0001\u0018\u0003\u0018\u0130\b\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0005\u0018\u0137\b\u0018\n\u0018\f\u0018\u013a"+
		"\t\u0018\u0001\u0018\u0003\u0018\u013d\b\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0000\u0000\u001b\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.024\u0000\u0002\u0002\u0000$$00\u0001\u0000+-\u0159\u00008\u0001"+
		"\u0000\u0000\u0000\u0002:\u0001\u0000\u0000\u0000\u0004D\u0001\u0000\u0000"+
		"\u0000\u0006K\u0001\u0000\u0000\u0000\bU\u0001\u0000\u0000\u0000\nh\u0001"+
		"\u0000\u0000\u0000\fz\u0001\u0000\u0000\u0000\u000e|\u0001\u0000\u0000"+
		"\u0000\u0010\u007f\u0001\u0000\u0000\u0000\u0012\u0082\u0001\u0000\u0000"+
		"\u0000\u0014\u0085\u0001\u0000\u0000\u0000\u0016\u008d\u0001\u0000\u0000"+
		"\u0000\u0018\u0095\u0001\u0000\u0000\u0000\u001a\u009d\u0001\u0000\u0000"+
		"\u0000\u001c\u00aa\u0001\u0000\u0000\u0000\u001e\u00b1\u0001\u0000\u0000"+
		"\u0000 \u00b4\u0001\u0000\u0000\u0000\"\u00bd\u0001\u0000\u0000\u0000"+
		"$\u00cd\u0001\u0000\u0000\u0000&\u00d0\u0001\u0000\u0000\u0000(\u00d3"+
		"\u0001\u0000\u0000\u0000*\u00d5\u0001\u0000\u0000\u0000,\u00e8\u0001\u0000"+
		"\u0000\u0000.\u00f5\u0001\u0000\u0000\u00000\u011c\u0001\u0000\u0000\u0000"+
		"2\u0140\u0001\u0000\u0000\u00004\u0144\u0001\u0000\u0000\u000069\u0003"+
		"\u0002\u0001\u000079\u0003\u0004\u0002\u000086\u0001\u0000\u0000\u0000"+
		"87\u0001\u0000\u0000\u00009\u0001\u0001\u0000\u0000\u0000:;\u0003\n\u0005"+
		"\u0000;=\u0003\u0006\u0003\u0000<>\u0003\u0010\b\u0000=<\u0001\u0000\u0000"+
		"\u0000=>\u0001\u0000\u0000\u0000>@\u0001\u0000\u0000\u0000?A\u0003\u000e"+
		"\u0007\u0000@?\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AB\u0001"+
		"\u0000\u0000\u0000BC\u0005%\u0000\u0000C\u0003\u0001\u0000\u0000\u0000"+
		"DE\u0003\f\u0006\u0000EG\u0003\b\u0004\u0000FH\u0003\u0012\t\u0000GF\u0001"+
		"\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000"+
		"IJ\u0005%\u0000\u0000J\u0005\u0001\u0000\u0000\u0000KN\u0005\u0002\u0000"+
		"\u0000LO\u00050\u0000\u0000MO\u0003.\u0017\u0000NL\u0001\u0000\u0000\u0000"+
		"NM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PQ\u0005\u001c\u0000"+
		"\u0000QS\u0007\u0000\u0000\u0000RT\u0003\u0012\t\u0000SR\u0001\u0000\u0000"+
		"\u0000ST\u0001\u0000\u0000\u0000T\u0007\u0001\u0000\u0000\u0000UX\u0005"+
		"\u0002\u0000\u0000VY\u00050\u0000\u0000WY\u00030\u0018\u0000XV\u0001\u0000"+
		"\u0000\u0000XW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z[\u0005"+
		"\u001c\u0000\u0000[]\u0007\u0000\u0000\u0000\\^\u0003\u0012\t\u0000]\\"+
		"\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\t\u0001\u0000\u0000"+
		"\u0000_`\u0005\u0003\u0000\u0000`d\u0003*\u0015\u0000ab\u0005\u0006\u0000"+
		"\u0000be\u0005-\u0000\u0000ce\u0005\u0005\u0000\u0000da\u0001\u0000\u0000"+
		"\u0000dc\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ei\u0001\u0000"+
		"\u0000\u0000fg\u0005\u0003\u0000\u0000gi\u0003\u0014\n\u0000h_\u0001\u0000"+
		"\u0000\u0000hf\u0001\u0000\u0000\u0000i\u000b\u0001\u0000\u0000\u0000"+
		"jk\u0005\u0003\u0000\u0000ko\u0003,\u0016\u0000lm\u0005\u0006\u0000\u0000"+
		"mp\u0005-\u0000\u0000np\u0005\u0005\u0000\u0000ol\u0001\u0000\u0000\u0000"+
		"on\u0001\u0000\u0000\u0000op\u0001\u0000\u0000\u0000p{\u0001\u0000\u0000"+
		"\u0000qr\u0005\u0003\u0000\u0000r{\u0003\u0016\u000b\u0000sv\u0005\u0003"+
		"\u0000\u0000tw\u00050\u0000\u0000uw\u00030\u0018\u0000vt\u0001\u0000\u0000"+
		"\u0000vu\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000xy\u0005\u001c"+
		"\u0000\u0000y{\u0007\u0000\u0000\u0000zj\u0001\u0000\u0000\u0000zq\u0001"+
		"\u0000\u0000\u0000zs\u0001\u0000\u0000\u0000{\r\u0001\u0000\u0000\u0000"+
		"|}\u0005\u0001\u0000\u0000}~\u0003\u0014\n\u0000~\u000f\u0001\u0000\u0000"+
		"\u0000\u007f\u0080\u0005\u0004\u0000\u0000\u0080\u0081\u0003\u0014\n\u0000"+
		"\u0081\u0011\u0001\u0000\u0000\u0000\u0082\u0083\u0005\u0004\u0000\u0000"+
		"\u0083\u0084\u0003\u0016\u000b\u0000\u0084\u0013\u0001\u0000\u0000\u0000"+
		"\u0085\u008a\u0003\u0018\f\u0000\u0086\u0087\u0005)\u0000\u0000\u0087"+
		"\u0089\u0003\u0018\f\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0089\u008c"+
		"\u0001\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u008b"+
		"\u0001\u0000\u0000\u0000\u008b\u0015\u0001\u0000\u0000\u0000\u008c\u008a"+
		"\u0001\u0000\u0000\u0000\u008d\u0092\u0003\u001a\r\u0000\u008e\u008f\u0005"+
		")\u0000\u0000\u008f\u0091\u0003\u001a\r\u0000\u0090\u008e\u0001\u0000"+
		"\u0000\u0000\u0091\u0094\u0001\u0000\u0000\u0000\u0092\u0090\u0001\u0000"+
		"\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0017\u0001\u0000"+
		"\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0095\u009a\u0003\u001c"+
		"\u000e\u0000\u0096\u0097\u0005(\u0000\u0000\u0097\u0099\u0003\u001c\u000e"+
		"\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0099\u009c\u0001\u0000\u0000"+
		"\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000"+
		"\u0000\u009b\u0019\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000"+
		"\u0000\u009d\u00a2\u0003\u001e\u000f\u0000\u009e\u009f\u0005(\u0000\u0000"+
		"\u009f\u00a1\u0003\u001e\u000f\u0000\u00a0\u009e\u0001\u0000\u0000\u0000"+
		"\u00a1\u00a4\u0001\u0000\u0000\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000"+
		"\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u001b\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a5\u00ab\u0003 \u0010\u0000\u00a6"+
		"\u00a7\u0005\u001e\u0000\u0000\u00a7\u00a8\u0003\u0014\n\u0000\u00a8\u00a9"+
		"\u0005\u001f\u0000\u0000\u00a9\u00ab\u0001\u0000\u0000\u0000\u00aa\u00a5"+
		"\u0001\u0000\u0000\u0000\u00aa\u00a6\u0001\u0000\u0000\u0000\u00ab\u001d"+
		"\u0001\u0000\u0000\u0000\u00ac\u00b2\u0003\"\u0011\u0000\u00ad\u00ae\u0005"+
		"\u001e\u0000\u0000\u00ae\u00af\u0003\u0016\u000b\u0000\u00af\u00b0\u0005"+
		"\u001f\u0000\u0000\u00b0\u00b2\u0001\u0000\u0000\u0000\u00b1\u00ac\u0001"+
		"\u0000\u0000\u0000\u00b1\u00ad\u0001\u0000\u0000\u0000\u00b2\u001f\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b5\u0005*\u0000\u0000\u00b4\u00b3\u0001\u0000"+
		"\u0000\u0000\u00b4\u00b5\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000"+
		"\u0000\u0000\u00b6\u00ba\u0003*\u0015\u0000\u00b7\u00bb\u0003$\u0012\u0000"+
		"\u00b8\u00bb\u0003&\u0013\u0000\u00b9\u00bb\u0003(\u0014\u0000\u00ba\u00b7"+
		"\u0001\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000\u0000\u0000\u00ba\u00b9"+
		"\u0001\u0000\u0000\u0000\u00bb!\u0001\u0000\u0000\u0000\u00bc\u00be\u0005"+
		"*\u0000\u0000\u00bd\u00bc\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000"+
		"\u0000\u0000\u00be\u00c6\u0001\u0000\u0000\u0000\u00bf\u00c7\u0003,\u0016"+
		"\u0000\u00c0\u00c3\u00050\u0000\u0000\u00c1\u00c3\u00030\u0018\u0000\u00c2"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c2\u00c1\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c4\u0001\u0000\u0000\u0000\u00c4\u00c5\u0005\u001c\u0000\u0000\u00c5"+
		"\u00c7\u0007\u0000\u0000\u0000\u00c6\u00bf\u0001\u0000\u0000\u0000\u00c6"+
		"\u00c2\u0001\u0000\u0000\u0000\u00c7\u00cb\u0001\u0000\u0000\u0000\u00c8"+
		"\u00cc\u0003$\u0012\u0000\u00c9\u00cc\u0003&\u0013\u0000\u00ca\u00cc\u0003"+
		"(\u0014\u0000\u00cb\u00c8\u0001\u0000\u0000\u0000\u00cb\u00c9\u0001\u0000"+
		"\u0000\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000\u00cc#\u0001\u0000\u0000"+
		"\u0000\u00cd\u00ce\u0005\u0011\u0000\u0000\u00ce\u00cf\u0007\u0001\u0000"+
		"\u0000\u00cf%\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005\u0012\u0000\u0000"+
		"\u00d1\u00d2\u0005/\u0000\u0000\u00d2\'\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d4\u0005\u0019\u0000\u0000\u00d4)\u0001\u0000\u0000\u0000\u00d5\u00d6"+
		"\u0005\u0007\u0000\u0000\u00d6\u00d9\u0005\u001e\u0000\u0000\u00d7\u00da"+
		"\u00050\u0000\u0000\u00d8\u00da\u0003.\u0017\u0000\u00d9\u00d7\u0001\u0000"+
		"\u0000\u0000\u00d9\u00d8\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000"+
		"\u0000\u0000\u00db\u00dc\u0005\u001c\u0000\u0000\u00dc\u00de\u0007\u0000"+
		"\u0000\u0000\u00dd\u00df\u0003\u0012\t\u0000\u00de\u00dd\u0001\u0000\u0000"+
		"\u0000\u00de\u00df\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000"+
		"\u0000\u00e0\u00e1\u0005\u001d\u0000\u0000\u00e1\u00e2\u0005-\u0000\u0000"+
		"\u00e2\u00e3\u0005\u001d\u0000\u0000\u00e3\u00e4\u0005-\u0000\u0000\u00e4"+
		"\u00e5\u0005\u001d\u0000\u0000\u00e5\u00e6\u0005.\u0000\u0000\u00e6\u00e7"+
		"\u0005\u001f\u0000\u0000\u00e7+\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005"+
		"\u0007\u0000\u0000\u00e9\u00ec\u0005\u001e\u0000\u0000\u00ea\u00ed\u0005"+
		"0\u0000\u0000\u00eb\u00ed\u00030\u0018\u0000\u00ec\u00ea\u0001\u0000\u0000"+
		"\u0000\u00ec\u00eb\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000"+
		"\u0000\u00ee\u00ef\u0005\u001c\u0000\u0000\u00ef\u00f1\u0007\u0000\u0000"+
		"\u0000\u00f0\u00f2\u0003\u0012\t\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000"+
		"\u00f1\u00f2\u0001\u0000\u0000\u0000\u00f2\u00f3\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f4\u0005\u001f\u0000\u0000\u00f4-\u0001\u0000\u0000\u0000\u00f5"+
		"\u00f6\u00051\u0000\u0000\u00f6\u00f7\u0005\"\u0000\u0000\u00f7\u00f8"+
		"\u00050\u0000\u0000\u00f8\u00f9\u0005#\u0000\u0000\u00f9\u00fb\u0005\""+
		"\u0000\u0000\u00fa\u00fc\u00050\u0000\u0000\u00fb\u00fa\u0001\u0000\u0000"+
		"\u0000\u00fb\u00fc\u0001\u0000\u0000\u0000\u00fc\u00fd\u0001\u0000\u0000"+
		"\u0000\u00fd\u00fe\u0005#\u0000\u0000\u00fe\u0108\u0005\"\u0000\u0000"+
		"\u00ff\u0100\u00032\u0019\u0000\u0100\u0101\u0005\u001d\u0000\u0000\u0101"+
		"\u0103\u0001\u0000\u0000\u0000\u0102\u00ff\u0001\u0000\u0000\u0000\u0103"+
		"\u0106\u0001\u0000\u0000\u0000\u0104\u0102\u0001\u0000\u0000\u0000\u0104"+
		"\u0105\u0001\u0000\u0000\u0000\u0105\u0107\u0001\u0000\u0000\u0000\u0106"+
		"\u0104\u0001\u0000\u0000\u0000\u0107\u0109\u00032\u0019\u0000\u0108\u0104"+
		"\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u0109\u010a"+
		"\u0001\u0000\u0000\u0000\u010a\u010b\u0005#\u0000\u0000\u010b\u0115\u0005"+
		"\"\u0000\u0000\u010c\u010d\u00034\u001a\u0000\u010d\u010e\u0005\u001d"+
		"\u0000\u0000\u010e\u0110\u0001\u0000\u0000\u0000\u010f\u010c\u0001\u0000"+
		"\u0000\u0000\u0110\u0113\u0001\u0000\u0000\u0000\u0111\u010f\u0001\u0000"+
		"\u0000\u0000\u0111\u0112\u0001\u0000\u0000\u0000\u0112\u0114\u0001\u0000"+
		"\u0000\u0000\u0113\u0111\u0001\u0000\u0000\u0000\u0114\u0116\u00034\u001a"+
		"\u0000\u0115\u0111\u0001\u0000\u0000\u0000\u0115\u0116\u0001\u0000\u0000"+
		"\u0000\u0116\u0117\u0001\u0000\u0000\u0000\u0117\u0118\u0005#\u0000\u0000"+
		"\u0118\u0119\u0005\"\u0000\u0000\u0119\u011a\u00050\u0000\u0000\u011a"+
		"\u011b\u0005#\u0000\u0000\u011b/\u0001\u0000\u0000\u0000\u011c\u011d\u0005"+
		"1\u0000\u0000\u011d\u011e\u0005\"\u0000\u0000\u011e\u011f\u00050\u0000"+
		"\u0000\u011f\u0120\u0005#\u0000\u0000\u0120\u0122\u0005\"\u0000\u0000"+
		"\u0121\u0123\u00050\u0000\u0000\u0122\u0121\u0001\u0000\u0000\u0000\u0122"+
		"\u0123\u0001\u0000\u0000\u0000\u0123\u0124\u0001\u0000\u0000\u0000\u0124"+
		"\u0125\u0005#\u0000\u0000\u0125\u012f\u0005\"\u0000\u0000\u0126\u0127"+
		"\u00032\u0019\u0000\u0127\u0128\u0005\u001d\u0000\u0000\u0128\u012a\u0001"+
		"\u0000\u0000\u0000\u0129\u0126\u0001\u0000\u0000\u0000\u012a\u012d\u0001"+
		"\u0000\u0000\u0000\u012b\u0129\u0001\u0000\u0000\u0000\u012b\u012c\u0001"+
		"\u0000\u0000\u0000\u012c\u012e\u0001\u0000\u0000\u0000\u012d\u012b\u0001"+
		"\u0000\u0000\u0000\u012e\u0130\u00032\u0019\u0000\u012f\u012b\u0001\u0000"+
		"\u0000\u0000\u012f\u0130\u0001\u0000\u0000\u0000\u0130\u0131\u0001\u0000"+
		"\u0000\u0000\u0131\u0132\u0005#\u0000\u0000\u0132\u013c\u0005\"\u0000"+
		"\u0000\u0133\u0134\u00034\u001a\u0000\u0134\u0135\u0005\u001d\u0000\u0000"+
		"\u0135\u0137\u0001\u0000\u0000\u0000\u0136\u0133\u0001\u0000\u0000\u0000"+
		"\u0137\u013a\u0001\u0000\u0000\u0000\u0138\u0136\u0001\u0000\u0000\u0000"+
		"\u0138\u0139\u0001\u0000\u0000\u0000\u0139\u013b\u0001\u0000\u0000\u0000"+
		"\u013a\u0138\u0001\u0000\u0000\u0000\u013b\u013d\u00034\u001a\u0000\u013c"+
		"\u0138\u0001\u0000\u0000\u0000\u013c\u013d\u0001\u0000\u0000\u0000\u013d"+
		"\u013e\u0001\u0000\u0000\u0000\u013e\u013f\u0005#\u0000\u0000\u013f1\u0001"+
		"\u0000\u0000\u0000\u0140\u0141\u00050\u0000\u0000\u0141\u0142\u0005&\u0000"+
		"\u0000\u0142\u0143\u00050\u0000\u0000\u01433\u0001\u0000\u0000\u0000\u0144"+
		"\u0145\u00050\u0000\u0000\u0145\u0146\u0005\'\u0000\u0000\u0146\u0147"+
		"\u00050\u0000\u0000\u01475\u0001\u0000\u0000\u0000\'8=@GNSX]dhovz\u008a"+
		"\u0092\u009a\u00a2\u00aa\u00b1\u00b4\u00ba\u00bd\u00c2\u00c6\u00cb\u00d9"+
		"\u00de\u00ec\u00f1\u00fb\u0104\u0108\u0111\u0115\u0122\u012b\u012f\u0138"+
		"\u013c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}