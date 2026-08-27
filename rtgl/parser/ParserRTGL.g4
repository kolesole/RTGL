/**
 * Parser for RTGL (Relational Task Generation Language)
 * Defines the syntax rules for valid RTGL queries
 */
parser grammar ParserRTGL ;

options { tokenVocab=LexerRTGL; }    // Import tokens from the lexer grammar

// ============================================================================
// MAIN QUERY RULE
// ============================================================================

query
    : query_tmp 
    | query_stat
    ;

query_tmp
    : common_path_exprs? predict_tmp for_each_tmp where_tmp? assuming? SEMICOLON
    ;

query_stat
    : common_path_exprs? predict_stat for_each_stat where_stat? SEMICOLON
    ;

// ============================================================================
// QUERY CLAUSES
// ============================================================================

// Common Path Expressions (CPEs): declares one or more named, explicit multi-hop join paths
common_path_exprs
    : WITH common_path_expr (COMMA common_path_expr)*
    ;

// A single named CPE
common_path_expr
    : path_name=ID AS OPEN_PAREN steps+=path_node (ARROW steps+=path_node)+ CLOSE_PAREN
    ;

// FOR_EACH clause: specifies the table/path/sql injection and column to iterate over
for_each_tmp
    : FOR_EACH table_tmp DOT column (where_stat)?
    ;

for_each_stat
    : FOR_EACH table_stat DOT column (where_stat)?
    ;

// PREDICT clause: specifies what to predict (aggregation, expression, or table/path/sql injection with column)
predict_tmp
    : PREDICT aggregation_tmp (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or_tmp  
    ;

predict_stat
    : PREDICT aggregation_stat (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or_stat  
    | PREDICT table_stat DOT column
    ;

// WHERE clause: filters results based on conditions
where_tmp
    : WHERE expr_or_tmp 
    ;

where_stat
    : WHERE expr_or_stat 
    ;

// ASSUMING clause: specifies conditions that should be assumed to hold
assuming    
    : ASSUMING expr_or_tmp
    ;

// ============================================================================
// BOOLEAN EXPRESSIONS (Operator precedence: OR < AND < condition)
// ============================================================================

// OR expressions: lowest precedence
expr_or_tmp
    : expr_and_tmp (OR expr_and_tmp)*
    ;

expr_or_stat
    : expr_and_stat (OR expr_and_stat)*
    ;

// AND expressions: medium precedence
expr_and_tmp
    : expr_term_tmp (AND expr_term_tmp)*
    ;

expr_and_stat
    : expr_term_stat (AND expr_term_stat)*
    ;

// Terms: highest precedence (conditions or parenthesized expressions)
expr_term_tmp
    : condition_tmp
    | OPEN_PAREN expr_or_tmp CLOSE_PAREN
    ;

expr_term_stat
    : condition_stat
    | OPEN_PAREN expr_or_stat CLOSE_PAREN
    ;

// ============================================================================
// CONDITIONS
// ============================================================================

// A condition consists of a subject (aggregation or table/path/sql injection with column reference) and a comparison
condition_tmp
    : NOT? aggregation_tmp (num_condition | str_condition | null_check_condition)
    ;

condition_stat
    : NOT? (aggregation_stat | table_stat DOT column)  
      (num_condition | str_condition | null_check_condition)
    ;

// Numeric comparison: compares against numbers or timestamps
num_condition
    : NUM_COMP_OP (DATETIME | FLOAT | INT)
    ;

// String comparison: compares against string values
str_condition
    : STR_COMP_OP STRING 
    ;

// NULL check: tests if a value is NULL or NOT NULL
null_check_condition
    : NULL_CHECK_OP
    ;

// ============================================================================
// AGGREGATION FUNCTIONS
// ============================================================================

// Aggregation: specifies an aggregation function applied to a table/path/sql injection column, 
// optionally with a static WHERE clause and time interval for temporal queries
aggregation_tmp
    : AGGR_FUNC OPEN_PAREN table_tmp DOT column where_stat? COMMA 
      start=INT COMMA end=INT COMMA TIME_MEASURE_UNIT CLOSE_PAREN
    ;

aggregation_stat
    : AGGR_FUNC OPEN_PAREN table_stat DOT column where_stat? CLOSE_PAREN
    ;

// ============================================================================
// SQL INJECTIONS
// ============================================================================

// SQL injection: allows specifying a SQL query with parameters
sql_injection_tmp
    : SQL_INJECTION_BODY
      OPEN_BRACE table=ID CLOSE_BRACE // table name
      OPEN_BRACE pkey_col=ID? CLOSE_BRACE // pkey_col
      OPEN_BRACE ((fkey_col_to_pkey_table COMMA)* fkey_col_to_pkey_table)? CLOSE_BRACE  // fkey_col_to_pkey_table list
      OPEN_BRACE ((fkey_table_to_fkey_col COMMA)* fkey_table_to_fkey_col)? CLOSE_BRACE // fkey_table_to_fkey_col list
      OPEN_BRACE time_col=ID? CLOSE_BRACE // time_col 
    ;

sql_injection_stat
    : SQL_INJECTION_BODY
      OPEN_BRACE table=ID CLOSE_BRACE // table name
      OPEN_BRACE pkey_col=ID? CLOSE_BRACE // pkey_col
      OPEN_BRACE (fkey_col_to_pkey_table (COMMA fkey_col_to_pkey_table)*)? CLOSE_BRACE  // fkey_col_to_pkey_table list
      OPEN_BRACE (fkey_table_to_fkey_col (COMMA fkey_table_to_fkey_col)*)? CLOSE_BRACE // fkey_table_to_fkey_col list
    ;

// ============================================================================
// SIMPLE COMPONENTS OF QUERIES
// ============================================================================

// One hop of a path
path_node
    : table=ID DOT left_key=ID (COLON right_key=ID)?
    ;

// Parameters for SQL injection
fkey_col_to_pkey_table
    : fkey_col=ID ARROW pkey_table=ID
    ;

fkey_table_to_fkey_col
    : fkey_table=ID DOT fkey_col=ID
    ;

// Table/Path and column references
table_tmp
    : ID 
    | sql_injection_tmp
    ;

table_stat
    : ID
    | sql_injection_stat
    ;

column
    : ID
    | STAR
    ;
