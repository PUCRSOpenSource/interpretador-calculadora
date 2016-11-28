#!/usr/bin/env python3

from bc import BcParser as parser

stringsTMP = list()

while True:
    try:
        calc_input = input('> ')
    except EOFError:
        break
    print(calc_input)
    if calc_input == '^[[A':
    	a = stringsTMP.pop()
    	print('using command history: ', a)
    	# parser.parse(a)
    	continue
    stringsTMP.append(calc_input)
    parser.parse(calc_input)

