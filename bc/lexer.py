from ply import lex

tokens = (
        'HELP',
        'LOAD',
        'SAVE',
        'SHOW',
        'SHOW_ALL'
        )

literals = ['+','-','/','*', '^', '<', '>', '=', '!']

t_HELP     = r'help'
t_LOAD     = r'load'
t_SAVE     = r'save'
t_SHOW     = r'show'
t_SHOW_ALL = r'show_all'

def t_error(token):
    token.lexer.skip(1)
    return ('ILLEGAL CHAR', token.value, token.lineno, token.lexpos)

lexer = lex.lex()
