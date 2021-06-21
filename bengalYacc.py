from bengalLex import *
import ply.yacc as yacc
import sys
 
 
#---------------------------- Funciones ------------------------------------
def Avails(num):
    a = []
    for i in range(num) :
        t = 'T'
        t = t+str(i)
        a.append(t)
    return a     
        
def hacerLista(*elementos):
    lista = []
    for j in elementos:
        lista.append(j)
    global cont
    cont = cont + 1
    return lista

def tablaSim(*elementos):
    lst = []
    for k in elementos:
        lst.append(k)
    global dirSim
    dirSim = dirSim + 1  
    return lst

def rellenar(direc, cont): 
    cuadruplos[direc].append(str(cont))

#-------------------------------------------------------     
def guardar(valor, variab):  
     for idx,item in enumerate(simbolos):
         if variab in item[0]:
             if len(item) == 3:
                 item.pop()
                 item.append(str(valor))
             else:
                 item.append(str(valor))
              
def recuperar(variab): 
    try:
        float(variab)
        vl = variab
        return vl
    except ValueError:
        for list in simbolos:
            if list[0] == variab:
                vl = list[2]
                return vl

def printB(variable):
    bandera = False
    try: 
        float(variable)
        vl = variable
        print(vl) 
    except ValueError:
        for list in simbolos:
            if list[0] == variable:
                vl = list[2]
                print(vl) 
                bandera = False
                break
            else:
                bandera = True
    if bandera == True:
        print(variable)
        bandera = False 

#----------------------------- VARIABLES ----------------------------------
simbolos = []
tabla_temporales = [[] for i in range(30)]

nombre_var = [] #lista de nombres al declarar
nom = ""
tipo_var = ""
variable = ""
varOutput =""
space = " "
proceso_nom = ""

checkpoint = 0
checkpoint2 = 0
checkpoint3 = 0
i_dimen = ""
exp_dim = ""
parte1 = ""
parte2 = ""
parte3 = ""
parte4 = ""

n1 = ""
n2 = ""
n3 = ""
n4 = ""

pila_operandos = []
pila_saltos = []
cont = 0
dirSim = 0
temp = ''
avail = Avails(30)

for ind,x in enumerate(avail):         # Se hace una lista de listas para la tabla de temporales
   tabla_temporales[ind].append(x)
   tabla_temporales[ind].append('temp')

for y in tabla_temporales:             #Junto la tabla de simo
    simbolos.append(y)
    
cuadruplos = []        #Lista de listas de cuadruplos

#--------------------------------------------------------------------------

#-----------------------Definición del programa principal-------------------
def p_programa(p):
    '''
    programa : START A1 variables procedures A2 main END A3 
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
               simbolos.append(tablaSim(x, tipo_var)) 
            nombre_var.clear()
            tipo_var = ""

             
def p_B(p):   
    '''
    B : ID COMA B
      | ID 
    ''' 
    global nombre_var  
    global nom 
    nom = p[1]


def p_C(p):  
    '''
    C : NORMAL 
      | ARRAY 
      | MATRIZ 
      | CUBO 
    '''
def p_NORMAL(p):
    '''
    NORMAL : 
    '''
    nombre_var.append(nom)

def p_ARRAY(p):
    '''
    ARRAY : IZQCORCH CTE DERCORCH
    '''
    for i in range(int(p[2])):
        nombre_var.append(nom + str(i)) 
   # print(nombre_var)

def p_MATRIZ(p):
    '''
    MATRIZ : IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
    '''
    for i in range(int(p[2])):
        for j in range(int(p[5])):
            nombre_var.append(nom + str(i) + str(j))
    #print(nombre_var)

def p_CUBO(p):
    '''
    CUBO : IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
    '''
    for i in range(int(p[2])):
        for j in range(int(p[5])):
            for k in range(int(p[8])):
                nombre_var.append(nom + str(i) + str(j) + str(k))
    #print(nombre_var)
    
    
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
    procedures : SUB PROCEDURE A4 main RETURN ';' A5 procedures
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
      | INPUT var AUX14
      | OUTPUT IZQPAR K DERPAR AUX12
      | OUTPUT var AUX13
      | IF EL THEN AUX1 G L  
      | WHEN AUX4 EL AUX5 DO G AUX6 END
      | DO AUX4 G WHEN EL  AUX7 END
      | FOR AUX8 LINK EA AUX9 TO EA AUX10 DO G AUX11 END
      | GO '#' ID
      | GOSUB AUX15
      | EA
      |
    '''  
    global variable
    global checkpoint
    global parte1, parte2, parte3
    if  p[2] == '<=':
        if len(pila_operandos) >= 1:
            operando1 = pila_operandos.pop()
            if checkpoint == 1:
                cuadruplos.append(hacerLista('checar', str(operando1), parte1, parte2)) 
                checkpoint = 0
                
            elif checkpoint == 2:
                cuadruplos.append(hacerLista('checar2', str(operando1), parte1, parte2, parte3))
                checkpoint = 0
                
            elif checkpoint == 3:
                cuadruplos.append(hacerLista('checar3', str(operando1), parte1, parte2, parte3, parte4))
                checkpoint = 0                
            else:
                cuadr = hacerLista('=', str(operando1), variable)
                cuadruplos.append(cuadr)
            
    
def p_G(p):
    '''
    G : G S ';'
      | S ';'
    ''' 
    
def p_L(p):
    '''
    L : ELSE AUX2 G AUX3 END
      | AUX3 END
    ''' 
    
def p_K(p):
    '''
    K : K ID
      | K CTE
      | SIM
      | CTE
      | ID
    '''
    global varOutput 
    global space
    if p[1] != None:
        varOutput = varOutput + space + str(p[1])
    elif p[1] == None:
        varOutput = varOutput + space + str(p[2])
         
def p_var(p):
    '''
    var : var_normal  
        | var_array
        | var_matriz
        | var_cubo
    '''  

 
def p_var_normal(p):
    '''
    var_normal : ID  
    '''     
    global variable
    variable = p[1]
    
def p_var_array(p):
    '''
    var_array : ID IZQCORCH CTE DERCORCH
              | ID IZQCORCH ID DERCORCH
              
    '''  
    global variable
    global checkpoint
    global parte1, parte2   

    if p[3] in (item[0] for item in simbolos):
        parte1 = p[1]
        parte2 = p[3]
        variable = p[1] + p[3] 
        checkpoint = 1  #checkpoint = 1 significa que es un array 
    else:
        if isinstance(p[3], int) == True:
            variable = p[1] + p[3]
        elif isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
            variable = p[1] + i 
        else:
            sys.exit(str(p[3]) + ' no fue definido')
    

def p_var_matriz(p):
    '''
    var_matriz : ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
               | ID IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH
    '''    
    global variable
    global checkpoint
    global parte1, parte2, parte3  

    if all(w in (item[0] for item in simbolos) for w in [p[3], p[6]]): #checar si varios elementos en lista de listas
        parte1 = p[1]
        parte2 = p[3]
        parte3 = p[6]
        variable = p[1] + p[3] + p[6]
        checkpoint = 2 #checkpoint = 2 significa que es una matriz 
    else:
        if isinstance(p[3], int) == True:
            i = p[3]
        if isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
        if isinstance(p[6], int) == True:
            j = p[6]
        if isinstance(p[6], float) == True:
            left_text = str(p[6]) 
            j = left_text.partition(".")[0] 
       
        else:
            sys.exit(str(p[3]) + ' no fue definido')    
        
        variable = p[1] + i + j  
    
def p_var_cubo(p):
    '''
    var_cubo : ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
             | ID IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH
    '''    
    global variable
    global checkpoint
    global parte1, parte2, parte3, parte4  

    if all(w in (item[0] for item in simbolos) for w in [p[3], p[6], p[9]]): #checar si varios elementos en lista de listas
        parte1 = p[1]
        parte2 = p[3]
        parte3 = p[6]
        parte4 = p[9]
        variable = p[1] + p[3] + p[6] + p[9]
        checkpoint = 3 #checkpoint = 2 significa que es una matriz 
    else:
        if isinstance(p[3], int) == True:
            i = p[3]
        if isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
        if isinstance(p[6], int) == True:
            j = p[6]
        if isinstance(p[6], float) == True:
            left_text = str(p[6]) 
            j = left_text.partition(".")[0] 
        if isinstance(p[9], int) == True:
            k = p[9]
        if isinstance(p[9], float) == True:
            left_text = str(p[9]) 
            k = left_text.partition(".")[0]             
       
        else:
            sys.exit(str(p[3]) + ' no fue definido')    
        
        variable = p[1] + i + j + k

    
#Expresiones Aritmeticas    
def p_EA(p):
    '''
    EA : EA SUMA TA
       | EA RESTA TA
       | TA AUX
    ''' 
    
    global temp
    global id_dimen
    global checkpoint2 
    if p[2] == '+' or p[2] == '-':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            
            if checkpoint2 == 0: 
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '0'))
                checkpoint2 = 0
            elif checkpoint2 == 1:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '1'))
                checkpoint2 = 0
            elif checkpoint2 == 2:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '2'))
                checkpoint2 = 0
            else:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '3'))
                checkpoint2 = 0

                
            checkpoint2 = 0    
            pila_operandos.append(temp)
            
def p_TA(p):
    '''
    TA : TA MULT FA
       | TA DIV FA
       | FA AUX       
    '''   
    global temp
    global id_dimen
    global checkpoint2
    
    if p[2] == '*' or p[2] == '/':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            
            if checkpoint2 == 0: 
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '0'))
                checkpoint2 = 0
            elif checkpoint2 == 1:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '1'))
                checkpoint2 = 0
            elif checkpoint2 == 2:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '2'))
                checkpoint2 = 0
            else:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '3'))
                checkpoint2 = 0
                
            checkpoint2 = 0    
            pila_operandos.append(temp)


def p_FA(p):
    '''
    FA : FA_normal  
        | FA_array
        | FA_matriz
        | FA_cubo
        | FA_CTE 
        | IZQPAR EA DERPAR
    '''  

def p_FA_normal(p):
    '''
    FA_normal : ID 
    '''  
    if p[1] in (item[0] for item in simbolos):
        pila_operandos.append(p[1])
    checkpoint2 = 0
         
def p_FA_array(p):
    '''
    FA_array : ID IZQCORCH CTE DERCORCH
             | ID IZQCORCH ID DERCORCH
    '''        
    global exp_dim 
    global checkpoint2 
   # global checkpoint
    global parte1, parte2  
    
    
    if p[3] in (item[0] for item in simbolos):
    #    parte1 = p[1]   
    #   parte2 = p[3]
        exp_dim = p[1] + p[3] 
        checkpoint2 = 1  #checkpoint = 1 significa que es un array 
    #    checkpoint = 1
    else:
        if isinstance(p[3], int) == True:
            exp_dim = p[1] + p[3] 
        elif isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
            exp_dim = p[1] + i 
        else:
            sys.exit(str(p[3]) + ' no fue definido')
            
    pila_operandos.append(exp_dim)  

    
def p_FA_matriz(p):
    '''
    FA_matriz : ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
              | ID IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH
    '''  
    global exp_dim
    global checkpoint2
    global n1, n2  
    
    
    if all(w in (item[0] for item in simbolos) for w in [p[3], p[6]]): #checar si varios elementos en lista de listas
        exp_dim = p[1] + p[3] + p[6]
        checkpoint2 = 2  #checkpoint = 1 significa que es un array 
    else:
        if isinstance(p[3], int) == True:
            i = p[3]
        if isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
        if isinstance(p[6], int) == True:
            j = p[6]
        if isinstance(p[6], float) == True:
            left_text = str(p[6]) 
            j = left_text.partition(".")[0] 
       
        else:
            sys.exit(str(p[3]) + ' no fue definido')    
        
        exp_dim = p[1] + i + j         
            
    pila_operandos.append(exp_dim)      
    
    
def p_FA_cubo(p):
    '''
    FA_cubo : ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
            | ID IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH
    '''  
    global exp_dim
    global checkpoint2
    global n1, n2   
    
    if all(w in (item[0] for item in simbolos) for w in [p[3], p[6], p[9]]): #checar si varios elementos en lista de listas
        exp_dim = p[1] + p[3] + p[6] + p[9]
        checkpoint2 = 3 #checkpoint = 2 significa que es una matriz 
    else:
        if isinstance(p[3], int) == True:
            i = p[3]
        if isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
        if isinstance(p[6], int) == True:
            j = p[6] 
        if isinstance(p[6], float) == True:
            left_text = str(p[6]) 
            j = left_text.partition(".")[0] 
        if isinstance(p[9], int) == True:
            k = p[9]
        if isinstance(p[9], float) == True:
            left_text = str(p[9]) 
            k = left_text.partition(".")[0]             
       
        else:
            sys.exit(str(p[3]) + ' no fue definido')    
        
        exp_dim = p[1] + i + j + k    
        
    pila_operandos.append(exp_dim)
    
def p_FA_CTE(p):
    '''
    FA_CTE : CTE
    '''  
    pila_operandos.append(p[1])

                
def p_AUX(p):
    '''     
    AUX :
    '''  
                  
#Expresiones Logicas      
def p_EL(p):
    '''
    EL : EL OR TL
       | EL AND TL
       | TL AUX
    ''' 
    global temp
    global checkpoint3
    
    if p[2] == 'or' or p[2] == 'and':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            
            if checkpoint3 == 0:  
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '0'))
                checkpoint3 = 0
            elif checkpoint3 == 1:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '1'))
                checkpoint3 = 0
            elif checkpoint3 == 2:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '2'))
                checkpoint3 = 0
            else:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '3'))
                checkpoint3 = 0
                
            checkpoint3 = 0    
            pila_operandos.append(temp)
   
             
def p_TL(p):
    '''        
    TL : TL NOT FL
       | FL AUX
    ''' 
    global temp
    global checkpoint3
    if p[2] == 'not':
       if len(pila_operandos) >= 2:
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            temp = avail.pop(0)
            
            if checkpoint3 == 0:  
                cuadruplos.append(hacerLista(p[2], str(operando1), temp, '0'))
                checkpoint3 = 0
            elif checkpoint3 == 1:
                cuadruplos.append(hacerLista(p[2], str(operando1), temp, '1'))
                checkpoint3 = 0
            elif checkpoint3 == 2:
                cuadruplos.append(hacerLista(p[2], str(operando1), temp, '2'))
                checkpoint3 = 0
            else:
                cuadruplos.append(hacerLista(p[2], str(operando1), temp, '3'))
                checkpoint3 = 0
                
            checkpoint3 = 0     
            pila_operandos.append(temp)
            

            
    
def p_FL(p):
    '''     
    FL : H MAYOR H
       | H MENOR H
       | H MAYOR_IGUAL H
       | H MENOR_IGUAL H 
       | H EQUAL H
       | H NOTEQUAL H
       | IZQPAR EL DERPAR
    '''
    global temp
    global checkpoint3
    
    if p[2] == '<' or p[2] == '>' or p[2] == '==' or p[2] == '!=' or  p[2] == '=<' or  p[2] == '=>':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            
            if checkpoint3 == 0:  
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '0'))
                checkpoint3 = 0
            elif checkpoint3 == 1:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '1'))
                checkpoint3 = 0
            elif checkpoint3 == 2:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '2'))
                checkpoint3 = 0
            else:
                cuadruplos.append(hacerLista(p[2], str(operando1), str(operando2), temp, '3'))
                checkpoint3 = 0
                
            checkpoint3 = 0    
            pila_operandos.append(temp)
            
        
            
# =============================================================================
# def p_H(p):
#     '''     
#     H : ID
#       | CTE
#       | ID IZQCORCH EA DERCORCH
#       | ID IZQCORCH EA DERCORCH IZQCORCH EA DERCORCH
#       | ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
#       | IZQPAR EL DERPAR
#     '''  
#     global pila_operandos
#     if p[1] != '(' and p[1] != None:
#         if p[1] in (item[0] for item in simbolos):
#             pila_operandos.append(p[1])
#         else:
#             if isinstance(p[1], int) == True:
#                 pila_operandos.append(p[1])
#             elif isinstance(p[1], float) == True:
#                 pila_operandos.append(p[1])
#             else:
#                 sys.exit(str(p[1]) + ' no fue definido')
# =============================================================================
                  
def p_H(p):
    '''
    H : H_normal  
        | H_array
        | H_matriz
        | H_cubo
        | H_CTE 
        | IZQPAR EL DERPAR
    '''  
def p_H_normal(p):
    '''
    H_normal : ID 
    '''  
    if p[1] in (item[0] for item in simbolos):
        pila_operandos.append(p[1])
    checkpoint3 = 0
         
def p_H_array(p):
    '''
    H_array : ID IZQCORCH CTE DERCORCH
             | ID IZQCORCH ID DERCORCH
    '''        
    global exp_dim
    global checkpoint3 
    global n1, n2  
    
    
    if p[3] in (item[0] for item in simbolos):
        exp_dim = p[1] + p[3] 
        checkpoint3 = 1  #checkpoint = 1 significa que es un array 
    else:
        if isinstance(p[3], int) == True:
            exp_dim = p[1] + p[3] 
        elif isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
            exp_dim = p[1] + i 
        else:
            sys.exit(str(p[3]) + ' no fue definido')
            
    pila_operandos.append(exp_dim)  

    
def p_H_matriz(p):
    '''
    H_matriz : ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
              | ID IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH
    '''  
    global exp_dim
    global checkpoint3
    global n1, n2  
    
    
    if all(w in (item[0] for item in simbolos) for w in [p[3], p[6]]): #checar si varios elementos en lista de listas
        exp_dim = p[1] + p[3] + p[6]
        checkpoint3 = 2  #checkpoint = 1 significa que es un array 
    else:
        if isinstance(p[3], int) == True:
            i = p[3]
        if isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
        if isinstance(p[6], int) == True:
            j = p[6]
        if isinstance(p[6], float) == True:
            left_text = str(p[6]) 
            j = left_text.partition(".")[0] 
       
        else:
            sys.exit(str(p[3]) + ' no fue definido')    
        
        exp_dim = p[1] + i + j         
            
    pila_operandos.append(exp_dim)      
    
    
def p_H_cubo(p):
    '''
    H_cubo : ID IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH IZQCORCH CTE DERCORCH
            | ID IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH IZQCORCH ID DERCORCH
    '''  
    global exp_dim
    global checkpoint3
    global n1, n2   
    
    if all(w in (item[0] for item in simbolos) for w in [p[3], p[6], p[9]]): #checar si varios elementos en lista de listas
        exp_dim = p[1] + p[3] + p[6] + p[9]
        checkpoint3 = 3 #checkpoint = 2 significa que es una matriz 
    else:
        if isinstance(p[3], int) == True:
            i = p[3]
        if isinstance(p[3], float) == True:
            left_text = str(p[3]) 
            i = left_text.partition(".")[0] 
        if isinstance(p[6], int) == True:
            j = p[6]
        if isinstance(p[6], float) == True:
            left_text = str(p[6]) 
            j = left_text.partition(".")[0] 
        if isinstance(p[9], int) == True:
            k = p[9]
        if isinstance(p[9], float) == True:
            left_text = str(p[9]) 
            k = left_text.partition(".")[0]             
       
        else:
            sys.exit(str(p[3]) + ' no fue definido')    
        
        exp_dim = p[1] + i + j + k    
        
    pila_operandos.append(exp_dim)
    
def p_H_CTE(p):
    '''
    H_CTE : CTE
    '''  
    pila_operandos.append(p[1])    
#----------------- AUXILIARES (sirven para la programación) ---------------

#--------------Auxiliares del "IF"--------------

def p_AUX1(p):      #Primer auxiliar del "if"
    '''     
    AUX1 :
    '''          
    te = pila_operandos.pop()
    cuadr = hacerLista('gotoF', te)
    cuadruplos.append(cuadr)
    pila_saltos.append(cont - 1)
    
def p_AUX2(p):        #Segundo auxiliar del "if"
    '''     
    AUX2 :
    '''          
    direc = pila_saltos.pop()
    cuadr = hacerLista('goto')
    cuadruplos.append(cuadr)
    pila_saltos.append(cont - 1)
    rellenar(direc, cont)     
    
def p_AUX3(p):        #Tercer auxiliar del "if"
    '''     
    AUX3 :
    '''          
    direc = pila_saltos.pop()
    rellenar(direc, cont)    
    
#--------------Auxiliares del "WHILE" y "DO WHILE"--------------

def p_AUX4(p):        #Primer auxiliar del "while" y "do while"
    '''     
    AUX4 :
    '''          
    pila_saltos.append(cont)    

def p_AUX5(p):        #Segundo auxiliar del "while"
    '''     
    AUX5 :
    '''         
    tr = pila_operandos.pop()
    cuadr = hacerLista('gotoF', tr)
    cuadruplos.append(cuadr)
    pila_saltos.append(cont - 1)

def p_AUX6(p):        #Tercer auxiliar del "while"
    '''     
    AUX6 :
    '''           
    dir1 = pila_saltos.pop()
    dir2 = pila_saltos.pop()
    cuadr = hacerLista('goto', str(dir2))
    cuadruplos.append(cuadr)
    rellenar(dir1, cont)

def p_AUX7(p):        #Segundo auxiliar del " do while"
    '''     
    AUX7 :
    '''          
    cuadr = hacerLista('gotoF', str(pila_operandos.pop()), str(pila_saltos.pop()))
    cuadruplos.append(cuadr)


#-------------------- Auxiliares del ciclo for -------------------------------
def p_AUX8(p):        #Primer auxiliar del ciclo for
    '''     
    AUX8 : ID
    '''
    if p[1] != None:
        if p[1] in (item[0] for item in simbolos):
            pila_operandos.append(p[1])
        else:
            sys.exit(str(p[1]) + ' no fue definido')
                
            
def p_AUX9(p):        #Segundo auxiliar del ciclo for
    '''     
    AUX9 : 
    '''
    exp1 = pila_operandos.pop()
    id1 =  pila_operandos[-1]     
    cuadr = hacerLista('=', str(exp1), id1)
    cuadruplos.append(cuadr)       
            
def p_AUX10(p):        #Tercer auxiliar del ciclo for
    '''     
    AUX10 : 
    '''
    global tf
    tf = avail.pop(0)
    exp2 = pila_operandos.pop() 
    #print(exp2)
    tx = avail.pop(0) 
    id2 =  pila_operandos[-1]     
    cuadruplos.append(hacerLista('=', str(exp2), tf))   
    cuadruplos.append(hacerLista('<', id2, tf, tx, '0'))  
    cuadruplos.append(hacerLista('gotoF', tx)) 
    avail.insert(0, tx)
    pila_saltos.append(cont-2) 

def p_AUX11(p):        #Tercer auxiliar del ciclo for
    '''     
    AUX11 : 
    '''
    
    id3 = pila_operandos.pop()
    cuadruplos.append(hacerLista('+', id3, 1, id3, '0')) 
    retorno = pila_saltos.pop()
    cuadruplos.append(hacerLista('goto', retorno)) 
    rellenar(retorno+1, cont)
    avail.insert(0, tf)
    
#------------------------ Auxiliares del INPUT y OUPTUT -----------------------------
def p_AUX12(p):        # 1er Auxiliar del Output
    '''     
    AUX12 : 
    '''
    global varOutput
    cuadruplos.append(hacerLista('output', varOutput, '0')) 
    varOutput = ""
    
def p_AUX13(p):        # 2ndo Auxiliar del Output
    '''     
    AUX13 : 
    '''    
    global checkpoint
    
    if checkpoint == 1:
        cuadruplos.append(hacerLista('output', variable, '1')) 
        checkpoint = 0
                
    elif checkpoint == 2:
        cuadruplos.append(hacerLista('output', variable, '2')) 
        checkpoint = 0
                
    elif checkpoint == 3:
        cuadruplos.append(hacerLista('output', variable, '3')) 
        checkpoint = 0                
    else:
        cuadruplos.append(hacerLista('output', variable, '0')) 

        


def p_AUX14(p):        # Auxiliar del Input
    '''     
    AUX14 : 
    '''    
    global checkpoint
    
    if checkpoint == 1:
        cuadruplos.append(hacerLista('input', variable, '0'))
        checkpoint = 0
                
    elif checkpoint == 2:
        cuadruplos.append(hacerLista('input', variable, '0'))
        checkpoint = 0
                
    elif checkpoint == 3:
        cuadruplos.append(hacerLista('input', variable, '0'))
        checkpoint = 0                
    else:
        cuadruplos.append(hacerLista('input', variable, '0'))

# =============================================================================
#     if variable in (item[0] for item in simbolos):
#         cuadruplos.append(hacerLista('input', variable))
#     else:
#         sys.exit(variable + ' no fue definido')   
# =============================================================================
    
#------------------------- Auxiliar del GOSUB --------------------------------------
    
def p_AUX15(p):        #Primer auxiliar del GOSUB
    '''     
    AUX15 : ID
    '''
    proced = recuperar(p[1])
    cuadruplos.append(hacerLista('call', proced))
            
#------------------------ Auxiliares del main program -----------------------------
def p_A1(p):        # 1er Auxiliar del Main
    '''     
    A1 : 
    '''
    cuadruplos.append(hacerLista('goto'))

def p_A2(p):        # 2ndo Auxiliar del Main
    '''     
    A2 : 
    '''
    rellenar(0, cont)

def p_A3(p):        # 3er Auxiliar del Main
    '''     
    A3 : 
    '''
    cuadruplos.append(hacerLista('finPrograma'))

#------------------------ Auxiliares de los procedures -----------------------------
def p_A4(p):        # 1er Auxiliar del procedure
    '''     
    A4 : ID
    
    '''
    global proceso_nom 
    proceso_nom = p[1]
    simbolos.append([proceso_nom, 'procedimiento', str(cont)])

def p_A5(p):        # 2ndo Auxiliar del procedure
    '''     
    A5 : 
    '''
    cuadruplos.append(hacerLista('finProcedure'))



def p_error(p):
    print("\tINCORRECTO")

#--------------- Se crea el parser -------------------------
parser = yacc.yacc()

#--------------- Pruebas con diferentes archivos ------------
try:

    f = open("Final3.txt", "r")
    #f = open("numeros_imprimir.txt", "r")
    contenido = f.read()
    parser.parse(contenido)


except EOFError:
    PASS
    

#------------- PRINTS -----------------------------------

#---------------------------------------------------------------
# =============================================================================
# print('----------Tabla de simbolos-------')
# for sim in enumerate(simbolos):
#     print(*sim)
# 
# print('\n--------Código Intermedio ----------')
# for s in cuadruplos:
#     print(s)  #cuadruplos es una lista de listas. Con el * se itera en cada lista e imprime los valores de cada lista sin corchetes ni comas
#     #print(s)   #Formato de listas
#     
# =============================================================================
# =============================================================================
#     
# print('\n----------Pilas------------')    
# print("Avails:", avail)
# print("pila operandos:", pila_operandos)
# print("pila saltos:", pila_saltos)
# print("Contador:", cont)
# print("Direcciones:", dirSim)
# #---------------------------------------------
# =============================================================================


