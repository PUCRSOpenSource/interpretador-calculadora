import logging
from .ply import yacc as yacc
from . import BcLexer as lexer

lexer.build()
tokens = lexer.tokens
names = {}
funtionStack = list()
precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('nonassoc', 'NOT'),
        ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
        ('right', 'EQUALS', 'TIMESEQUAL', 'PLUSEQUAL'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('left', 'POW'),
        ('right', 'UMINUS'),
        )

def p_expr_statement(token):
    """
        statement : expr
    """

def p_built_in_unary(token):
    """
        statement : SHOW_ALL
    """
    print(names)

def p_built_in_ops(token):
    """
        statement : HELP
    """
    print('#############')
    print('#  Manual   #')
    print('#############')
    print('''Examples
             1+1 Input
             2   Result
             1 / 3 Input
            .33333333333333333333 Result
             4 * (6 + 7) Input
             52 Result''')    

def p_built_in_binary(token):
    """
        statement : SHOW ID
                  | SAVE ID
                  | LOAD ID
    """

def p_built_in_print_id(p):
    '''
        statement : PRINT ID
    '''
    print(names.get( p[2] , None ))

def p_evaluate_id(p):
    '''
        statement : EVALUATE ID
    '''
    print(evaluate(names.get( p[2] , None )))

def p_evaluate_expr(p):
    '''
        statement : EVALUATE expr
    '''
    print(evaluate(p[2]))
    
def p_function(token):
    """
        statement  : DEFINE ID LPAREN listParams RPAREN LBRACE liststatements RBRACE
    """
    tmp = names.get(token[2], None)
    if tmp == None:
        names[token[2]] = ('define', token[2] ,token[7])
    else:
        print("function name already defined")

def p_function_call(p):
    '''
        statment :  ID LPAREN listParams RPAREN
                 | ID LPAREN RPAREN
    '''
    tmp = names.get(p[1], None)
    if tmp != None:
        funtionStack.append(p[3]) if p[3] != None else None
        print('aqui')
        evaluate(tmp)
    else:
        print("function name not defined yet")
        

def p_expr_statement_assign(token):
    """
        statement : ID EQUALS expr
                  | ID TIMESEQUAL expr
                  | ID PLUSEQUAL expr
    """
    if token[2] == '=':
        names[token[1]] = token[3]
    elif token[2] == '*=':
        if token[1] not in names:
            names[token[1]] = 0
        actual = names[token[1]]
        names[token[1]] = token[3] * actual
    elif token[2] == '+=':
        if token[1] not in names:
            names[token[1]] = 0
        actual = names[token[1]]
        names[token[1]] = token[3] + actual

def p_if(token):
    """
        statement : IF LPAREN expr RPAREN liststatements statement_else
    """

def p_else(token):
    """statement_else : ELSE liststatements
                      | empty
    """

def p_while_loop(token):
    """
        statement : WHILE LPAREN expr RPAREN liststatements 
    """

def p_for_loop(token):
    """
        statement : FOR LPAREN expr SEMI expr SEMI expr RPAREN LBRACE liststatements RBRACE
    """
    token[0] = ('for', token[3], token[5], token[7], token[10])
#    aprint(token[0])
    print(evaluate(token[0]))

def p_not(token):
    """
        statement : NOT expr
    """
    token[0] = ('not', token[2])
    print(evaluate(token[0]))

def p_expr_number(token):
    """expr : NUMBER"""
    token[0] = ('num',token[1])

def p_expr_bool(token):
    '''
        expr : TRUE
             | FALSE
    '''
    token[0] = ('bool', token[1])

def p_expr_id(token):
    """expr : ID """
    if token[1] in names:
        token[0] = names[token[1]]
    else:
        print('identifier not defined')

def p_expr_paren(token):
    """
        expr : LPAREN expr RPAREN
    """
    token[0] = token[2]
    # print (evaluate(token[0]))

def p_expr_bin(token):
    """
        expr    : expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | expr POW expr
                | expr LT expr
                | expr GT expr
                | expr LE expr
                | expr GE expr
                | expr EQ expr
                | expr NE expr
                | expr OR expr
                | expr AND expr
    """
    if token[2] == '+':
        token[0] = ('+', token[1], token[3])
    elif token[2] == '-':
        token[0] = ('-',token[1],token[3])
    elif token[2] == '*':
        token[0] = ('*', token[1] , token[3])
    elif token[2] == '/':
        token[0] = ('/', token[1] , token[3])
    elif token[2] == '^':
        token[0] = ('^', token[1] , token[3])
    elif token[2] == '<':
         token[0] = ('<' , token[1] , token[3])
    elif token[2] == '<=':
        token[0] = ('<=' , token[1] , token[3])
    elif token[2] == '>=':
        token[0] = ('>=' , token[1] , token[3])
    elif token[2] == '>':
        token[0] = ('>' , token[1] , token[3])
    elif token[2] == '&&':
        token[0] = ('&&' , token[1] , token[3])
    elif token[2] == '||':
        token[0] = ('||' , token[1] , token[3])
    elif token[2] == '!=':
        token[0] = ('!=' , token[1] , token[3])
    # print(evaluate(token[0]))

def p_expression_uminus(token):
    """expr : MINUS expr %prec UMINUS"""
    token[0] = -token[2]

def p_ternary(p):
    '''
        expr : expr QUESTION expr COLLUMN expr
    '''
    p[0] = ('ternary', p[1], p[3], p[5])
    evaluate(p[0])

def p_params(token):
    """
        listParams : ID COMMA listParams
                   | ID
                   | empty
    """

def p_statements(t):
    """
        liststatements : expr SEMI liststatements
    """
    t[0] = ('liststatments' , t[1], t[3])

def p_statments_alone(t):
    '''
        liststatements : expr        
    '''    
    t[0] = t[1]

def p_statments_empty(t):
    '''
        liststatements : empty        
    '''
    pass

def p_error(t):
    print('Syntax Error in input !', t)

def p_empty(token):
    """empty :  """
    pass

def evaluate(lst):
    if(lst[0] == 'num'):
        return lst[1]
    elif(lst[0] == 'id'):
        return names.get(lst[1] , None)
    elif(lst[0] == None):
        print('Identifier invalid')
    elif(lst[0] == 'bool'):
        return True if lst[1] == 'true' else False
    elif(lst[0] == '+'):
        return evaluate(lst[1]) + evaluate(lst[2])
    elif(lst[0] == '-'):
        return evaluate(lst[1]) - evaluate(lst[2])
    elif(lst[0] == '*'):
        return evaluate(lst[1]) * evaluate(lst[2])
    elif(lst[0] == '^'):
        return evaluate(lst[1]) ** evaluate(lst[2])
    elif(lst[0] == '/'):
        return evaluate(lst[1]) / evaluate(lst[2])
    elif(lst[0] == '<'):
        return evaluate(lst[1]) < evaluate(lst[2])
    elif(lst[0] == '<='):
        return evaluate(lst[1]) <= evaluate(lst[2])
    elif(lst[0] == '>'):
        return evaluate(lst[1]) > evaluate(lst[2])
    elif(lst[0] == '>='):
        return evaluate(lst[1]) >= evaluate(lst[2])
    elif(lst[0] == '&&'):
        return evaluate(lst[1]) and evaluate(lst[2])
    elif(lst[0] == '||'):
        return evaluate(lst[1]) or evaluate(lst[2])
    elif(lst[0] == '!='):
        return evaluate(lst[1]) != evaluate(lst[2])
    elif(lst[0] == 'not'):
        return not evaluate(lst[1])
    elif(lst[0] == 'liststatments'):
        return ( evaluate(lst[1]) , evaluate(lst[2]) )
    
    elif(lst[0] == 'ternary'):
        return lst[1] if evaluate(lst[2]) else lst[3]

    elif(lst[0] == 'for'):
        for i in range(evaluate(lst[1]),evaluate(lst[2]), evaluate(lst[3])):
            print(evaluate(lst[4]))
        return
    elif(lst[0] == 'define'):
        params = funtionStack.pop() if len(funtionStack) > 0 else None
        return evaluate(names[lst[1]][2])


def parse(data):
    parser.parse(data)

logging.basicConfig(
        level = logging.DEBUG,
        filename = "bc.log",
        filemode = "w",
        format = "%(filename)10s:%(lineno)4d:%(message)s"
        )
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log, errorlog=log)
