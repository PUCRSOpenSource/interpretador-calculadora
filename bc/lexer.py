import ply.lex as lex

class BcLexer():
    def __init__(self):
        self.reserved = {
                'help'     : 'HELP',
                'load'     : 'LOAD',
                'save'     : 'SAVE',
                'show'     : 'SHOW',
                'show_all' : 'SHOW_ALL',
                'if'       : 'IF',
                'while'    : 'WHILE',
                'for'      : 'FOR',
                'define'   : 'DEFINE'
                }

        self.tokens = ['ID'] + list(self.reserved.values())
        self.literals = ['+', '-', '/', '*', '^', '<', '>', '=', 
                         '!', '&', '|', ':', '?', '(', ')', '{', 
                         '}', '[', ']', ';', ',']
        
        self.t_ignore  = ' \t\r'

    def t_newline(self, token):
        r'\n+'
        token.lexer.lineno += 1

    def t_id(self, token):
        r'[a-z-A-Z_][a-zA-Z_0-9]*'
        token.type = self.reserved.get(token.value, 'ID')
        return token
    
    def t_number(self, token): 
        r'\d+'
        try: 
            token.value = int(token.value)
        except ValueError: 
            print("Integer value too large %d", token.value) token.value = 0 
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
