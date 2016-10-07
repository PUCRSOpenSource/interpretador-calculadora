import lexer as lexer
while True: 	
	try:
		calc_input = input('>')
	except EOFError:
		break
	lexer.lexer.input(calc_input)
	[token for token in lexer.lexer]

