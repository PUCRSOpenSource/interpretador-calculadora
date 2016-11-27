import logging
from .ply import yacc as yacc
from . import BcLexer as lexer

lexer.build()
tokens = lexer.tokens
names = {}
precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('nonassoc', 'NOT'),
        ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
        ('right', 'EQUALS', 'TIMESEQUAL', 'PLUSEQUAL'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('left', 'POW'),
        ('right', 'UMINUS'),
        )

def p_expr_statement(token):
    """
        statement : expr
    """

def p_built_in_unary(token):
    """
        statement : SHOW_ALL
                  | HELP
    """

def p_built_in_binary(token):
    """
        statement : SHOW ID
                  | SAVE ID
                  | LOAD ID
                  | PRINT ID
    """

def p_function(token):
    """
        statement  : DEFINE ID LPAREN listParams RPAREN LBRACE liststatements RBRACE
    """

def p_expr_statement_assign(token):
    """
        statement : ID EQUALS expr
                  | ID TIMESEQUAL expr
                  | ID PLUSEQUAL expr
    """
    if token[2] == '=':
        names[token[1]] = token[3]
    elif token[2] == '*=':
        if token[1] not in names:
            names[token[1]] = 0
        actual = names[token[1]]
        names[token[1]] = token[3] * actual
    elif token[2] == '+=':
        if token[1] not in names:
            names[token[1]] = 0
        actual = names[token[1]]
        names[token[1]] = token[3] + actual

def p_if(token):
    """
        statement : IF LPAREN expr RPAREN liststatements statement_else
    """

def p_else(token):
    """statement_else : ELSE liststatements
                      | empty
    """

def p_while_loop(token):
    """
        statement : WHILE LPAREN expr RPAREN liststatements 
    """

def p_for_loop(token):
    """
        statement : FOR LPAREN expr SEMI expr SEMI expr RPAREN LBRACE liststatements RBRACE
    """
    token[0] = ('for', token[3], token[5], token[7], token[10])
    print(token[0])
    print(evaluate(token[0]))

def p_not(token):
    """
        statement : NOT expr
    """

def p_expr_number(token):
    """expr : NUMBER"""
    token[0] = ('num',token[1])

def p_expr_id(token):
    """expr : ID """
    if token[1] in names:
        token[0] = names[token[1]]

def p_expr_bin(token):
    """
        expr    : expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | expr POW expr
                | expr LT expr
                | expr GT expr
                | expr LE expr
                | expr GE expr
                | expr EQ expr
                | expr NE expr
                | expr OR expr
                | expr AND expr
    """
    if token[2] == '+':
        token[0] = ('+', token[1], token[3])
    elif token[2] == '-':
        token[0] = ('-',token[1],token[3])
    elif token[2] == '*':
        token[0] = ('*', token[1] , token[3])
    elif token[2] == '/':
        token[0] = ('/', token[1] , token[3])
    elif token[2] == '^':
        token[0] = ('^', token[1] , token[3])
    elif token[2] == '<':
         token[0] = ('<' , token[1] , token[3])
    elif token[2] == '<=':
        token[0] = ('<=' , token[1] , token[3])
    elif token[2] == '>=':
        token[0] = ('>=' , token[1] , token[3])
    elif token[2] == '>':
        token[0] = ('>' , token[1] , token[3])
    elif token[2] == '&&':
        token[0] = ('&&' , token[1] , token[3])
    elif token[2] == '||':
        token[0] = ('||' , token[1] , token[3])
    elif token[2] == '!=':
        token[0] = ('!=' , token[1] , token[3])
    print(token[0])
    print(evaluate(token[0]))

def p_expression_uminus(token):
    """expr : MINUS expr %prec UMINUS"""
    token[0] = -token[2]

def p_params(token):
    """
        listParams : ID COMMA listParams
                   | ID
                   | empty
    """

def p_statements(token):
    """
        liststatements : statement SEMI liststatements
    """


def p_statments_alone(t):
    '''
        liststatements : statement        
    '''    
    t[0] = t[1]

def p_statments_empty(t):
    '''
        liststatements : empty        
    '''

def p_empty(token):
    """empty :"""
    pass

def evaluate(lst):
    if(lst[0] == 'num'):
        return lst[1]
    elif(lst[0] == '+'):
        return evaluate(lst[1]) + evaluate(lst[2])
    elif(lst[0] == '-'):
        return evaluate(lst[1]) - evaluate(lst[2])
    elif(lst[0] == '*'):
        return evaluate(lst[1]) * evaluate(lst[2])
    elif(lst[0] == '^'):
        return evaluate(lst[1]) ** evaluate(lst[2])
    elif(lst[0] == '/'):
        return evaluate(lst[1]) / evaluate(lst[2])
    elif(lst[0] == '<'):
        return evaluate(lst[1]) < evaluate(lst[2])
    elif(lst[0] == '<='):
        return evaluate(lst[1]) <= evaluate(lst[2])
    elif(lst[0] == '>'):
        return evaluate(lst[1]) > evaluate(lst[2])
    elif(lst[0] == '>='):
        return evaluate(lst[1]) >= evaluate(lst[2])
    elif(lst[0] == '&&'):
        return evaluate(lst[1]) and evaluate(lst[2])
    elif(lst[0] == '||'):
        return evaluate(lst[1]) or evaluate(lst[2])
    elif(lst[0] == '!='):
        return evaluate(lst[1]) != evaluate(lst[2])

    elif(lst[0] == 'for'):
        for i in range(evaluate(lst[1]),evaluate(lst[2]), evaluate(lst[3])):
            evaluate(lst[4])
        return

def parse(data):
    parser.parse(data)

logging.basicConfig(
        level = logging.DEBUG,
        filename = "bc.log",
        filemode = "w",
        format = "%(filename)10s:%(lineno)4d:%(message)s"
        )
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log, errorlog=log)
