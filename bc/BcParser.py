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
            statement   : ID EQUALS expr
                        | ID TIMESEQUAL expr
                        | ID PLUSEQUAL expr
        """
        if token[2] == '=':
            self.names[token[1]] = token[3]
        elif token[2] == '*=':
            if token[1] not in self.names:
                self.names[token[1]] = 0
            actual = self.names[token[1]]
            self.names[token[1]] = token[3] * actual
        elif token[2] == '+=':
            if token[1] not in self.names:
                self.names[token[1]] = 0
            actual = self.names[token[1]]
            self.names[token[1]] = token[3] + actual

    def p_expr_statement(self, token):
        """
            statement : expr
        """
        print(token[1])

    def p_expr_number(self, token):
        """expr : NUMBER"""
        token[0] = token[1]

    def p_expr_id(self, token):
        """expr : ID """
        if token[1] in self.names:
            token[0] = self.names[token[1]]

    def p_if(self, token):
        """
            statement  : IF LPAREN expr RPAREN statement
                       | IF LPAREN expr RPAREN statement ELSE statement
        """

    def p_while_loop(self, token):
        """
            statement  : WHILE LPAREN expr RPAREN statement 
        """

    def p_for_loop(self, token):
        """
            statement   : FOR LPAREN expr SEMI expr SEMI expr RPAREN statement
        """
        
    def p_not(self, token):
        """
            statement   : NOT expr
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
            token[0] = token[1] **token[3]
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

    def parse(self, data):
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
