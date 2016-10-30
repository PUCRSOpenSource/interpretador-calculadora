from BcLexer import BcLexer as lexer

lex = lexer()
lex.build()
while True:
    try:
        calc_input = input('> ')
    except EOFError:
        break
    lex.parse(calc_input)

