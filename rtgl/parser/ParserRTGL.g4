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
    : predict_tmp for_each_tmp (where_tmp)? (assuming)? SEMICOLON
    ;

query_stat
    : predict_stat for_each_stat (where_stat)? SEMICOLON
    ;

// ============================================================================
// QUERY CLAUSES
// ============================================================================

// FOR_EACH clause: specifies the table/sql injection and column to iterate over
for_each_tmp
    : FOR_EACH (ID | sql_injection_tmp) DOT (ID | STAR) (where_stat)?
    ;

for_each_stat
    : FOR_EACH (ID | sql_injection_stat) DOT (ID | STAR) (where_stat)?
    ;

// PREDICT clause: specifies what to predict (aggregation, expression, or table/sql injection with column)
predict_tmp
    : PREDICT aggregation_tmp (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or_tmp  
    ;

predict_stat
    : PREDICT aggregation_stat (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or_stat  
    | PREDICT (ID | sql_injection_stat) DOT (ID | STAR)
    ;

// ASSUMING clause: specifies conditions that should be assumed to hold
assuming    
    : ASSUMING expr_or_tmp
    ;

// WHERE clause: filters results based on conditions
where_tmp
    : WHERE expr_or_tmp 
    ;

where_stat
    : WHERE expr_or_stat 
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

// A condition consists of a subject (aggregation or table/sql ibjection with column reference) and a comparison
condition_tmp
    : (NOT)? aggregation_tmp (num_condition | str_condition | null_check_condition)
    ;

condition_stat
    : (NOT)? (aggregation_stat | (ID | sql_injection_stat) DOT (ID | STAR))  
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

// Aggregation: specifies an aggregation function applied to a table/sql injection column, optionally with a  static WHERE clause and time inteval for temporal queries
aggregation_tmp
    : AGGR_FUNC OPEN_PAREN (ID | sql_injection_tmp) DOT (ID | STAR) (where_stat)? COMMA INT COMMA INT COMMA TIME_MEASURE_UNIT CLOSE_PAREN
    ;

aggregation_stat
    : AGGR_FUNC OPEN_PAREN (ID | sql_injection_stat) DOT (ID | STAR) (where_stat)? CLOSE_PAREN
    ;

// ============================================================================
// SQL INJECTIONS
// ============================================================================

// SQL injection: allows specifying a SQL query with parameters.
sql_injection_tmp
    : SQL_INJECTION_BODY
      OPEN_BRACE ID CLOSE_BRACE // name
      OPEN_BRACE (ID)? CLOSE_BRACE // pkey_col
      OPEN_BRACE ((fk_col_to_pk_table COMMA)* fk_col_to_pk_table)? CLOSE_BRACE  // fkey_col_to_pkey_table list
      OPEN_BRACE ((fk_table_col COMMA)* fk_table_col)? CLOSE_BRACE // fkey_table_col list
      OPEN_BRACE ID CLOSE_BRACE // time_col 
    ;

sql_injection_stat
    : SQL_INJECTION_BODY
      OPEN_BRACE ID CLOSE_BRACE // name
      OPEN_BRACE (ID)? CLOSE_BRACE // pkey_col
      OPEN_BRACE ((fk_col_to_pk_table COMMA)* fk_col_to_pk_table)? CLOSE_BRACE  // fkey_col_to_pkey_table list
      OPEN_BRACE ((fk_table_col COMMA)* fk_table_col)? CLOSE_BRACE // fkey_table_col list
    ;

// Parameters for SQL injection.
fk_col_to_pk_table
    : ID ARROW ID
    ;
    
fk_table_col
    : ID COLON ID
    ;