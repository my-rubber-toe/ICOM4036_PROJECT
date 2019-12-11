import ply.yacc as yacc
import ply.lex as lex
from dao.env_controller import EnvController
import re

tokens = [
    "DATA",
    "INT",
    "STRING",
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
t_ignore = " \t\n"

def t_DATA(t):
    r"\".*\""
    return t
def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    # Check Port --> Min Port: 1024, Max Port: 65535, Port: 0 Kernel will auto assign port
    return t
def t_EQUALS(t):
    r"="
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
                 | DELETE STRING
    """
    if p[1] == "delete":
        environment.delete_client_or_server(p[2])
    elif p[1] == "create":
        if p[2] == "client":
            client_name = p[3]
            # Run create client here: OK
            environment.create_client(client_name)
    else:
        print("ERROR in create/delete server or client...")

def p_statement_create_server(p):
    """statement : CREATE SERVER STRING DATA INT
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
        environment.create_server(server_name, p[4].replace('"', ''), p[5])

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

def p_statement_variable_string(p):
    'statement : STRING EQUALS DATA'
    # Run var var assignment here: OK
    environment.var_assign(p[1], p[3].replace('"', ''))

def p_statement_variable_int(p):
    'statement : STRING EQUALS INT'
    # Run var int assignment here: OK
    environment.var_assign(p[1], p[3])

def p_statement_send_data(p):
    """statement : STRING SEND STRING DATA
                 | STRING SEND STRING STRING
    """
    if p[2] == "send":
        length = len(p)
        environment.send_message(p[1], p[3], p[4].replace('"', ''))
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
    'statement : STRING CONNECT DATA'
    if p[2] == "connect" and re.match("https?:\/\/(www\.)?", p[3].replace('"', '')):
        sender = p[1]
        address = p[3]
        environment.connect_external(sender, address)
    else:
        print("ERROR in external connection... did you missed \"http://\" or \"https://\" ?")

# def p_statement_expr(p):
#     'statement : expression'

# def p_expression_string(p):
#     """expression : STRING expression
#                   | STRING
#     """

# def p_expression_int(p):
#     'expression : INT'
#     p[0] = p[1]
#     print(p[0])


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

read_file = input('Read from file? (y/N): ')

if(read_file == 'y' or read_file == 'yes'):
    file_name = input('File name: ')
    file = open(file_name, 'r')
    line = file.readline()
    while(line):
        # lexer.input(line)
        parser.parse(line, lexer=lexer)
        line = file.readline()
    

else:
    while True:
        try:
            s = input('simply_connected >> ')   # use input() on Python 3
        except EOFError:
            break
        lexer.input(s)
        # for tok in iter(lexer.token, None):
        #     # print(repr(tok.type), repr(tok.value))
        #     print(tok.type, tok.value)
        parser.parse(s)