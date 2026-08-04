# Generated from ParserRTGL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,329,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,3,0,57,8,0,1,1,1,1,1,1,3,1,62,8,1,1,1,3,1,65,8,1,1,1,1,1,
        1,2,1,2,1,2,3,2,72,8,2,1,2,1,2,1,3,1,3,1,3,3,3,79,8,3,1,3,1,3,1,
        3,3,3,84,8,3,1,4,1,4,1,4,3,4,89,8,4,1,4,1,4,1,4,3,4,94,8,4,1,5,1,
        5,1,5,1,5,1,5,3,5,101,8,5,1,5,1,5,3,5,105,8,5,1,6,1,6,1,6,1,6,1,
        6,3,6,112,8,6,1,6,1,6,1,6,1,6,1,6,3,6,119,8,6,1,6,1,6,3,6,123,8,
        6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,5,10,137,8,
        10,10,10,12,10,140,9,10,1,11,1,11,1,11,5,11,145,8,11,10,11,12,11,
        148,9,11,1,12,1,12,1,12,5,12,153,8,12,10,12,12,12,156,9,12,1,13,
        1,13,1,13,5,13,161,8,13,10,13,12,13,164,9,13,1,14,1,14,1,14,1,14,
        1,14,3,14,171,8,14,1,15,1,15,1,15,1,15,1,15,3,15,178,8,15,1,16,3,
        16,181,8,16,1,16,1,16,1,16,1,16,3,16,187,8,16,1,17,3,17,190,8,17,
        1,17,1,17,1,17,3,17,195,8,17,1,17,1,17,3,17,199,8,17,1,17,1,17,1,
        17,3,17,204,8,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,21,1,
        21,1,21,1,21,3,21,218,8,21,1,21,1,21,1,21,3,21,223,8,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,237,8,22,
        1,22,1,22,1,22,3,22,242,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,252,8,23,1,23,1,23,1,23,1,23,1,23,5,23,259,8,23,10,23,
        12,23,262,9,23,1,23,3,23,265,8,23,1,23,1,23,1,23,1,23,1,23,5,23,
        272,8,23,10,23,12,23,275,9,23,1,23,3,23,278,8,23,1,23,1,23,1,23,
        1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,291,8,24,1,24,1,24,
        1,24,1,24,1,24,5,24,298,8,24,10,24,12,24,301,9,24,1,24,3,24,304,
        8,24,1,24,1,24,1,24,1,24,1,24,5,24,311,8,24,10,24,12,24,314,9,24,
        1,24,3,24,317,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,0,2,2,0,36,36,48,48,1,0,43,45,345,0,56,
        1,0,0,0,2,58,1,0,0,0,4,68,1,0,0,0,6,75,1,0,0,0,8,85,1,0,0,0,10,104,
        1,0,0,0,12,122,1,0,0,0,14,124,1,0,0,0,16,127,1,0,0,0,18,130,1,0,
        0,0,20,133,1,0,0,0,22,141,1,0,0,0,24,149,1,0,0,0,26,157,1,0,0,0,
        28,170,1,0,0,0,30,177,1,0,0,0,32,180,1,0,0,0,34,189,1,0,0,0,36,205,
        1,0,0,0,38,208,1,0,0,0,40,211,1,0,0,0,42,213,1,0,0,0,44,232,1,0,
        0,0,46,245,1,0,0,0,48,284,1,0,0,0,50,320,1,0,0,0,52,324,1,0,0,0,
        54,57,3,2,1,0,55,57,3,4,2,0,56,54,1,0,0,0,56,55,1,0,0,0,57,1,1,0,
        0,0,58,59,3,10,5,0,59,61,3,6,3,0,60,62,3,16,8,0,61,60,1,0,0,0,61,
        62,1,0,0,0,62,64,1,0,0,0,63,65,3,14,7,0,64,63,1,0,0,0,64,65,1,0,
        0,0,65,66,1,0,0,0,66,67,5,37,0,0,67,3,1,0,0,0,68,69,3,12,6,0,69,
        71,3,8,4,0,70,72,3,18,9,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,
        0,0,73,74,5,37,0,0,74,5,1,0,0,0,75,78,5,2,0,0,76,79,5,48,0,0,77,
        79,3,46,23,0,78,76,1,0,0,0,78,77,1,0,0,0,79,80,1,0,0,0,80,81,5,28,
        0,0,81,83,7,0,0,0,82,84,3,18,9,0,83,82,1,0,0,0,83,84,1,0,0,0,84,
        7,1,0,0,0,85,88,5,2,0,0,86,89,5,48,0,0,87,89,3,48,24,0,88,86,1,0,
        0,0,88,87,1,0,0,0,89,90,1,0,0,0,90,91,5,28,0,0,91,93,7,0,0,0,92,
        94,3,18,9,0,93,92,1,0,0,0,93,94,1,0,0,0,94,9,1,0,0,0,95,96,5,3,0,
        0,96,100,3,42,21,0,97,98,5,6,0,0,98,101,5,45,0,0,99,101,5,5,0,0,
        100,97,1,0,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,105,1,0,0,0,102,
        103,5,3,0,0,103,105,3,20,10,0,104,95,1,0,0,0,104,102,1,0,0,0,105,
        11,1,0,0,0,106,107,5,3,0,0,107,111,3,44,22,0,108,109,5,6,0,0,109,
        112,5,45,0,0,110,112,5,5,0,0,111,108,1,0,0,0,111,110,1,0,0,0,111,
        112,1,0,0,0,112,123,1,0,0,0,113,114,5,3,0,0,114,123,3,22,11,0,115,
        118,5,3,0,0,116,119,5,48,0,0,117,119,3,48,24,0,118,116,1,0,0,0,118,
        117,1,0,0,0,119,120,1,0,0,0,120,121,5,28,0,0,121,123,7,0,0,0,122,
        106,1,0,0,0,122,113,1,0,0,0,122,115,1,0,0,0,123,13,1,0,0,0,124,125,
        5,1,0,0,125,126,3,20,10,0,126,15,1,0,0,0,127,128,5,4,0,0,128,129,
        3,20,10,0,129,17,1,0,0,0,130,131,5,4,0,0,131,132,3,22,11,0,132,19,
        1,0,0,0,133,138,3,24,12,0,134,135,5,41,0,0,135,137,3,24,12,0,136,
        134,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,
        21,1,0,0,0,140,138,1,0,0,0,141,146,3,26,13,0,142,143,5,41,0,0,143,
        145,3,26,13,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,
        147,1,0,0,0,147,23,1,0,0,0,148,146,1,0,0,0,149,154,3,28,14,0,150,
        151,5,40,0,0,151,153,3,28,14,0,152,150,1,0,0,0,153,156,1,0,0,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,25,1,0,0,0,156,154,1,0,0,0,157,162,
        3,30,15,0,158,159,5,40,0,0,159,161,3,30,15,0,160,158,1,0,0,0,161,
        164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,27,1,0,0,0,164,162,
        1,0,0,0,165,171,3,32,16,0,166,167,5,30,0,0,167,168,3,20,10,0,168,
        169,5,31,0,0,169,171,1,0,0,0,170,165,1,0,0,0,170,166,1,0,0,0,171,
        29,1,0,0,0,172,178,3,34,17,0,173,174,5,30,0,0,174,175,3,22,11,0,
        175,176,5,31,0,0,176,178,1,0,0,0,177,172,1,0,0,0,177,173,1,0,0,0,
        178,31,1,0,0,0,179,181,5,42,0,0,180,179,1,0,0,0,180,181,1,0,0,0,
        181,182,1,0,0,0,182,186,3,42,21,0,183,187,3,36,18,0,184,187,3,38,
        19,0,185,187,3,40,20,0,186,183,1,0,0,0,186,184,1,0,0,0,186,185,1,
        0,0,0,187,33,1,0,0,0,188,190,5,42,0,0,189,188,1,0,0,0,189,190,1,
        0,0,0,190,198,1,0,0,0,191,199,3,44,22,0,192,195,5,48,0,0,193,195,
        3,48,24,0,194,192,1,0,0,0,194,193,1,0,0,0,195,196,1,0,0,0,196,197,
        5,28,0,0,197,199,7,0,0,0,198,191,1,0,0,0,198,194,1,0,0,0,199,203,
        1,0,0,0,200,204,3,36,18,0,201,204,3,38,19,0,202,204,3,40,20,0,203,
        200,1,0,0,0,203,201,1,0,0,0,203,202,1,0,0,0,204,35,1,0,0,0,205,206,
        5,17,0,0,206,207,7,1,0,0,207,37,1,0,0,0,208,209,5,18,0,0,209,210,
        5,47,0,0,210,39,1,0,0,0,211,212,5,25,0,0,212,41,1,0,0,0,213,214,
        5,7,0,0,214,217,5,30,0,0,215,218,5,48,0,0,216,218,3,46,23,0,217,
        215,1,0,0,0,217,216,1,0,0,0,218,219,1,0,0,0,219,220,5,28,0,0,220,
        222,7,0,0,0,221,223,3,18,9,0,222,221,1,0,0,0,222,223,1,0,0,0,223,
        224,1,0,0,0,224,225,5,29,0,0,225,226,5,45,0,0,226,227,5,29,0,0,227,
        228,5,45,0,0,228,229,5,29,0,0,229,230,5,46,0,0,230,231,5,31,0,0,
        231,43,1,0,0,0,232,233,5,7,0,0,233,236,5,30,0,0,234,237,5,48,0,0,
        235,237,3,48,24,0,236,234,1,0,0,0,236,235,1,0,0,0,237,238,1,0,0,
        0,238,239,5,28,0,0,239,241,7,0,0,0,240,242,3,18,9,0,241,240,1,0,
        0,0,241,242,1,0,0,0,242,243,1,0,0,0,243,244,5,31,0,0,244,45,1,0,
        0,0,245,246,5,49,0,0,246,247,5,34,0,0,247,248,5,48,0,0,248,249,5,
        35,0,0,249,251,5,34,0,0,250,252,5,48,0,0,251,250,1,0,0,0,251,252,
        1,0,0,0,252,253,1,0,0,0,253,254,5,35,0,0,254,264,5,34,0,0,255,256,
        3,50,25,0,256,257,5,29,0,0,257,259,1,0,0,0,258,255,1,0,0,0,259,262,
        1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,263,1,0,0,0,262,260,
        1,0,0,0,263,265,3,50,25,0,264,260,1,0,0,0,264,265,1,0,0,0,265,266,
        1,0,0,0,266,267,5,35,0,0,267,277,5,34,0,0,268,269,3,52,26,0,269,
        270,5,29,0,0,270,272,1,0,0,0,271,268,1,0,0,0,272,275,1,0,0,0,273,
        271,1,0,0,0,273,274,1,0,0,0,274,276,1,0,0,0,275,273,1,0,0,0,276,
        278,3,52,26,0,277,273,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,
        280,5,35,0,0,280,281,5,34,0,0,281,282,5,48,0,0,282,283,5,35,0,0,
        283,47,1,0,0,0,284,285,5,49,0,0,285,286,5,34,0,0,286,287,5,48,0,
        0,287,288,5,35,0,0,288,290,5,34,0,0,289,291,5,48,0,0,290,289,1,0,
        0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,293,5,35,0,0,293,303,5,34,
        0,0,294,295,3,50,25,0,295,296,5,29,0,0,296,298,1,0,0,0,297,294,1,
        0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,302,1,
        0,0,0,301,299,1,0,0,0,302,304,3,50,25,0,303,299,1,0,0,0,303,304,
        1,0,0,0,304,305,1,0,0,0,305,306,5,35,0,0,306,316,5,34,0,0,307,308,
        3,52,26,0,308,309,5,29,0,0,309,311,1,0,0,0,310,307,1,0,0,0,311,314,
        1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,315,1,0,0,0,314,312,
        1,0,0,0,315,317,3,52,26,0,316,312,1,0,0,0,316,317,1,0,0,0,317,318,
        1,0,0,0,318,319,5,35,0,0,319,49,1,0,0,0,320,321,5,48,0,0,321,322,
        5,38,0,0,322,323,5,48,0,0,323,51,1,0,0,0,324,325,5,48,0,0,325,326,
        5,39,0,0,326,327,5,48,0,0,327,53,1,0,0,0,39,56,61,64,71,78,83,88,
        93,100,104,111,118,122,138,146,154,162,170,177,180,186,189,194,198,
        203,217,222,236,241,251,260,264,273,277,290,299,303,312,316
    ]

class ParserRTGL ( Parser ):

    grammarFileName = "ParserRTGL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "','", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'*'", "';'", "'->'", "':'" ]

    symbolicNames = [ "<INVALID>", "ASSUMING", "FOR_EACH", "PREDICT", "WHERE", 
                      "CLASSIFY", "RANK_TOP", "AGGR_FUNC", "AVG", "COUNT", 
                      "COUNT_DISTINCT", "FIRST", "LAST", "LIST_DISTINCT", 
                      "MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", 
                      "NOT_LIKE", "NOT_CONTAINS", "ENDS_WITH", "STARTS_WITH", 
                      "LIKE", "CONTAINS", "NULL_CHECK_OP", "IS_NOT_NULL", 
                      "IS_NULL", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                      "STAR", "SEMICOLON", "ARROW", "COLON", "AND", "OR", 
                      "NOT", "DATETIME", "FLOAT", "INT", "TIME_MEASURE_UNIT", 
                      "STRING", "ID", "SQL_INJECTION_BODY", "WS_SKIP", "ANY" ]

    RULE_query = 0
    RULE_query_tmp = 1
    RULE_query_stat = 2
    RULE_for_each_tmp = 3
    RULE_for_each_stat = 4
    RULE_predict_tmp = 5
    RULE_predict_stat = 6
    RULE_assuming = 7
    RULE_where_tmp = 8
    RULE_where_stat = 9
    RULE_expr_or_tmp = 10
    RULE_expr_or_stat = 11
    RULE_expr_and_tmp = 12
    RULE_expr_and_stat = 13
    RULE_expr_term_tmp = 14
    RULE_expr_term_stat = 15
    RULE_condition_tmp = 16
    RULE_condition_stat = 17
    RULE_num_condition = 18
    RULE_str_condition = 19
    RULE_null_check_condition = 20
    RULE_aggregation_tmp = 21
    RULE_aggregation_stat = 22
    RULE_sql_injection_tmp = 23
    RULE_sql_injection_stat = 24
    RULE_fk_col_to_pk_table = 25
    RULE_fk_table_col = 26

    ruleNames =  [ "query", "query_tmp", "query_stat", "for_each_tmp", "for_each_stat", 
                   "predict_tmp", "predict_stat", "assuming", "where_tmp", 
                   "where_stat", "expr_or_tmp", "expr_or_stat", "expr_and_tmp", 
                   "expr_and_stat", "expr_term_tmp", "expr_term_stat", "condition_tmp", 
                   "condition_stat", "num_condition", "str_condition", "null_check_condition", 
                   "aggregation_tmp", "aggregation_stat", "sql_injection_tmp", 
                   "sql_injection_stat", "fk_col_to_pk_table", "fk_table_col" ]

    EOF = Token.EOF
    ASSUMING=1
    FOR_EACH=2
    PREDICT=3
    WHERE=4
    CLASSIFY=5
    RANK_TOP=6
    AGGR_FUNC=7
    AVG=8
    COUNT=9
    COUNT_DISTINCT=10
    FIRST=11
    LAST=12
    LIST_DISTINCT=13
    MAX=14
    MIN=15
    SUM=16
    NUM_COMP_OP=17
    STR_COMP_OP=18
    NOT_LIKE=19
    NOT_CONTAINS=20
    ENDS_WITH=21
    STARTS_WITH=22
    LIKE=23
    CONTAINS=24
    NULL_CHECK_OP=25
    IS_NOT_NULL=26
    IS_NULL=27
    DOT=28
    COMMA=29
    OPEN_PAREN=30
    CLOSE_PAREN=31
    OPEN_BRACKET=32
    CLOSE_BRACKET=33
    OPEN_BRACE=34
    CLOSE_BRACE=35
    STAR=36
    SEMICOLON=37
    ARROW=38
    COLON=39
    AND=40
    OR=41
    NOT=42
    DATETIME=43
    FLOAT=44
    INT=45
    TIME_MEASURE_UNIT=46
    STRING=47
    ID=48
    SQL_INJECTION_BODY=49
    WS_SKIP=50
    ANY=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Query_tmpContext,0)


        def query_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Query_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = ParserRTGL.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.query_tmp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.query_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predict_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Predict_tmpContext,0)


        def for_each_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.For_each_tmpContext,0)


        def SEMICOLON(self):
            return self.getToken(ParserRTGL.SEMICOLON, 0)

        def where_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Where_tmpContext,0)


        def assuming(self):
            return self.getTypedRuleContext(ParserRTGL.AssumingContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_query_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_tmp" ):
                listener.enterQuery_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_tmp" ):
                listener.exitQuery_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_tmp" ):
                return visitor.visitQuery_tmp(self)
            else:
                return visitor.visitChildren(self)




    def query_tmp(self):

        localctx = ParserRTGL.Query_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.predict_tmp()
            self.state = 59
            self.for_each_tmp()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 60
                self.where_tmp()


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 63
                self.assuming()


            self.state = 66
            self.match(ParserRTGL.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predict_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Predict_statContext,0)


        def for_each_stat(self):
            return self.getTypedRuleContext(ParserRTGL.For_each_statContext,0)


        def SEMICOLON(self):
            return self.getToken(ParserRTGL.SEMICOLON, 0)

        def where_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_query_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_stat" ):
                listener.enterQuery_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_stat" ):
                listener.exitQuery_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_stat" ):
                return visitor.visitQuery_stat(self)
            else:
                return visitor.visitChildren(self)




    def query_stat(self):

        localctx = ParserRTGL.Query_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.predict_stat()
            self.state = 69
            self.for_each_stat()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 70
                self.where_stat()


            self.state = 73
            self.match(ParserRTGL.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_each_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_EACH(self):
            return self.getToken(ParserRTGL.FOR_EACH, 0)

        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def sql_injection_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_tmpContext,0)


        def where_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_for_each_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_each_tmp" ):
                listener.enterFor_each_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_each_tmp" ):
                listener.exitFor_each_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each_tmp" ):
                return visitor.visitFor_each_tmp(self)
            else:
                return visitor.visitChildren(self)




    def for_each_tmp(self):

        localctx = ParserRTGL.For_each_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_for_each_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ParserRTGL.FOR_EACH)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 76
                self.match(ParserRTGL.ID)
                pass
            elif token in [49]:
                self.state = 77
                self.sql_injection_tmp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 80
            self.match(ParserRTGL.DOT)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==36 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 82
                self.where_stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_each_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_EACH(self):
            return self.getToken(ParserRTGL.FOR_EACH, 0)

        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def sql_injection_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_statContext,0)


        def where_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_for_each_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_each_stat" ):
                listener.enterFor_each_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_each_stat" ):
                listener.exitFor_each_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each_stat" ):
                return visitor.visitFor_each_stat(self)
            else:
                return visitor.visitChildren(self)




    def for_each_stat(self):

        localctx = ParserRTGL.For_each_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_for_each_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ParserRTGL.FOR_EACH)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 86
                self.match(ParserRTGL.ID)
                pass
            elif token in [49]:
                self.state = 87
                self.sql_injection_stat()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 90
            self.match(ParserRTGL.DOT)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==36 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 92
                self.where_stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predict_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(ParserRTGL.PREDICT, 0)

        def aggregation_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Aggregation_tmpContext,0)


        def RANK_TOP(self):
            return self.getToken(ParserRTGL.RANK_TOP, 0)

        def INT(self):
            return self.getToken(ParserRTGL.INT, 0)

        def CLASSIFY(self):
            return self.getToken(ParserRTGL.CLASSIFY, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_tmpContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_predict_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredict_tmp" ):
                listener.enterPredict_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredict_tmp" ):
                listener.exitPredict_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredict_tmp" ):
                return visitor.visitPredict_tmp(self)
            else:
                return visitor.visitChildren(self)




    def predict_tmp(self):

        localctx = ParserRTGL.Predict_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predict_tmp)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(ParserRTGL.PREDICT)
                self.state = 96
                self.aggregation_tmp()
                self.state = 100
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 97
                    self.match(ParserRTGL.RANK_TOP)
                    self.state = 98
                    self.match(ParserRTGL.INT)
                    pass
                elif token in [5]:
                    self.state = 99
                    self.match(ParserRTGL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ParserRTGL.PREDICT)
                self.state = 103
                self.expr_or_tmp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predict_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(ParserRTGL.PREDICT, 0)

        def aggregation_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Aggregation_statContext,0)


        def RANK_TOP(self):
            return self.getToken(ParserRTGL.RANK_TOP, 0)

        def INT(self):
            return self.getToken(ParserRTGL.INT, 0)

        def CLASSIFY(self):
            return self.getToken(ParserRTGL.CLASSIFY, 0)

        def expr_or_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_statContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def sql_injection_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_predict_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredict_stat" ):
                listener.enterPredict_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredict_stat" ):
                listener.exitPredict_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredict_stat" ):
                return visitor.visitPredict_stat(self)
            else:
                return visitor.visitChildren(self)




    def predict_stat(self):

        localctx = ParserRTGL.Predict_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_predict_stat)
        self._la = 0 # Token type
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(ParserRTGL.PREDICT)
                self.state = 107
                self.aggregation_stat()
                self.state = 111
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 108
                    self.match(ParserRTGL.RANK_TOP)
                    self.state = 109
                    self.match(ParserRTGL.INT)
                    pass
                elif token in [5]:
                    self.state = 110
                    self.match(ParserRTGL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(ParserRTGL.PREDICT)
                self.state = 114
                self.expr_or_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(ParserRTGL.PREDICT)
                self.state = 118
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [48]:
                    self.state = 116
                    self.match(ParserRTGL.ID)
                    pass
                elif token in [49]:
                    self.state = 117
                    self.sql_injection_stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 120
                self.match(ParserRTGL.DOT)
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==36 or _la==48):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssumingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSUMING(self):
            return self.getToken(ParserRTGL.ASSUMING, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_tmpContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_assuming

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssuming" ):
                listener.enterAssuming(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssuming" ):
                listener.exitAssuming(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssuming" ):
                return visitor.visitAssuming(self)
            else:
                return visitor.visitChildren(self)




    def assuming(self):

        localctx = ParserRTGL.AssumingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assuming)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ParserRTGL.ASSUMING)
            self.state = 125
            self.expr_or_tmp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(ParserRTGL.WHERE, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_tmpContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_where_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_tmp" ):
                listener.enterWhere_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_tmp" ):
                listener.exitWhere_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_tmp" ):
                return visitor.visitWhere_tmp(self)
            else:
                return visitor.visitChildren(self)




    def where_tmp(self):

        localctx = ParserRTGL.Where_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where_tmp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ParserRTGL.WHERE)
            self.state = 128
            self.expr_or_tmp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(ParserRTGL.WHERE, 0)

        def expr_or_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_where_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_stat" ):
                listener.enterWhere_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_stat" ):
                listener.exitWhere_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_stat" ):
                return visitor.visitWhere_stat(self)
            else:
                return visitor.visitChildren(self)




    def where_stat(self):

        localctx = ParserRTGL.Where_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_where_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ParserRTGL.WHERE)
            self.state = 131
            self.expr_or_stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_or_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_and_tmp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Expr_and_tmpContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Expr_and_tmpContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.OR)
            else:
                return self.getToken(ParserRTGL.OR, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_expr_or_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_or_tmp" ):
                listener.enterExpr_or_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_or_tmp" ):
                listener.exitExpr_or_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or_tmp" ):
                return visitor.visitExpr_or_tmp(self)
            else:
                return visitor.visitChildren(self)




    def expr_or_tmp(self):

        localctx = ParserRTGL.Expr_or_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_or_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.expr_and_tmp()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 134
                self.match(ParserRTGL.OR)
                self.state = 135
                self.expr_and_tmp()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_or_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_and_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Expr_and_statContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Expr_and_statContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.OR)
            else:
                return self.getToken(ParserRTGL.OR, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_expr_or_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_or_stat" ):
                listener.enterExpr_or_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_or_stat" ):
                listener.exitExpr_or_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or_stat" ):
                return visitor.visitExpr_or_stat(self)
            else:
                return visitor.visitChildren(self)




    def expr_or_stat(self):

        localctx = ParserRTGL.Expr_or_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_or_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.expr_and_stat()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 142
                self.match(ParserRTGL.OR)
                self.state = 143
                self.expr_and_stat()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_and_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_term_tmp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Expr_term_tmpContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Expr_term_tmpContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.AND)
            else:
                return self.getToken(ParserRTGL.AND, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_expr_and_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and_tmp" ):
                listener.enterExpr_and_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and_tmp" ):
                listener.exitExpr_and_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and_tmp" ):
                return visitor.visitExpr_and_tmp(self)
            else:
                return visitor.visitChildren(self)




    def expr_and_tmp(self):

        localctx = ParserRTGL.Expr_and_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr_and_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.expr_term_tmp()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 150
                self.match(ParserRTGL.AND)
                self.state = 151
                self.expr_term_tmp()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_and_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_term_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Expr_term_statContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Expr_term_statContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.AND)
            else:
                return self.getToken(ParserRTGL.AND, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_expr_and_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and_stat" ):
                listener.enterExpr_and_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and_stat" ):
                listener.exitExpr_and_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and_stat" ):
                return visitor.visitExpr_and_stat(self)
            else:
                return visitor.visitChildren(self)




    def expr_and_stat(self):

        localctx = ParserRTGL.Expr_and_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr_and_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.expr_term_stat()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 158
                self.match(ParserRTGL.AND)
                self.state = 159
                self.expr_term_stat()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_term_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Condition_tmpContext,0)


        def OPEN_PAREN(self):
            return self.getToken(ParserRTGL.OPEN_PAREN, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_tmpContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_expr_term_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_tmp" ):
                listener.enterExpr_term_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_tmp" ):
                listener.exitExpr_term_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_tmp" ):
                return visitor.visitExpr_term_tmp(self)
            else:
                return visitor.visitChildren(self)




    def expr_term_tmp(self):

        localctx = ParserRTGL.Expr_term_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_term_tmp)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.condition_tmp()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(ParserRTGL.OPEN_PAREN)
                self.state = 167
                self.expr_or_tmp()
                self.state = 168
                self.match(ParserRTGL.CLOSE_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_term_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Condition_statContext,0)


        def OPEN_PAREN(self):
            return self.getToken(ParserRTGL.OPEN_PAREN, 0)

        def expr_or_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Expr_or_statContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_expr_term_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_stat" ):
                listener.enterExpr_term_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_stat" ):
                listener.exitExpr_term_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_stat" ):
                return visitor.visitExpr_term_stat(self)
            else:
                return visitor.visitChildren(self)




    def expr_term_stat(self):

        localctx = ParserRTGL.Expr_term_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_term_stat)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 42, 48, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.condition_stat()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(ParserRTGL.OPEN_PAREN)
                self.state = 174
                self.expr_or_stat()
                self.state = 175
                self.match(ParserRTGL.CLOSE_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregation_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Aggregation_tmpContext,0)


        def num_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Null_check_conditionContext,0)


        def NOT(self):
            return self.getToken(ParserRTGL.NOT, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_condition_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_tmp" ):
                listener.enterCondition_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_tmp" ):
                listener.exitCondition_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_tmp" ):
                return visitor.visitCondition_tmp(self)
            else:
                return visitor.visitChildren(self)




    def condition_tmp(self):

        localctx = ParserRTGL.Condition_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 179
                self.match(ParserRTGL.NOT)


            self.state = 182
            self.aggregation_tmp()
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 183
                self.num_condition()
                pass
            elif token in [18]:
                self.state = 184
                self.str_condition()
                pass
            elif token in [25]:
                self.state = 185
                self.null_check_condition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregation_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Aggregation_statContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def num_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Null_check_conditionContext,0)


        def NOT(self):
            return self.getToken(ParserRTGL.NOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def sql_injection_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_condition_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_stat" ):
                listener.enterCondition_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_stat" ):
                listener.exitCondition_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_stat" ):
                return visitor.visitCondition_stat(self)
            else:
                return visitor.visitChildren(self)




    def condition_stat(self):

        localctx = ParserRTGL.Condition_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condition_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 188
                self.match(ParserRTGL.NOT)


            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 191
                self.aggregation_stat()
                pass
            elif token in [48, 49]:
                self.state = 194
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [48]:
                    self.state = 192
                    self.match(ParserRTGL.ID)
                    pass
                elif token in [49]:
                    self.state = 193
                    self.sql_injection_stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 196
                self.match(ParserRTGL.DOT)
                self.state = 197
                _la = self._input.LA(1)
                if not(_la==36 or _la==48):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 200
                self.num_condition()
                pass
            elif token in [18]:
                self.state = 201
                self.str_condition()
                pass
            elif token in [25]:
                self.state = 202
                self.null_check_condition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_COMP_OP(self):
            return self.getToken(ParserRTGL.NUM_COMP_OP, 0)

        def DATETIME(self):
            return self.getToken(ParserRTGL.DATETIME, 0)

        def FLOAT(self):
            return self.getToken(ParserRTGL.FLOAT, 0)

        def INT(self):
            return self.getToken(ParserRTGL.INT, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_num_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum_condition" ):
                listener.enterNum_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum_condition" ):
                listener.exitNum_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_condition" ):
                return visitor.visitNum_condition(self)
            else:
                return visitor.visitChildren(self)




    def num_condition(self):

        localctx = ParserRTGL.Num_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_num_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ParserRTGL.NUM_COMP_OP)
            self.state = 206
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61572651155456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_COMP_OP(self):
            return self.getToken(ParserRTGL.STR_COMP_OP, 0)

        def STRING(self):
            return self.getToken(ParserRTGL.STRING, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_str_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_condition" ):
                listener.enterStr_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_condition" ):
                listener.exitStr_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_condition" ):
                return visitor.visitStr_condition(self)
            else:
                return visitor.visitChildren(self)




    def str_condition(self):

        localctx = ParserRTGL.Str_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_str_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ParserRTGL.STR_COMP_OP)
            self.state = 209
            self.match(ParserRTGL.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_check_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_CHECK_OP(self):
            return self.getToken(ParserRTGL.NULL_CHECK_OP, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_null_check_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNull_check_condition" ):
                listener.enterNull_check_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNull_check_condition" ):
                listener.exitNull_check_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull_check_condition" ):
                return visitor.visitNull_check_condition(self)
            else:
                return visitor.visitChildren(self)




    def null_check_condition(self):

        localctx = ParserRTGL.Null_check_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_null_check_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ParserRTGL.NULL_CHECK_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregation_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGR_FUNC(self):
            return self.getToken(ParserRTGL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserRTGL.OPEN_PAREN, 0)

        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.COMMA)
            else:
                return self.getToken(ParserRTGL.COMMA, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.INT)
            else:
                return self.getToken(ParserRTGL.INT, i)

        def TIME_MEASURE_UNIT(self):
            return self.getToken(ParserRTGL.TIME_MEASURE_UNIT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def sql_injection_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_tmpContext,0)


        def where_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_aggregation_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation_tmp" ):
                listener.enterAggregation_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation_tmp" ):
                listener.exitAggregation_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation_tmp" ):
                return visitor.visitAggregation_tmp(self)
            else:
                return visitor.visitChildren(self)




    def aggregation_tmp(self):

        localctx = ParserRTGL.Aggregation_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_aggregation_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ParserRTGL.AGGR_FUNC)
            self.state = 214
            self.match(ParserRTGL.OPEN_PAREN)
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 215
                self.match(ParserRTGL.ID)
                pass
            elif token in [49]:
                self.state = 216
                self.sql_injection_tmp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 219
            self.match(ParserRTGL.DOT)
            self.state = 220
            _la = self._input.LA(1)
            if not(_la==36 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 221
                self.where_stat()


            self.state = 224
            self.match(ParserRTGL.COMMA)
            self.state = 225
            self.match(ParserRTGL.INT)
            self.state = 226
            self.match(ParserRTGL.COMMA)
            self.state = 227
            self.match(ParserRTGL.INT)
            self.state = 228
            self.match(ParserRTGL.COMMA)
            self.state = 229
            self.match(ParserRTGL.TIME_MEASURE_UNIT)
            self.state = 230
            self.match(ParserRTGL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregation_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGR_FUNC(self):
            return self.getToken(ParserRTGL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserRTGL.OPEN_PAREN, 0)

        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def sql_injection_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_statContext,0)


        def where_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_aggregation_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation_stat" ):
                listener.enterAggregation_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation_stat" ):
                listener.exitAggregation_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation_stat" ):
                return visitor.visitAggregation_stat(self)
            else:
                return visitor.visitChildren(self)




    def aggregation_stat(self):

        localctx = ParserRTGL.Aggregation_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_aggregation_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(ParserRTGL.AGGR_FUNC)
            self.state = 233
            self.match(ParserRTGL.OPEN_PAREN)
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 234
                self.match(ParserRTGL.ID)
                pass
            elif token in [49]:
                self.state = 235
                self.sql_injection_stat()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 238
            self.match(ParserRTGL.DOT)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==36 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 240
                self.where_stat()


            self.state = 243
            self.match(ParserRTGL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_injection_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL_INJECTION_BODY(self):
            return self.getToken(ParserRTGL.SQL_INJECTION_BODY, 0)

        def OPEN_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.OPEN_BRACE)
            else:
                return self.getToken(ParserRTGL.OPEN_BRACE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def CLOSE_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.CLOSE_BRACE)
            else:
                return self.getToken(ParserRTGL.CLOSE_BRACE, i)

        def fk_col_to_pk_table(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fk_col_to_pk_tableContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fk_col_to_pk_tableContext,i)


        def fk_table_col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fk_table_colContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fk_table_colContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.COMMA)
            else:
                return self.getToken(ParserRTGL.COMMA, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_sql_injection_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_injection_tmp" ):
                listener.enterSql_injection_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_injection_tmp" ):
                listener.exitSql_injection_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_injection_tmp" ):
                return visitor.visitSql_injection_tmp(self)
            else:
                return visitor.visitChildren(self)




    def sql_injection_tmp(self):

        localctx = ParserRTGL.Sql_injection_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sql_injection_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ParserRTGL.SQL_INJECTION_BODY)
            self.state = 246
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 247
            self.match(ParserRTGL.ID)
            self.state = 248
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 249
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 250
                self.match(ParserRTGL.ID)


            self.state = 253
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 254
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 255
                        self.fk_col_to_pk_table()
                        self.state = 256
                        self.match(ParserRTGL.COMMA) 
                    self.state = 262
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                self.state = 263
                self.fk_col_to_pk_table()


            self.state = 266
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 267
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 268
                        self.fk_table_col()
                        self.state = 269
                        self.match(ParserRTGL.COMMA) 
                    self.state = 275
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 276
                self.fk_table_col()


            self.state = 279
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 280
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 281
            self.match(ParserRTGL.ID)
            self.state = 282
            self.match(ParserRTGL.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_injection_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL_INJECTION_BODY(self):
            return self.getToken(ParserRTGL.SQL_INJECTION_BODY, 0)

        def OPEN_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.OPEN_BRACE)
            else:
                return self.getToken(ParserRTGL.OPEN_BRACE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def CLOSE_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.CLOSE_BRACE)
            else:
                return self.getToken(ParserRTGL.CLOSE_BRACE, i)

        def fk_col_to_pk_table(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fk_col_to_pk_tableContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fk_col_to_pk_tableContext,i)


        def fk_table_col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fk_table_colContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fk_table_colContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.COMMA)
            else:
                return self.getToken(ParserRTGL.COMMA, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_sql_injection_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_injection_stat" ):
                listener.enterSql_injection_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_injection_stat" ):
                listener.exitSql_injection_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_injection_stat" ):
                return visitor.visitSql_injection_stat(self)
            else:
                return visitor.visitChildren(self)




    def sql_injection_stat(self):

        localctx = ParserRTGL.Sql_injection_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sql_injection_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ParserRTGL.SQL_INJECTION_BODY)
            self.state = 285
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 286
            self.match(ParserRTGL.ID)
            self.state = 287
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 288
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 289
                self.match(ParserRTGL.ID)


            self.state = 292
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 293
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 294
                        self.fk_col_to_pk_table()
                        self.state = 295
                        self.match(ParserRTGL.COMMA) 
                    self.state = 301
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                self.state = 302
                self.fk_col_to_pk_table()


            self.state = 305
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 306
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 307
                        self.fk_table_col()
                        self.state = 308
                        self.match(ParserRTGL.COMMA) 
                    self.state = 314
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                self.state = 315
                self.fk_table_col()


            self.state = 318
            self.match(ParserRTGL.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fk_col_to_pk_tableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def ARROW(self):
            return self.getToken(ParserRTGL.ARROW, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_fk_col_to_pk_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFk_col_to_pk_table" ):
                listener.enterFk_col_to_pk_table(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFk_col_to_pk_table" ):
                listener.exitFk_col_to_pk_table(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFk_col_to_pk_table" ):
                return visitor.visitFk_col_to_pk_table(self)
            else:
                return visitor.visitChildren(self)




    def fk_col_to_pk_table(self):

        localctx = ParserRTGL.Fk_col_to_pk_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fk_col_to_pk_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ParserRTGL.ID)
            self.state = 321
            self.match(ParserRTGL.ARROW)
            self.state = 322
            self.match(ParserRTGL.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fk_table_colContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def COLON(self):
            return self.getToken(ParserRTGL.COLON, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_fk_table_col

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFk_table_col" ):
                listener.enterFk_table_col(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFk_table_col" ):
                listener.exitFk_table_col(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFk_table_col" ):
                return visitor.visitFk_table_col(self)
            else:
                return visitor.visitChildren(self)




    def fk_table_col(self):

        localctx = ParserRTGL.Fk_table_colContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fk_table_col)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ParserRTGL.ID)
            self.state = 325
            self.match(ParserRTGL.COLON)
            self.state = 326
            self.match(ParserRTGL.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





