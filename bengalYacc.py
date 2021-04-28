from bengalLex import *
import ply.yacc as yacc
import sys

#Para los stacks
from collections import deque 
#----------------------------- VARIABLES ----------------------------------
tabla_simbolos = {}
nombre_var = []
tipo_var = ""

pila_operandos = []

avail = []
temp = ''
for i in range(11):
    t = 'T'
    t = t+str(i)
    avail.append(t)
   
cuadruplos = []
#--------------------------------------------------------------------------

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
    global nombre_var
    global tipo_var
    
    for t in p:
        if t ==';':
            for x in nombre_var:
               tabla_simbolos.update({x : tipo_var})
               nombre_var.clear()
               tipo_var = ""
             
def p_B(p):   
    '''
    B : ID COMA B
      | ID 
    ''' 
    global nombre_var 
    left_text = p[1].partition("[")[0]
    nombre_var.append(left_text)

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
    global tipo_var
    tipo_var = p[1]

    
                    
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
       | TA AUX
    ''' 
    
    global temp
    if p[2] == '+' or p[2] == '-':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            cuadruplos.extend([p[2], operando1, operando2, temp])
            pila_operandos.append(temp)
def p_TA(p):
    '''
    TA : TA MULT FA
       | TA DIV FA
       | FA AUX       
    '''  
    global temp
    if p[2] == '*' or p[2] == '/':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            cuadruplos.extend([p[2], operando1, operando2, temp])
            pila_operandos.append(temp)
    
def p_FA(p):
    '''
    FA : ID
       | CTE
       | IZQPAR EA DERPAR      
    '''    
    global pila_operandos
    if p[1] != '(' and p[1] != None:
        if p[1] in tabla_simbolos.keys():
            pila_operandos.append(p[1])
        else:
            if isinstance(p[1], int) != True:
               print(str(p[1]) + ' no fue definido')

      
        
#Expresiones Logicas      
def p_EL(p):
    '''
    EL : EL OR TL
       | EL AND TL
       | TL AUX
    ''' 
    global temp
    if p[2] == 'or' or p[2] == 'and':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            cuadruplos.extend([p[2], operando1, operando2, temp])
            pila_operandos.append(temp)
   
            
def p_TL(p):
    '''        
    TL : TL NOT FL
       | FL AUX
    ''' 
    global temp
    if p[2] == 'not':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            cuadruplos.extend([p[2], operando1, operando2, temp])
            pila_operandos.append(temp)
    
def p_FL(p):
    '''     
    FL : H MAYOR H
       | H MENOR H
       | H EQUAL H
       | H NOTEQUAL H
       | IZQPAR EL DERPAR
    '''
    global temp
    if p[2] == '<' or p[2] == '>' or p[2] == '==' or p[2] == '!=':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            cuadruplos.extend([p[2], operando1, operando2, temp])
            pila_operandos.append(temp)
        
            
def p_H(p):
    '''     
    H : ID
      | CTE
    '''  
    global pila_operandos
    if p[1] != None:
        if p[1] in tabla_simbolos.keys():
            pila_operandos.append(p[1])
        else:
            if isinstance(p[1], int) != True:
               print(str(p[1]) + ' no fue definido')
            
def p_AUX(p):
    '''     
    AUX :
    '''  
    
def p_error(p):
    print("\tINCORRECTO")

# Se crea el parser 
parser = yacc.yacc()


try:
    f = open("prueba_cuadruplos2.txt", "r")
    #f = open("prueba_variables.txt", "r")
    #f = open("matricesEntrega_A01244818.txt", "r")
    #f = open("arit_logic_ProgramaPrueba.txt", "r")
    contenido = f.read()
    parser.parse(contenido)


except EOFError:
    PASS
#------------- PRINTS -----------------------
print('---------Tabla de Símbolos------------')    
print("\n".join("{}\t{}\t{}".format(i, k, v) for i, (k, v) in enumerate(tabla_simbolos.items())))


print('\n--------Código Intermedio----------')
for i in range(0, len(cuadruplos), 4):
    print(*cuadruplos[i:i+4], sep=' ') 
    
print('\n----------Pilas------------')    
print(pila_operandos)
print(avail)
#---------------------------------------------
