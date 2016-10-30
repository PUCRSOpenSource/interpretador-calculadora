from ply import lex as lex

class BcLexer():
    def __init__(self):
        self.literals = [':', '?', ';']
        self.t_ignore  = ' \t\r'

    reserved = {
            'help'     : 'HELP',
            'load'     : 'LOAD',
            'save'     : 'SAVE',
            'show'     : 'SHOW',
            'show_all' : 'SHOW_ALL',
            'if'       : 'IF',
            'else'     : 'ELSE',
            'while'    : 'WHILE',
            'for'      : 'FOR',
            'define'   : 'DEFINE'
            }
    tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',
            'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
            'OR', 'AND', 'NOT',
            'EQUALS', 'TIMESEQUAL', 'PLUSEQUAL',
            'LPAREN', 'RPAREN',
            'LBRACKET', 'RBRACKET',
            'LBRACE', 'RBRACE', 'COMMA',
            'ID', 'NUMBER'] + list(reserved.values())

    # Atritiméticos
    t_PLUS              = r'\+'
    t_MINUS             = r'-'
    t_TIMES             = r'\*'
    t_DIVIDE            = r'/'
    t_POW               = r'\^'

    # Relacionais
    t_LT                = r'<'
    t_GT                = r'>'
    t_LE                = r'<='
    t_GE                = r'>='
    t_EQ                = r'=='
    t_NE                = r'!='

    # Lógicos
    t_OR               = r'\|\|'
    t_AND              = r'&&'
    t_NOT              = r'!'

    # Atribuição
    t_EQUALS            = r'='
    t_TIMESEQUAL        = r'\*='
    t_PLUSEQUAL         = r'\+='

    # Delimitadores
    t_LPAREN            = r'\('
    t_RPAREN            = r'\)'
    t_LBRACKET          = r'\['
    t_RBRACKET          = r'\]'
    t_LBRACE            = r'\{'
    t_RBRACE            = r'\}'
    t_COMMA             = r','


    def t_newline(self, token):
        r'\n+'
        token.lexer.lineno += 1

    def t_id(self, token):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        token.type = self.reserved.get(token.value, 'ID')
        return token

    def t_NUMBER(self, token):
        r'\d+'
        try:
            token.value = int(token.value)
        except ValueError: 
            print('Integer value too large %d', token.value)
            token.value = 0 
        return token

    def t_error(self, token):
        token.lexer.skip(1)
        return ('ILLEGAL', token.value, token.lineno, token.lexpos)

    def find_column(self, input, token):
        last_cr = input.rfind('\n',0,token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = (token.lexpos - last_cr) + 1
        return column

    def parse(self, data):
        self.lexer.input(data)
        while True:
            token = self.lexer.token()
            if not token:
                break
            print(token)

    def build(self):
        self.lexer = lex.lex(module=self)
