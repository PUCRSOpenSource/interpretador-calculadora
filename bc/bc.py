from BcParser import BcParser as parser

parser = parser().parser

while True:
    try:
        calc_input = input('> ')
    except EOFError:
        break
    parser.parse(calc_input)

