from ply import yacc as yacc
from BcLexer import BcLexer

class BcParser():
    def __init__(self, 
                 lexer=BcLexer):
        self.bcLexer = BcLexer()
        self.bclex = lexer()
        self.bclex.build()
        self.tokens = self.bcLexer.tokens
        self.names = {}
        self.precence = (
                ('left', 'PLUS', 'MINUS'),
                ('left', 'TIMES', 'DIVIDE'),
                ('right', 'UMINUS')
                )

    def p_statement_assgin(self, token):
        """statement: ID EQUALS expression"""
        names[token[1]] = token[3]

        
    def p_expr(self, token):
        """
        expr       : expr PLUS expr
                   | expr MINUS expr
                   | expr TIMES expr
                   | expr DIVIDE expr
                   | expr POW expr
                   | ID
                   | NUMBER
        """
        print(token)
        if token[2] == '+':
            print('+')
        # elif p[2] == '-':
            # print('-')
        # elif p[2] == '*':
            # print('*')
        # elif p[2] == '/':
            # print ('/') 
        # elif p[2] == 'ˆ':
            # print ('ˆ')
        # elif p[2] == '<':
            # print ('<')
        # elif p[2] == '<=':
            # print ('<=')
        # elif p[2] == '>=':
            # print ('>=')   
        # elif p[2] == '>':
            # print ('>')
        # elif p[2] == '&&':
            # print ('&&')
        # elif p[2] == '||':
            # print ('||')
        # elif p[2] == '!=':
            # print ('!=')
        # elif p[2] == '!.':
            # print ('!.')   

    def parse(self, data):
        """docstring for parse"""
        self.parser.parse(data)

    def build(self):
        self.parser = yacc.yacc(module=self)

bc = BcParser()
bc.build()
while True:
    try:
        calc_input = input('> ')
    except EOFError:
        break
    bc.parse(calc_input)
