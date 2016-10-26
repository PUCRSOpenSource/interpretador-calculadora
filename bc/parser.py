import ply.yacc as yacc
from lexer import BcLexer

def p_expr():
    if p[2] == '+':
        print('+')
    elif p[2] == '-':
        print('-')
    elif p[2] == '*':
        print('*')

