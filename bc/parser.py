import ply.yacc as yacc
from lexer import BcLexer

class BcParser():
    def __init__(self):
        pass

    def p_expr():
        if p[2] == '+':
            print('+')
        elif p[2] == '-':
            print('-')
        elif p[2] == '*':
            print('*')
        elif p[2] == '/':
            print ('/') 
        elif p[2] == 'ˆ':
            print ('ˆ')            
        elif p[2] == '<':
            print ('<')            
        elif p[2] == '<=':
            print ('<=')
        elif p[2] == '>=':
            print ('>=')   
        elif p[2] == '>':
            print ('>')    
     

    def build(self):
        self.parser = yacc.yacc(module=self)

