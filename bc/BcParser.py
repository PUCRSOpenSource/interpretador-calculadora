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

    def p_expr_statement_assgin(self, token):
        """
            statement : ID EQUALS expr
        """
        self.names[token[1]] = token[3]

    def p_expr_statement(self, token):
        """
            statement : expr
        """
        print(token[1])

    def p_expr_number(self, token):
        """expr : NUMBER"""
        token[0] = token[1]

    def P_if_expr(self, token):
        """
            if      : IF LPAREN expr RPAREN statement
        """
        

    def p_expr_bin(self, token):
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
                    | expr NOT expr
        """
        if token[2] == '+':
            token[0] = token[1] + token[3]
        elif token[2] == '-':
            token[0] = token[1] - token[3]
        elif token[2] == '*':
            token[0] = token[1] * token[3]
        elif token[2] == '/':
            token[0] = token[1] / token[3]
        elif token[2] == 'ˆ':
            token[0] = token[1]**token[3]
        elif token[2] == '<':
             token[0] = token[1] < token[3]
        elif token[2] == '<=':
            token[0] = token[1] <= token[3]
        elif token[2] == '>=':
            token[0] = token[1] >= token[3]
        elif token[2] == '>':
            token[0] = token[1] > token[3]
        elif token[2] == '&&':
            token[0] = token[1] > token[3]
        elif token[2] == '||':
            token[0] = token[1] or token[3]
        elif token[2] == '!=':
            token[0] = token[1] != token[3]
        elif p[2] == '!.':
            token[0] = token[1] !. token[3]   

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
