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
    'word' : 'WORD',
    'float' : 'FLOAT',
    '#' : 'WHERE'
        
 }

tokens = [      #Todos los tokens que se vayan a usar
    'ID',
    'CTE',
#    'WORD',
#    'FLOAT',

    
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
    'COMMENT',
    
    'EQUAL',
    'NOTEQUAL'
        
] + list(reserved.values())

literals = "+-/*()[],!;:^<>.|" 

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
    
#def t_WORD(t):
#    r'\"[a-z A-Z_\d]+\"'
#    t.value = str(t.value)
#    return t    

#def t_FLOAT(t):
#        r'\d+\.\d+'
#        t.value = float(t.value)    
#        return t 
    
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
t_COMA = r'\,'

t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
 
#Comentarios (//) 
def t_COMMENT(t): 
    r'\/\/.*'
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

def p_programa(p):
	'''
	programa : START variables procedures main END 
	'''
	print("\tCORRECTO")

def p_variables(p):
	'''
	variables : DIM A
              | 
              
    A : A B C IS tipo ';'
      | B C IS tipo ';'
      
    B : ID COMA B
      | ID
    
    C : IZQCORCH D DERCORCH
      |
    
    D : CTE COMA D
      | CTE
      
    tipo : WORD
         | FLOAT
	'''
    
def p_procedures(p):
    '''
	procedures : SUBPROCEDURE ID main RETURN ';' procedures
               |
	'''
def p_main(p):
    '''
	main : E
    
    E : E F S ';'
      | F S ';'
    
    F : WHERE ID ':'
      |
	'''  

def p_S(p):
    '''
	S : var LINK EA COMMENT
      | INPUT var
      | OUTPUT WORD
      | IF EL THEN G ELSE G END
      | WHEN EL DO G END
      | DO G WHEN EL END
      | FOR ID LINK EA TO EA DO G END
      | GO WHERE ID
      | GOSUB ID
      | EA
      |
    
    G : G S
      | S
     
    var : ID
        | ID IZQCORCH J DERCORCH 

    J : EA COMA J
    J : EA
	'''  
    
def p_EA(p):
    '''
	EA : EA SUMA TA
       | EA RESTA TA
       | TA
       
    TA : TA MULT FA
       | TA DIV FA
       | FA
    
    FA : CTE
       | ID
       | IZQPAR EA DERPAR
    
	'''  
def p_EL(p):
    '''
	EL : EL OR TL
       | EL AND TL
       | TL
       
    TL : TL NOT FL
       | FL
    
    FL : H '>' H
       | H '<' H
       | H EQUAL H
       | H NOTEQUAL H
       | IZQPAR EL DERPAR
    
    H : ID
      | CTE
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
