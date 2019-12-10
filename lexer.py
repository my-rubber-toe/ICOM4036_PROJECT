import ply.yacc as yacc


tokens = (
    "INT",
    "STRING",
    "QUOTE",
    "EQUALS",
    "KEYWORD"
)
t_ignore = " \t"

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    # Check Port --> Min Port: 1024, Max Port: 65535, Port: 0 Kernel will auto assign port
    return t
def t_KEYWORD(t):
    r"create|server|client|send|connect|to|all|receive|delete|external|info|from"
    return t
def t_EQUALS(t):
    r"="
    return t
def t_QUOTE(t):
    r"\""
    return t
def t_STRING(t):
    r"[a-zA-Z_.-][a-zA-Z0-9_.-]*"
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

def p_statement_create_or_delete_client_server(p):
    'statement : KEYWORD KEYWORD STRING'
    if p[1] == "delete":
        if p[2] == "client":
            print("Deleting the client '%s'..." % p[3])
        elif p[2] == "server":
            print("Deleting the server '%s'..." % p[3])
        else:
            print("Error in delete client")
    elif p[1] == "create":
        if p[2] == "client":
            print("Creating a new client '%s'..." % p[3])
    else:
        print("Error in ")

def p_statement_create_server(p):
    'statement : KEYWORD KEYWORD STRING QUOTE STRING QUOTE INT'
    if p[2] == "server":
        print("Creating a new server '%s'..." % p[3])
    elif p[2] == "client":
        print("Creating a new client '%s'..." % p[3])
    else:
        print("Not a function.")

def p_statement_info(p):
    'statement : KEYWORD STRING'
    if p[1] == "info":
        print("Getting %s's information..." % p[2])
    else:
        print("Not a function.")

def p_statement_variable_int(p):
    'statement : STRING EQUALS INT'
    variables[p[1]] = p[3]
    print("Stored...", variables)

def p_statement_variable_string(p):
    'statement : STRING EQUALS QUOTE STRING QUOTE'
    variables[p[1]] = p[4]
    print("Stored...", variables)

def p_statement_local_conn(p):
    'statement : STRING KEYWORD STRING'
    if p[2] == "connect":
        print("Connecting %s to %s..." % (p[1], p[3]))
    else:
        print("Error in local connection...")

def p_statement_external_conn_no_port(p):
    'statement : STRING KEYWORD QUOTE STRING QUOTE'
    if p[2] == "connect":
        print("Connecting %s to %s:80..." % (p[1], p[4]))
    else:
        print("Error in external connection...")

def p_statement_external_conn(p):
    'statement : STRING KEYWORD QUOTE STRING QUOTE KEYWORD INT'
    if p[2] == "connect":
        print("Connecting %s to %s:%d..." % (p[1], p[4],p[6]))
    else:
        print("Error in external connection...")

def p_statement_expr(p):
    'statement : expression'
    print(p[1])
    print("in expr")

def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]
    print("in int")

def p_expression_keyword(p):
    'expression : KEYWORD'
    p[0] = p[1]
    print("in keyword")

def p_expression_string(p):
    'expression : STRING'
    try:
        p[0] = variables[p[1]]
        print("in string")
    except LookupError:
        print("Undefined string '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p is not None:
        print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

while True:
    try:
        s = input('parser > ')   # use input() on Python 3
    except EOFError:
        break
    lexer.input(s)
    parser.parse(s)