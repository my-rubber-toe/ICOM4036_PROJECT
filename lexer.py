
tokens = (
    "INT",
    "VARNAME",
    "QUOTE",
    "EQUALS",
    "KEYWORD"
)
t_ignore = " \t"

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    # Check Port --> Min Port: 0, Max Port: 99999
    return t
def t_KEYWORD(t):
    r"create|server|client|send|to|all|receive|delete|external|info|from"
    return t
def t_EQUALS(t):
    r"="
    return t
def t_QUOTE(t):
    r"\""
    return t
def t_VARNAME(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# lex.input("var1 = \"woah\" 33")
# for tok in iter(lex.token, None):
#     # print(repr(tok.type), repr(tok.value))
#     print(tok.type, tok.value)

variables = { }

def p_expression_keyword(p):
    'expression : KEYWORD'
    p[0] = p[1]
    print("in keyword")

def p_statement_assign(p):
    'statement : VARNAME EQUALS QUOTE VARNAME QUOTE'
    variables[p[1]] = p[4]
    print("in assign")

def p_statement_expr(p):
    'statement : expression'
    print(p[1])
    print("in expr")

def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]
    print("in int")

def p_expression_varname(p):
    'expression : VARNAME'
    try:
        p[0] = variables[p[1]]
        print("in varname")
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('parser > ')   # use input() on Python 3
    except EOFError:
        break
    lexer.input(s)
    parser.parse(s)