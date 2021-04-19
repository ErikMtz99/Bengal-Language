from bengalLex import *
import ply.yacc as yacc
import sys

tabla_simbolos = {}

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

    A : A DIM B C IS tipo ';'
      | DIM B C IS tipo ';'
      
    B : ID COMA B
      | ID
      
    C : IZQCORCH CTE DERCORCH
      | IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
      |

tipo : WORD
     | FLOAT
     
    ''' 
    global tipo_var
    global nombre_var
    
    for t in p:
        if t != ',' and t != None:
           if (t == "float" or t == "word"):
              tipo_var = t
           elif (t != "is" and t != "dim" ):
               nombre_var = t
           else:
               if len(nombre_var) > 0:
                   left_text = nombre_var.partition("[")[0]
                   tabla_simbolos.update({left_text : tipo_var})

                   
                      
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
    
    H : ID
      | CTE
	'''  
    
def p_error(p):
	print("\tINCORRECTO")

# Se crea el parser 
parser = yacc.yacc()


try:
    f = open("prueba_variables2.txt", "r")
    #f = open("matricesEntrega_A01244818.txt", "r")
    #f = open("arit_logic_ProgramaPrueba.txt", "r")
    contenido = f.read()
    parser.parse(contenido)


except EOFError:
    PASS
     
for x, y in tabla_simbolos.items():
    print(x, y)    
#while True:
# 	try:
# 		s = input('')
# 	except EOFError:
# 		break
# 	parser.parse(s)
    
# =============================================================================
# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
# while True:
#     string = ''
#     espacio = ' '
#     line = input('')
#     while line != '':
#         string += line
#         string += espacio #El error era que despues de la palabra start no habia espacio. Se solucionó con esto.
#         line = input('')
# 
#     parser.parse(string)
# 
# 
# =============================================================================

