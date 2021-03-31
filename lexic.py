import ply.lex as lex
import ply.yacc as yacc
import sys

reserved = {
    'start': 'START',
    'end' : 'END',
    'dim' : 'DIM',
    'is' : 'IS',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'when' : 'WHEN',
    'do' : 'DO',
    'for' : 'FOR',
    'to' : 'TO',
    'gosub' : 'GOSUB',
    'go' : 'GO',
    'input' : 'INPUT',
    'output' : 'OUTPUT',
    'sub procedure' : 'SUBPROCEDURE',
    'return' : 'RETURN',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    '#' : 'WHERE'
        
 }

tokens = [      #Todos los tokens que se vayan a usar
    'ID',
    'CTE',
    'WORD',
    'FLOAT',

    
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'IZQPAR',
    'DERPAR',
    'IZQCORCH',
    'DERCORCH',
    'LINK',
    'COMA',
    'COMMENT'
        
] + list(reserved.values())

literals = "+-/*()[], ;:^<>.|" 

#Ignoramos los espacios
t_ignore = r' '  
 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_\d\[\]]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTE(t):
        r'\d+'
        t.value = int(t.value)    
        return t 
    
def t_WORD(t):
    r'\"[a-z A-Z_\d]+\"'
    t.value = str(t.value)
    return t    

def t_FLOAT(t):
        r'\d+\.\d+'
        t.value = float(t.value)    
        return t 
    
 #Expresiones Regulares para tokens simples
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_MULT   = r'\*'
t_DIV  = r'/'
t_IZQPAR  = r'\('
t_DERPAR  = r'\)'
t_IZQCORCH  = r'\['
t_DERCORCH  = r'\]'
t_LINK = r'\<\='   

def t_COMA(t):
    r'\,'
    t.type = 'COMA'
   # print(",")
    return t
 
#Comentarios (//) 
def t_COMMENT(t): 
    r'\//.*'
    pass
    
# Define a rule so we can track line numbers
def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)   

# Error handling rule
def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

# Se crea el lexer 
lexer = lex.lex()

##################################################

def p_S(p):
	'''
	S : X QUE TAL 
	'''
	print("\tCORRECTO")

def p_X(p):
	'''
	X : HOLA Y
	'''

def p_Y(p):
	'''
	Y : COMA HOLA Y
	  | 
	'''
      
def p_error(p):
	print("\tINCORRECTO")

# Se crea el parser 
parser = yacc.yacc()

while True:
	try:
		s = input('')
	except EOFError:
		break
	parser.parse(s)
