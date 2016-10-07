from lexer import BcLexer 

lex = BcLexer()
lex.build()
while True: 	
    try:
        calc_input = input('> ')
    except EOFError:
        break
    lex.parse(calc_input)

