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
    'sub' : 'SUB',
    'procedure' : 'PROCEDURE',
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
    'NOTEQUAL',
    'MAYOR',
    'MENOR'
        
] + list(reserved.values())

literals = "+-/*()[]=,!;:^<>.|#" 

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

def t_COMA(t):
        r'\,'
        t.type = 'COMA'    
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


t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_MAYOR = r'\>'
t_MENOR = r'\<'

#Comentarios (//) 
def t_COMMENT(t):
    r'\%.*'
    pass
    # No return value. Token discarded
  
 
# Define a rule so we can track line numbers
def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)   

# Error handling rule
def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)
    
def testLexer():
    lexer.input(testProgram)
    for tok in lexer:
        print(tok)
        
# Se crea el lexer 
lexer = lex.lex()

##################################################

####Definición del programa principal
def p_programa(p):
	'''
	programa : START variables procedures main END 
	'''
	print("\tCORRECTO")

####Definición de variables
def p_variables(p):
	'''
	variables : A
              | 
	'''
def p_A(p):
    '''
    A : A DIM B C IS tipo ';'
      | DIM B C IS tipo ';'
    '''   
def p_B(p):
    '''
    B : ID COMA B
      | ID
    '''     
def p_C(p):
    '''
    C : IZQCORCH CTE DERCORCH
      | IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
      |
    '''  
def p_tipo(p):
    '''
    tipo : WORD
         | FLOAT
    '''        
    
#### Definición de procedures (procedures)
def p_procedures(p):
    '''
	procedures : SUB PROCEDURE ID main RETURN ';' procedures
               |
	'''

#Definición del bloque de estatutos (main)
def p_main(p):
    '''
	main : E
	'''  
def p_E(p):
    '''
    E : E F S ';'
      | F S ';'
    ''' 
    
def p_F(p):
    '''
    F : WHERE ID ':'
      |
    '''     
    
#Definición de Estatutos (S)
def p_S(p):
    '''
	S : var LINK EA 
      | INPUT var 
      | OUTPUT IZQPAR K DERPAR
      | OUTPUT var
      | IF EL THEN G ELSE G END
      | WHEN EL DO G END
      | DO G WHEN EL END
      | FOR ID LINK EA TO EA DO G END
      | GO '#' ID
      | GOSUB ID
      | EA
      |
	''' 
def p_G(p):
    '''
    G : G S ';'
      | S ';'
    ''' 
def p_K(p):
    '''
    K : K ID
      | K CTE
      | CTE
      | ID
    '''     
def p_var(p):
    '''
    var : ID 
        | ID IZQCORCH EA DERCORCH
        | ID IZQCORCH EA DERCORCH IZQCORCH EA DERCORCH
    ''' 
# =============================================================================
# def p_J(p):
#     '''
#     J : J COMA EA
#       | EA    
#     '''  
# =============================================================================
    
#Expresiones Aritmeticas    
def p_EA(p):
    '''
	EA : EA SUMA TA
       | EA RESTA TA
       | TA
	''' 
def p_TA(p):
    '''
    TA : TA MULT FA
       | TA DIV FA
       | FA        
    '''  
def p_FA(p):
    '''
    FA : var
       | CTE
       | IZQPAR EA DERPAR      
    '''    
    
    #if p[2] == '+' : p[0] = p[1] + p[3]
    #elif p[2] == '-' : p[0] = p[1] - p[3]
    #elif p[2] == '*' : p[0] = p[1] * p[3]
    #elif p[2] == '/' : p[0] = p[1] / p[3]

#Expresiones Logicas      
def p_EL(p):
    '''
	EL : EL OR TL
       | EL AND TL
       | TL
       
    TL : TL NOT FL
       | FL
    
    FL : H MAYOR H
       | H MENOR H
       | H EQUAL H
       | H NOTEQUAL H
       | IZQPAR EL DERPAR
    
    H : var
      | CTE
	'''  
    
def p_error(p):
	print("\tINCORRECTO")

# Se crea el parser 
parser = yacc.yacc()

#while True:
# 	try:
# 		s = input('')
# 	except EOFError:
# 		break
# 	parser.parse(s)
    
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
while True:
    string = ''
    espacio = ' '
    line = input('')
    while line != '':
        string += line
        string += espacio #El error era que despues de la palabra start no habia espacio. Se solucionó con esto.
        line = input('')

    parser.parse(string)

