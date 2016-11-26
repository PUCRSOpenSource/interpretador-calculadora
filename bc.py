#!/usr/bin/env python3

from bc import BcParser as parser

while True:
    try:
        calc_input = input('> ')
    except EOFError:
        break
    parser.parse(calc_input)

