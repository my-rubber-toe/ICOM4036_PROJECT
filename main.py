import ply.yacc as yacc
import ply.lex as lex
from dao.env_controller import EnvController
import re

tokens = [
    "INT",
    "LINK",
    "STRING",
    "QUOTE",
    "EQUALS"
]
reserved = {
    'create' : 'CREATE',
    'server' : 'SERVER',
    'client' : 'CLIENT',
    'delete' : 'DELETE',
    'connect' : 'CONNECT',
    'send' : 'SEND',
    'info' : 'INFO'
}
tokens += reserved.values()
t_ignore = " \t"

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    # Check Port --> Min Port: 1024, Max Port: 65535, Port: 0 Kernel will auto assign port
    return t
def t_EQUALS(t):
    r"="
    return t
def t_QUOTE(t):
    r"\""
    return t
def t_LINK(t):
    r"(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+"
    return t
def t_STRING(t):
    r"[a-zA-Z_.-][a-zA-Z0-9_.-]*"
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# lex.input("var1 = \"woah\" 33")
# for tok in iter(lex.token, None):
#     # print(repr(tok.type), repr(tok.value))
#     print(tok.type, tok.value)

variables = { }
environment = EnvController()

def p_statement_create_or_delete_client_server(p):
    """statement : CREATE CLIENT STRING
                 | DELETE CLIENT STRING
                 | DELETE SERVER STRING
    """
    if p[1] == "delete":
        if p[2] == "client":
            client_name = p[3]
            # Run delete client here: OK
            environment.delete_client_or_server(client_name)
        elif p[2] == "server":
            server_name = p[3]
            # Run delete server here: OK
            environment.delete_client_or_server(server_name)
        else:
            print("Error in delete client")
    elif p[1] == "create":
        if p[2] == "client":
            client_name = p[3]
            # Run create client here: OK
            environment.create_client(client_name)
    else:
        print("ERROR in create/delete server or client...")

def p_statement_create_server(p):
    """statement : CREATE SERVER STRING QUOTE STRING QUOTE INT
                 | CREATE SERVER STRING STRING INT
                 | CREATE SERVER STRING
    """
    if p[1] == "create" and p[2] == "server":
        server_name = p[3]
        # Run create server here: OK

        length = len(p)
        if(len(p) == 4):
            environment.create_server(server_name, "localhost", 0)
            return

        if(length == 6):
            environment.create_server(server_name, p[4], p[5])
            return

        environment.create_server(server_name, p[5], p[7])

    else:
        print("ERROR in creating server...")

def p_statement_info(p):
    'statement : INFO STRING'
    if p[1] == "info":
        # Run info here: OK
        variable = p[2]
        environment.info(variable)
    else:
        print("ERROR in getting variable info...")

def p_statement_variable_int(p):
    'statement : STRING EQUALS INT'
    # Run var int assignment here: OK
    environment.var_assign(p[1],p[3])

def p_statement_variable_string(p):
    'statement : STRING EQUALS QUOTE STRING QUOTE'

    # Run var int assignment here: OK
    environment.var_assign(p[1], p[4])

def p_statement_send_data(p):
    """statement : STRING SEND STRING QUOTE STRING QUOTE
                 | STRING SEND STRING STRING
    """
    if p[2] == "send":
        length = len(p)
        if(length == 7):
            environment.send_message(p[1], p[3], p[5])
            
        if(length == 5):
            environment.send_message(p[1], p[3], p[4])
    else:
        print("ERROR in send data...")

def p_statement_local_conn(p):
    'statement : STRING CONNECT STRING'
    if p[2] == "connect":
        sender = p[1]
        receiver = p[3]
        message = "PING PING PING..."
        environment.send_message(sender, receiver, message)
    else:
        print("ERROR in local connection...")

# def p_statement_external_conn(p):
#     'statement : STRING KEYWORD QUOTE STRING QUOTE KEYWORD INT'
#     if p[2] == "connect":
#         print("Connecting %s to %s:%d..." % (p[1], p[4],p[7]))
#     else:
#         print("ERROR in external connection...")

def p_statement_external_conn_no_port(p):
    'statement : STRING CONNECT QUOTE LINK QUOTE'
    if p[2] == "connect" and re.match("https?:\/\/(www\.)?", p[4]):
        sender = p[1]
        address = p[4]
        environment.connect_external(sender, address)
    else:
        print("ERROR in external connection... did you missed \"http://\" or \"https://\" ?")

def p_statement_expr(p):
    'statement : expression'

def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]
    print(p[0])

# def p_expression_string(p):
#     'expression : STRING'
#     try:
#         p[0] = variables[p[1]]
#         print("in string")
#     except LookupError:
#         print("Undefined string '%s'" % p[1])
#         p[0] = 0

def p_error(p):
    if p is not None:
        print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

while True:
    try:
        s = input(' simply_connected >> ')   # use input() on Python 3
    except EOFError:
        break
    lexer.input(s)
    parser.parse(s)