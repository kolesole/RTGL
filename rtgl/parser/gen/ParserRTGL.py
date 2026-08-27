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
        4,1,53,369,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,3,0,69,8,0,1,1,3,1,72,8,1,1,1,1,1,1,1,3,1,77,8,1,1,1,3,1,80,
        8,1,1,1,1,1,1,2,3,2,85,8,2,1,2,1,2,1,2,3,2,90,8,2,1,2,1,2,1,3,1,
        3,1,3,1,3,5,3,98,8,3,10,3,12,3,101,9,3,1,4,1,4,1,4,1,4,1,4,1,4,4,
        4,109,8,4,11,4,12,4,110,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,120,8,5,
        1,6,1,6,1,6,1,6,1,6,3,6,127,8,6,1,7,1,7,1,7,1,7,1,7,3,7,134,8,7,
        1,8,1,8,1,8,1,8,1,8,3,8,141,8,8,1,8,1,8,3,8,145,8,8,1,9,1,9,1,9,
        1,9,1,9,3,9,152,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,161,8,9,1,10,
        1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,5,13,175,
        8,13,10,13,12,13,178,9,13,1,14,1,14,1,14,5,14,183,8,14,10,14,12,
        14,186,9,14,1,15,1,15,1,15,5,15,191,8,15,10,15,12,15,194,9,15,1,
        16,1,16,1,16,5,16,199,8,16,10,16,12,16,202,9,16,1,17,1,17,1,17,1,
        17,1,17,3,17,209,8,17,1,18,1,18,1,18,1,18,1,18,3,18,216,8,18,1,19,
        3,19,219,8,19,1,19,1,19,1,19,1,19,3,19,225,8,19,1,20,3,20,228,8,
        20,1,20,1,20,1,20,1,20,1,20,3,20,235,8,20,1,20,1,20,1,20,3,20,240,
        8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,256,8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,25,3,25,272,8,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,3,26,282,8,26,1,26,1,26,1,26,1,26,1,26,5,26,
        289,8,26,10,26,12,26,292,9,26,1,26,3,26,295,8,26,1,26,1,26,1,26,
        1,26,1,26,5,26,302,8,26,10,26,12,26,305,9,26,1,26,3,26,308,8,26,
        1,26,1,26,1,26,3,26,313,8,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,27,3,27,323,8,27,1,27,1,27,1,27,1,27,1,27,5,27,330,8,27,10,27,
        12,27,333,9,27,3,27,335,8,27,1,27,1,27,1,27,1,27,1,27,5,27,342,8,
        27,10,27,12,27,345,9,27,3,27,347,8,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,1,29,1,30,1,30,3,30,361,8,30,1,31,1,31,3,31,365,
        8,31,1,32,1,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,2,1,0,
        45,47,2,0,38,38,50,50,381,0,68,1,0,0,0,2,71,1,0,0,0,4,84,1,0,0,0,
        6,93,1,0,0,0,8,102,1,0,0,0,10,114,1,0,0,0,12,121,1,0,0,0,14,128,
        1,0,0,0,16,144,1,0,0,0,18,160,1,0,0,0,20,162,1,0,0,0,22,165,1,0,
        0,0,24,168,1,0,0,0,26,171,1,0,0,0,28,179,1,0,0,0,30,187,1,0,0,0,
        32,195,1,0,0,0,34,208,1,0,0,0,36,215,1,0,0,0,38,218,1,0,0,0,40,227,
        1,0,0,0,42,241,1,0,0,0,44,244,1,0,0,0,46,247,1,0,0,0,48,249,1,0,
        0,0,50,265,1,0,0,0,52,275,1,0,0,0,54,316,1,0,0,0,56,350,1,0,0,0,
        58,354,1,0,0,0,60,360,1,0,0,0,62,364,1,0,0,0,64,366,1,0,0,0,66,69,
        3,2,1,0,67,69,3,4,2,0,68,66,1,0,0,0,68,67,1,0,0,0,69,1,1,0,0,0,70,
        72,3,6,3,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,3,16,
        8,0,74,76,3,12,6,0,75,77,3,20,10,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        79,1,0,0,0,78,80,3,24,12,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,
        0,0,81,82,5,39,0,0,82,3,1,0,0,0,83,85,3,6,3,0,84,83,1,0,0,0,84,85,
        1,0,0,0,85,86,1,0,0,0,86,87,3,18,9,0,87,89,3,14,7,0,88,90,3,22,11,
        0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,39,0,0,92,5,
        1,0,0,0,93,94,5,1,0,0,94,99,3,8,4,0,95,96,5,31,0,0,96,98,3,8,4,0,
        97,95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,7,
        1,0,0,0,101,99,1,0,0,0,102,103,5,50,0,0,103,104,5,6,0,0,104,105,
        5,32,0,0,105,108,3,10,5,0,106,107,5,40,0,0,107,109,3,10,5,0,108,
        106,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,
        112,1,0,0,0,112,113,5,33,0,0,113,9,1,0,0,0,114,115,5,50,0,0,115,
        116,5,30,0,0,116,119,5,50,0,0,117,118,5,41,0,0,118,120,5,50,0,0,
        119,117,1,0,0,0,119,120,1,0,0,0,120,11,1,0,0,0,121,122,5,2,0,0,122,
        123,3,60,30,0,123,124,5,30,0,0,124,126,3,64,32,0,125,127,3,22,11,
        0,126,125,1,0,0,0,126,127,1,0,0,0,127,13,1,0,0,0,128,129,5,2,0,0,
        129,130,3,62,31,0,130,131,5,30,0,0,131,133,3,64,32,0,132,134,3,22,
        11,0,133,132,1,0,0,0,133,134,1,0,0,0,134,15,1,0,0,0,135,136,5,3,
        0,0,136,140,3,48,24,0,137,138,5,8,0,0,138,141,5,47,0,0,139,141,5,
        7,0,0,140,137,1,0,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,145,1,
        0,0,0,142,143,5,3,0,0,143,145,3,26,13,0,144,135,1,0,0,0,144,142,
        1,0,0,0,145,17,1,0,0,0,146,147,5,3,0,0,147,151,3,50,25,0,148,149,
        5,8,0,0,149,152,5,47,0,0,150,152,5,7,0,0,151,148,1,0,0,0,151,150,
        1,0,0,0,151,152,1,0,0,0,152,161,1,0,0,0,153,154,5,3,0,0,154,161,
        3,28,14,0,155,156,5,3,0,0,156,157,3,62,31,0,157,158,5,30,0,0,158,
        159,3,64,32,0,159,161,1,0,0,0,160,146,1,0,0,0,160,153,1,0,0,0,160,
        155,1,0,0,0,161,19,1,0,0,0,162,163,5,4,0,0,163,164,3,26,13,0,164,
        21,1,0,0,0,165,166,5,4,0,0,166,167,3,28,14,0,167,23,1,0,0,0,168,
        169,5,5,0,0,169,170,3,26,13,0,170,25,1,0,0,0,171,176,3,30,15,0,172,
        173,5,43,0,0,173,175,3,30,15,0,174,172,1,0,0,0,175,178,1,0,0,0,176,
        174,1,0,0,0,176,177,1,0,0,0,177,27,1,0,0,0,178,176,1,0,0,0,179,184,
        3,32,16,0,180,181,5,43,0,0,181,183,3,32,16,0,182,180,1,0,0,0,183,
        186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,29,1,0,0,0,186,184,
        1,0,0,0,187,192,3,34,17,0,188,189,5,42,0,0,189,191,3,34,17,0,190,
        188,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,
        31,1,0,0,0,194,192,1,0,0,0,195,200,3,36,18,0,196,197,5,42,0,0,197,
        199,3,36,18,0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,
        201,1,0,0,0,201,33,1,0,0,0,202,200,1,0,0,0,203,209,3,38,19,0,204,
        205,5,32,0,0,205,206,3,26,13,0,206,207,5,33,0,0,207,209,1,0,0,0,
        208,203,1,0,0,0,208,204,1,0,0,0,209,35,1,0,0,0,210,216,3,40,20,0,
        211,212,5,32,0,0,212,213,3,28,14,0,213,214,5,33,0,0,214,216,1,0,
        0,0,215,210,1,0,0,0,215,211,1,0,0,0,216,37,1,0,0,0,217,219,5,44,
        0,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,224,3,48,
        24,0,221,225,3,42,21,0,222,225,3,44,22,0,223,225,3,46,23,0,224,221,
        1,0,0,0,224,222,1,0,0,0,224,223,1,0,0,0,225,39,1,0,0,0,226,228,5,
        44,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,234,1,0,0,0,229,235,3,
        50,25,0,230,231,3,62,31,0,231,232,5,30,0,0,232,233,3,64,32,0,233,
        235,1,0,0,0,234,229,1,0,0,0,234,230,1,0,0,0,235,239,1,0,0,0,236,
        240,3,42,21,0,237,240,3,44,22,0,238,240,3,46,23,0,239,236,1,0,0,
        0,239,237,1,0,0,0,239,238,1,0,0,0,240,41,1,0,0,0,241,242,5,19,0,
        0,242,243,7,0,0,0,243,43,1,0,0,0,244,245,5,20,0,0,245,246,5,49,0,
        0,246,45,1,0,0,0,247,248,5,27,0,0,248,47,1,0,0,0,249,250,5,9,0,0,
        250,251,5,32,0,0,251,252,3,60,30,0,252,253,5,30,0,0,253,255,3,64,
        32,0,254,256,3,22,11,0,255,254,1,0,0,0,255,256,1,0,0,0,256,257,1,
        0,0,0,257,258,5,31,0,0,258,259,5,47,0,0,259,260,5,31,0,0,260,261,
        5,47,0,0,261,262,5,31,0,0,262,263,5,48,0,0,263,264,5,33,0,0,264,
        49,1,0,0,0,265,266,5,9,0,0,266,267,5,32,0,0,267,268,3,62,31,0,268,
        269,5,30,0,0,269,271,3,64,32,0,270,272,3,22,11,0,271,270,1,0,0,0,
        271,272,1,0,0,0,272,273,1,0,0,0,273,274,5,33,0,0,274,51,1,0,0,0,
        275,276,5,51,0,0,276,277,5,36,0,0,277,278,5,50,0,0,278,279,5,37,
        0,0,279,281,5,36,0,0,280,282,5,50,0,0,281,280,1,0,0,0,281,282,1,
        0,0,0,282,283,1,0,0,0,283,284,5,37,0,0,284,294,5,36,0,0,285,286,
        3,56,28,0,286,287,5,31,0,0,287,289,1,0,0,0,288,285,1,0,0,0,289,292,
        1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,293,1,0,0,0,292,290,
        1,0,0,0,293,295,3,56,28,0,294,290,1,0,0,0,294,295,1,0,0,0,295,296,
        1,0,0,0,296,297,5,37,0,0,297,307,5,36,0,0,298,299,3,58,29,0,299,
        300,5,31,0,0,300,302,1,0,0,0,301,298,1,0,0,0,302,305,1,0,0,0,303,
        301,1,0,0,0,303,304,1,0,0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,
        308,3,58,29,0,307,303,1,0,0,0,307,308,1,0,0,0,308,309,1,0,0,0,309,
        310,5,37,0,0,310,312,5,36,0,0,311,313,5,50,0,0,312,311,1,0,0,0,312,
        313,1,0,0,0,313,314,1,0,0,0,314,315,5,37,0,0,315,53,1,0,0,0,316,
        317,5,51,0,0,317,318,5,36,0,0,318,319,5,50,0,0,319,320,5,37,0,0,
        320,322,5,36,0,0,321,323,5,50,0,0,322,321,1,0,0,0,322,323,1,0,0,
        0,323,324,1,0,0,0,324,325,5,37,0,0,325,334,5,36,0,0,326,331,3,56,
        28,0,327,328,5,31,0,0,328,330,3,56,28,0,329,327,1,0,0,0,330,333,
        1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,335,1,0,0,0,333,331,
        1,0,0,0,334,326,1,0,0,0,334,335,1,0,0,0,335,336,1,0,0,0,336,337,
        5,37,0,0,337,346,5,36,0,0,338,343,3,58,29,0,339,340,5,31,0,0,340,
        342,3,58,29,0,341,339,1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,
        344,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,346,338,1,0,0,0,346,
        347,1,0,0,0,347,348,1,0,0,0,348,349,5,37,0,0,349,55,1,0,0,0,350,
        351,5,50,0,0,351,352,5,40,0,0,352,353,5,50,0,0,353,57,1,0,0,0,354,
        355,5,50,0,0,355,356,5,30,0,0,356,357,5,50,0,0,357,59,1,0,0,0,358,
        361,5,50,0,0,359,361,3,52,26,0,360,358,1,0,0,0,360,359,1,0,0,0,361,
        61,1,0,0,0,362,365,5,50,0,0,363,365,3,54,27,0,364,362,1,0,0,0,364,
        363,1,0,0,0,365,63,1,0,0,0,366,367,7,1,0,0,367,65,1,0,0,0,41,68,
        71,76,79,84,89,99,110,119,126,133,140,144,151,160,176,184,192,200,
        208,215,218,224,227,234,239,255,271,281,290,294,303,307,312,322,
        331,334,343,346,360,364
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
                     "<INVALID>", "<INVALID>", "'.'", "','", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'*'", "';'", "'->'", "':'" ]

    symbolicNames = [ "<INVALID>", "WITH", "FOR_EACH", "PREDICT", "WHERE", 
                      "ASSUMING", "AS", "CLASSIFY", "RANK_TOP", "AGGR_FUNC", 
                      "AVG", "COUNT", "COUNT_DISTINCT", "FIRST", "LAST", 
                      "LIST_DISTINCT", "MAX", "MIN", "SUM", "NUM_COMP_OP", 
                      "STR_COMP_OP", "NOT_LIKE", "NOT_CONTAINS", "ENDS_WITH", 
                      "STARTS_WITH", "LIKE", "CONTAINS", "NULL_CHECK_OP", 
                      "IS_NOT_NULL", "IS_NULL", "DOT", "COMMA", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", 
                      "CLOSE_BRACE", "STAR", "SEMICOLON", "ARROW", "COLON", 
                      "AND", "OR", "NOT", "DATETIME", "FLOAT", "INT", "TIME_MEASURE_UNIT", 
                      "STRING", "ID", "SQL_INJECTION_BODY", "WS_SKIP", "ANY" ]

    RULE_query = 0
    RULE_query_tmp = 1
    RULE_query_stat = 2
    RULE_common_path_exprs = 3
    RULE_common_path_expr = 4
    RULE_path_node = 5
    RULE_for_each_tmp = 6
    RULE_for_each_stat = 7
    RULE_predict_tmp = 8
    RULE_predict_stat = 9
    RULE_where_tmp = 10
    RULE_where_stat = 11
    RULE_assuming = 12
    RULE_expr_or_tmp = 13
    RULE_expr_or_stat = 14
    RULE_expr_and_tmp = 15
    RULE_expr_and_stat = 16
    RULE_expr_term_tmp = 17
    RULE_expr_term_stat = 18
    RULE_condition_tmp = 19
    RULE_condition_stat = 20
    RULE_num_condition = 21
    RULE_str_condition = 22
    RULE_null_check_condition = 23
    RULE_aggregation_tmp = 24
    RULE_aggregation_stat = 25
    RULE_sql_injection_tmp = 26
    RULE_sql_injection_stat = 27
    RULE_fkey_col_to_pkey_table = 28
    RULE_fkey_table_to_fkey_col = 29
    RULE_table_tmp = 30
    RULE_table_stat = 31
    RULE_column = 32

    ruleNames =  [ "query", "query_tmp", "query_stat", "common_path_exprs", 
                   "common_path_expr", "path_node", "for_each_tmp", "for_each_stat", 
                   "predict_tmp", "predict_stat", "where_tmp", "where_stat", 
                   "assuming", "expr_or_tmp", "expr_or_stat", "expr_and_tmp", 
                   "expr_and_stat", "expr_term_tmp", "expr_term_stat", "condition_tmp", 
                   "condition_stat", "num_condition", "str_condition", "null_check_condition", 
                   "aggregation_tmp", "aggregation_stat", "sql_injection_tmp", 
                   "sql_injection_stat", "fkey_col_to_pkey_table", "fkey_table_to_fkey_col", 
                   "table_tmp", "table_stat", "column" ]

    EOF = Token.EOF
    WITH=1
    FOR_EACH=2
    PREDICT=3
    WHERE=4
    ASSUMING=5
    AS=6
    CLASSIFY=7
    RANK_TOP=8
    AGGR_FUNC=9
    AVG=10
    COUNT=11
    COUNT_DISTINCT=12
    FIRST=13
    LAST=14
    LIST_DISTINCT=15
    MAX=16
    MIN=17
    SUM=18
    NUM_COMP_OP=19
    STR_COMP_OP=20
    NOT_LIKE=21
    NOT_CONTAINS=22
    ENDS_WITH=23
    STARTS_WITH=24
    LIKE=25
    CONTAINS=26
    NULL_CHECK_OP=27
    IS_NOT_NULL=28
    IS_NULL=29
    DOT=30
    COMMA=31
    OPEN_PAREN=32
    CLOSE_PAREN=33
    OPEN_BRACKET=34
    CLOSE_BRACKET=35
    OPEN_BRACE=36
    CLOSE_BRACE=37
    STAR=38
    SEMICOLON=39
    ARROW=40
    COLON=41
    AND=42
    OR=43
    NOT=44
    DATETIME=45
    FLOAT=46
    INT=47
    TIME_MEASURE_UNIT=48
    STRING=49
    ID=50
    SQL_INJECTION_BODY=51
    WS_SKIP=52
    ANY=53

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
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.query_tmp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
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

        def common_path_exprs(self):
            return self.getTypedRuleContext(ParserRTGL.Common_path_exprsContext,0)


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
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 70
                self.common_path_exprs()


            self.state = 73
            self.predict_tmp()
            self.state = 74
            self.for_each_tmp()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 75
                self.where_tmp()


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 78
                self.assuming()


            self.state = 81
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

        def common_path_exprs(self):
            return self.getTypedRuleContext(ParserRTGL.Common_path_exprsContext,0)


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
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 83
                self.common_path_exprs()


            self.state = 86
            self.predict_stat()
            self.state = 87
            self.for_each_stat()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 88
                self.where_stat()


            self.state = 91
            self.match(ParserRTGL.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_path_exprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(ParserRTGL.WITH, 0)

        def common_path_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Common_path_exprContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Common_path_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.COMMA)
            else:
                return self.getToken(ParserRTGL.COMMA, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_common_path_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommon_path_exprs" ):
                listener.enterCommon_path_exprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommon_path_exprs" ):
                listener.exitCommon_path_exprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommon_path_exprs" ):
                return visitor.visitCommon_path_exprs(self)
            else:
                return visitor.visitChildren(self)




    def common_path_exprs(self):

        localctx = ParserRTGL.Common_path_exprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_common_path_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ParserRTGL.WITH)
            self.state = 94
            self.common_path_expr()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 95
                self.match(ParserRTGL.COMMA)
                self.state = 96
                self.common_path_expr()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_path_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.path_name = None # Token
            self._path_node = None # Path_nodeContext
            self.steps = list() # of Path_nodeContexts

        def AS(self):
            return self.getToken(ParserRTGL.AS, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserRTGL.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

        def ID(self):
            return self.getToken(ParserRTGL.ID, 0)

        def path_node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Path_nodeContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Path_nodeContext,i)


        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ARROW)
            else:
                return self.getToken(ParserRTGL.ARROW, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_common_path_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommon_path_expr" ):
                listener.enterCommon_path_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommon_path_expr" ):
                listener.exitCommon_path_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommon_path_expr" ):
                return visitor.visitCommon_path_expr(self)
            else:
                return visitor.visitChildren(self)




    def common_path_expr(self):

        localctx = ParserRTGL.Common_path_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_common_path_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            localctx.path_name = self.match(ParserRTGL.ID)
            self.state = 103
            self.match(ParserRTGL.AS)
            self.state = 104
            self.match(ParserRTGL.OPEN_PAREN)
            self.state = 105
            localctx._path_node = self.path_node()
            localctx.steps.append(localctx._path_node)
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.match(ParserRTGL.ARROW)
                self.state = 107
                localctx._path_node = self.path_node()
                localctx.steps.append(localctx._path_node)
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==40):
                    break

            self.state = 112
            self.match(ParserRTGL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Path_nodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.table = None # Token
            self.left_key = None # Token
            self.right_key = None # Token

        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def COLON(self):
            return self.getToken(ParserRTGL.COLON, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_path_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath_node" ):
                listener.enterPath_node(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath_node" ):
                listener.exitPath_node(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath_node" ):
                return visitor.visitPath_node(self)
            else:
                return visitor.visitChildren(self)




    def path_node(self):

        localctx = ParserRTGL.Path_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_path_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            localctx.table = self.match(ParserRTGL.ID)
            self.state = 115
            self.match(ParserRTGL.DOT)
            self.state = 116
            localctx.left_key = self.match(ParserRTGL.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 117
                self.match(ParserRTGL.COLON)
                self.state = 118
                localctx.right_key = self.match(ParserRTGL.ID)


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

        def table_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Table_tmpContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def column(self):
            return self.getTypedRuleContext(ParserRTGL.ColumnContext,0)


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
        self.enterRule(localctx, 12, self.RULE_for_each_tmp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ParserRTGL.FOR_EACH)
            self.state = 122
            self.table_tmp()
            self.state = 123
            self.match(ParserRTGL.DOT)
            self.state = 124
            self.column()
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 125
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

        def table_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Table_statContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def column(self):
            return self.getTypedRuleContext(ParserRTGL.ColumnContext,0)


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
        self.enterRule(localctx, 14, self.RULE_for_each_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ParserRTGL.FOR_EACH)
            self.state = 129
            self.table_stat()
            self.state = 130
            self.match(ParserRTGL.DOT)
            self.state = 131
            self.column()
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 132
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
        self.enterRule(localctx, 16, self.RULE_predict_tmp)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ParserRTGL.PREDICT)
                self.state = 136
                self.aggregation_tmp()
                self.state = 140
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 137
                    self.match(ParserRTGL.RANK_TOP)
                    self.state = 138
                    self.match(ParserRTGL.INT)
                    pass
                elif token in [7]:
                    self.state = 139
                    self.match(ParserRTGL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(ParserRTGL.PREDICT)
                self.state = 143
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


        def table_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Table_statContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def column(self):
            return self.getTypedRuleContext(ParserRTGL.ColumnContext,0)


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
        self.enterRule(localctx, 18, self.RULE_predict_stat)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ParserRTGL.PREDICT)
                self.state = 147
                self.aggregation_stat()
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 148
                    self.match(ParserRTGL.RANK_TOP)
                    self.state = 149
                    self.match(ParserRTGL.INT)
                    pass
                elif token in [7]:
                    self.state = 150
                    self.match(ParserRTGL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(ParserRTGL.PREDICT)
                self.state = 154
                self.expr_or_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.match(ParserRTGL.PREDICT)
                self.state = 156
                self.table_stat()
                self.state = 157
                self.match(ParserRTGL.DOT)
                self.state = 158
                self.column()
                pass


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
        self.enterRule(localctx, 20, self.RULE_where_tmp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ParserRTGL.WHERE)
            self.state = 163
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
        self.enterRule(localctx, 22, self.RULE_where_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ParserRTGL.WHERE)
            self.state = 166
            self.expr_or_stat()
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
        self.enterRule(localctx, 24, self.RULE_assuming)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ParserRTGL.ASSUMING)
            self.state = 169
            self.expr_or_tmp()
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
        self.enterRule(localctx, 26, self.RULE_expr_or_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expr_and_tmp()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 172
                self.match(ParserRTGL.OR)
                self.state = 173
                self.expr_and_tmp()
                self.state = 178
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
        self.enterRule(localctx, 28, self.RULE_expr_or_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.expr_and_stat()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 180
                self.match(ParserRTGL.OR)
                self.state = 181
                self.expr_and_stat()
                self.state = 186
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
        self.enterRule(localctx, 30, self.RULE_expr_and_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expr_term_tmp()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 188
                self.match(ParserRTGL.AND)
                self.state = 189
                self.expr_term_tmp()
                self.state = 194
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
        self.enterRule(localctx, 32, self.RULE_expr_and_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expr_term_stat()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 196
                self.match(ParserRTGL.AND)
                self.state = 197
                self.expr_term_stat()
                self.state = 202
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
        self.enterRule(localctx, 34, self.RULE_expr_term_tmp)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.condition_tmp()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(ParserRTGL.OPEN_PAREN)
                self.state = 205
                self.expr_or_tmp()
                self.state = 206
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
        self.enterRule(localctx, 36, self.RULE_expr_term_stat)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 44, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.condition_stat()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(ParserRTGL.OPEN_PAREN)
                self.state = 212
                self.expr_or_stat()
                self.state = 213
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
        self.enterRule(localctx, 38, self.RULE_condition_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 217
                self.match(ParserRTGL.NOT)


            self.state = 220
            self.aggregation_tmp()
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 221
                self.num_condition()
                pass
            elif token in [20]:
                self.state = 222
                self.str_condition()
                pass
            elif token in [27]:
                self.state = 223
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


        def table_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Table_statContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def column(self):
            return self.getTypedRuleContext(ParserRTGL.ColumnContext,0)


        def num_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(ParserRTGL.Null_check_conditionContext,0)


        def NOT(self):
            return self.getToken(ParserRTGL.NOT, 0)

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
        self.enterRule(localctx, 40, self.RULE_condition_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 226
                self.match(ParserRTGL.NOT)


            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 229
                self.aggregation_stat()
                pass
            elif token in [50, 51]:
                self.state = 230
                self.table_stat()
                self.state = 231
                self.match(ParserRTGL.DOT)
                self.state = 232
                self.column()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 236
                self.num_condition()
                pass
            elif token in [20]:
                self.state = 237
                self.str_condition()
                pass
            elif token in [27]:
                self.state = 238
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
        self.enterRule(localctx, 42, self.RULE_num_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ParserRTGL.NUM_COMP_OP)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_str_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ParserRTGL.STR_COMP_OP)
            self.state = 245
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
        self.enterRule(localctx, 46, self.RULE_null_check_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
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
            self.start = None # Token
            self.end = None # Token

        def AGGR_FUNC(self):
            return self.getToken(ParserRTGL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserRTGL.OPEN_PAREN, 0)

        def table_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Table_tmpContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def column(self):
            return self.getTypedRuleContext(ParserRTGL.ColumnContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.COMMA)
            else:
                return self.getToken(ParserRTGL.COMMA, i)

        def TIME_MEASURE_UNIT(self):
            return self.getToken(ParserRTGL.TIME_MEASURE_UNIT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.INT)
            else:
                return self.getToken(ParserRTGL.INT, i)

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
        self.enterRule(localctx, 48, self.RULE_aggregation_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ParserRTGL.AGGR_FUNC)
            self.state = 250
            self.match(ParserRTGL.OPEN_PAREN)
            self.state = 251
            self.table_tmp()
            self.state = 252
            self.match(ParserRTGL.DOT)
            self.state = 253
            self.column()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 254
                self.where_stat()


            self.state = 257
            self.match(ParserRTGL.COMMA)
            self.state = 258
            localctx.start = self.match(ParserRTGL.INT)
            self.state = 259
            self.match(ParserRTGL.COMMA)
            self.state = 260
            localctx.end = self.match(ParserRTGL.INT)
            self.state = 261
            self.match(ParserRTGL.COMMA)
            self.state = 262
            self.match(ParserRTGL.TIME_MEASURE_UNIT)
            self.state = 263
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

        def table_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Table_statContext,0)


        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def column(self):
            return self.getTypedRuleContext(ParserRTGL.ColumnContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ParserRTGL.CLOSE_PAREN, 0)

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
        self.enterRule(localctx, 50, self.RULE_aggregation_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ParserRTGL.AGGR_FUNC)
            self.state = 266
            self.match(ParserRTGL.OPEN_PAREN)
            self.state = 267
            self.table_stat()
            self.state = 268
            self.match(ParserRTGL.DOT)
            self.state = 269
            self.column()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 270
                self.where_stat()


            self.state = 273
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
            self.table = None # Token
            self.pkey_col = None # Token
            self.time_col = None # Token

        def SQL_INJECTION_BODY(self):
            return self.getToken(ParserRTGL.SQL_INJECTION_BODY, 0)

        def OPEN_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.OPEN_BRACE)
            else:
                return self.getToken(ParserRTGL.OPEN_BRACE, i)

        def CLOSE_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.CLOSE_BRACE)
            else:
                return self.getToken(ParserRTGL.CLOSE_BRACE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def fkey_col_to_pkey_table(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fkey_col_to_pkey_tableContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fkey_col_to_pkey_tableContext,i)


        def fkey_table_to_fkey_col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fkey_table_to_fkey_colContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fkey_table_to_fkey_colContext,i)


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
        self.enterRule(localctx, 52, self.RULE_sql_injection_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ParserRTGL.SQL_INJECTION_BODY)
            self.state = 276
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 277
            localctx.table = self.match(ParserRTGL.ID)
            self.state = 278
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 279
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 280
                localctx.pkey_col = self.match(ParserRTGL.ID)


            self.state = 283
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 284
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 285
                        self.fkey_col_to_pkey_table()
                        self.state = 286
                        self.match(ParserRTGL.COMMA) 
                    self.state = 292
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                self.state = 293
                self.fkey_col_to_pkey_table()


            self.state = 296
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 297
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 298
                        self.fkey_table_to_fkey_col()
                        self.state = 299
                        self.match(ParserRTGL.COMMA) 
                    self.state = 305
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                self.state = 306
                self.fkey_table_to_fkey_col()


            self.state = 309
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 310
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 311
                localctx.time_col = self.match(ParserRTGL.ID)


            self.state = 314
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
            self.table = None # Token
            self.pkey_col = None # Token

        def SQL_INJECTION_BODY(self):
            return self.getToken(ParserRTGL.SQL_INJECTION_BODY, 0)

        def OPEN_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.OPEN_BRACE)
            else:
                return self.getToken(ParserRTGL.OPEN_BRACE, i)

        def CLOSE_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.CLOSE_BRACE)
            else:
                return self.getToken(ParserRTGL.CLOSE_BRACE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def fkey_col_to_pkey_table(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fkey_col_to_pkey_tableContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fkey_col_to_pkey_tableContext,i)


        def fkey_table_to_fkey_col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserRTGL.Fkey_table_to_fkey_colContext)
            else:
                return self.getTypedRuleContext(ParserRTGL.Fkey_table_to_fkey_colContext,i)


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
        self.enterRule(localctx, 54, self.RULE_sql_injection_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ParserRTGL.SQL_INJECTION_BODY)
            self.state = 317
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 318
            localctx.table = self.match(ParserRTGL.ID)
            self.state = 319
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 320
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 321
                localctx.pkey_col = self.match(ParserRTGL.ID)


            self.state = 324
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 325
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 326
                self.fkey_col_to_pkey_table()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 327
                    self.match(ParserRTGL.COMMA)
                    self.state = 328
                    self.fkey_col_to_pkey_table()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 336
            self.match(ParserRTGL.CLOSE_BRACE)
            self.state = 337
            self.match(ParserRTGL.OPEN_BRACE)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 338
                self.fkey_table_to_fkey_col()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 339
                    self.match(ParserRTGL.COMMA)
                    self.state = 340
                    self.fkey_table_to_fkey_col()
                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 348
            self.match(ParserRTGL.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fkey_col_to_pkey_tableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fkey_col = None # Token
            self.pkey_table = None # Token

        def ARROW(self):
            return self.getToken(ParserRTGL.ARROW, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_fkey_col_to_pkey_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFkey_col_to_pkey_table" ):
                listener.enterFkey_col_to_pkey_table(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFkey_col_to_pkey_table" ):
                listener.exitFkey_col_to_pkey_table(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFkey_col_to_pkey_table" ):
                return visitor.visitFkey_col_to_pkey_table(self)
            else:
                return visitor.visitChildren(self)




    def fkey_col_to_pkey_table(self):

        localctx = ParserRTGL.Fkey_col_to_pkey_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_fkey_col_to_pkey_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            localctx.fkey_col = self.match(ParserRTGL.ID)
            self.state = 351
            self.match(ParserRTGL.ARROW)
            self.state = 352
            localctx.pkey_table = self.match(ParserRTGL.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fkey_table_to_fkey_colContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fkey_table = None # Token
            self.fkey_col = None # Token

        def DOT(self):
            return self.getToken(ParserRTGL.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserRTGL.ID)
            else:
                return self.getToken(ParserRTGL.ID, i)

        def getRuleIndex(self):
            return ParserRTGL.RULE_fkey_table_to_fkey_col

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFkey_table_to_fkey_col" ):
                listener.enterFkey_table_to_fkey_col(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFkey_table_to_fkey_col" ):
                listener.exitFkey_table_to_fkey_col(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFkey_table_to_fkey_col" ):
                return visitor.visitFkey_table_to_fkey_col(self)
            else:
                return visitor.visitChildren(self)




    def fkey_table_to_fkey_col(self):

        localctx = ParserRTGL.Fkey_table_to_fkey_colContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_fkey_table_to_fkey_col)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            localctx.fkey_table = self.match(ParserRTGL.ID)
            self.state = 355
            self.match(ParserRTGL.DOT)
            self.state = 356
            localctx.fkey_col = self.match(ParserRTGL.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ParserRTGL.ID, 0)

        def sql_injection_tmp(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_tmpContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_table_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_tmp" ):
                listener.enterTable_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_tmp" ):
                listener.exitTable_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_tmp" ):
                return visitor.visitTable_tmp(self)
            else:
                return visitor.visitChildren(self)




    def table_tmp(self):

        localctx = ParserRTGL.Table_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_table_tmp)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(ParserRTGL.ID)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.sql_injection_tmp()
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


    class Table_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ParserRTGL.ID, 0)

        def sql_injection_stat(self):
            return self.getTypedRuleContext(ParserRTGL.Sql_injection_statContext,0)


        def getRuleIndex(self):
            return ParserRTGL.RULE_table_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_stat" ):
                listener.enterTable_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_stat" ):
                listener.exitTable_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_stat" ):
                return visitor.visitTable_stat(self)
            else:
                return visitor.visitChildren(self)




    def table_stat(self):

        localctx = ParserRTGL.Table_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_table_stat)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(ParserRTGL.ID)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.sql_injection_stat()
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


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ParserRTGL.ID, 0)

        def STAR(self):
            return self.getToken(ParserRTGL.STAR, 0)

        def getRuleIndex(self):
            return ParserRTGL.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = ParserRTGL.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            _la = self._input.LA(1)
            if not(_la==38 or _la==50):
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





