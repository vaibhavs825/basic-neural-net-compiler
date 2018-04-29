import ply.lex as lex
import ply.yacc as yacc
import sys

# Create a list to hold all of the token names
tokens = [

    'int',
    'float',
    'string',
    'load',
    'split',
    'filepath',
    'input',
    'output',
    'index',
    'train',
    'use',
    'sequential',
    'test',
    'add_layer',
    'compile',
    'fit',
    'evaluate',
    'relu',
    'sigmoid',
    'adam'

]
t_load = r'(load)'
t_split = r'(split)'
t_input = r'(input)'
#t_ouptut = r'(output)'
t_train = r'(train)'
t_use = r'(use)'
t_sequential = r'(sequential)'
t_test = r'(test)'
t_add_layer = r'(add_layer)'
t_compile = r'(compile)'
t_fit = r'(fit)'
t_evaluate = r'(evaluate)'
t_relu = r'(relu)'
t_sigmoid = r'(sigmoid)'
t_adam = r'(adam)'
t_ignore = r' '

def t_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_int(t):
    r'\d+'
    t.value = int(t.value)
    return t


'''def t_load(t):
    r'(load)'
    t.type = 'load'
    return t
'''
def t_filepath(t) :
    #r'^(.+)\/([^\/]+)$'
    r'[a-zA-z]+\.csv'
    t.type = 'filepath'
    return t

'''def t_string(t):
    r'[a-zA-z]+'
    t.type = 'string'
    return t
'''
def t_index(t) :
    r'\[[0-9]+\]|\[[0-9]+\:[0-9]+\]'
    t.type = 'index'
    return t

def t_error(t) :
    print('Illegal type ')
    t.lexer.skip(1)

lexer = lex.lex()
'''
lexer.input("load read.csv")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''
'''while True:
    lexer = lex.lex()
    try:
        s = input('>> ')
    except EOFError:
        break
    print (s)
    lexer.input(s)
    while True :
        tok = lexer.token()
        if not tok:
            break
        print(tok)
'''

# --------------------------------------------- YACCC ------------
def p_start(p):
    '''
    start : LoadFile Split Use AddL Compile Fit Evaluate
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    #print (p[0])

def p_LoadFile(p) :
    '''
    LoadFile : load filepath
    '''
    p[0] = (p[1], p[2])

def p_Split(p) :
    '''
    Split : split splitinfo
    '''
    p[0] = (p[1], p[2])

def p_splitinfo(p) :
    '''
    splitinfo : input index
              | output index
    '''
    p[0] = (p[1], p[2])

def p_Use(p) :
    '''
    Use : use TON
    '''
    p[0] = (p[1], p[2])

def p_TON(p) :
    '''
    TON : sequential
    '''
    p[0] = (p[1])

def p_AddL(p) :
    '''
    AddL : add_layer int Act
    '''
    p[0] = (p[1], p[2], p[3])

def p_Act(p) :
    '''
    Act : relu
        | sigmoid
    '''
    p[0] = (p[1])

def p_Compile(p) :
    '''
    Compile : compile Optimizer
    '''
    p[0] = (p[1], p[2])

def p_Optimizer(p) :
    '''
    Optimizer : adam
    '''
    p[0] = (p[1])

def p_Fit(p) :
    '''
    Fit : fit epoch BatchSize
    '''
    p[0] = (p[1], p[2],p[3])

def p_epoch(p) :
    '''
    epoch : int
    '''
    p[0] = (p[1])

def p_BatchSize(p) :
    '''
    BatchSize : int
    '''
    p[0] = (p[1])

def p_Evaluate(p) :
    '''
    Evaluate : evaluate
    '''
    p[0] = (p[1])

'''
def p_error(p):
    print("Syntax error found!")
'''
parser = yacc.yacc()
while True :
    try :
        s = input (">> ")
    except EOFError :
        break
    parser.parse(s)
