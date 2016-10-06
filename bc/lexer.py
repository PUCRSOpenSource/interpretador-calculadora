from ply import lex

tokens = (
        'PLUS'  ,
        'MINUS' ,
        'TIMES' ,
        'DIVIDE',
        'POWER' ,
        )

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_POWER  = r'\^'

def t_error(token):
    # token.lexer.skip(1)

    return ('ILLEGAL CHAR', token.value, token.lineno, token.lexpos)

lexer = lex.lex()
