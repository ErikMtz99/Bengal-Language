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
tabla_temporales = [[] for i in range(10)]

nombre_var = []
tipo_var = ""
variable = ""
varOutput =""
space = " "
 
pila_operandos = []
pila_saltos = []
cont = 0
dirSim = 0
temp = ''
avail = Avails(10)

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
      | INPUT var AUX14
      | OUTPUT IZQPAR K DERPAR AUX12
      | OUTPUT var AUX13
      | IF EL THEN AUX1 G ELSE AUX2 G AUX3 END 
      | WHEN AUX4 EL AUX5 DO G AUX6 END
      | DO AUX4 G WHEN EL  AUX7 END
      | FOR AUX8 LINK EA AUX9 TO EA AUX10 DO G AUX11 END
      | GO '#' ID
      | GOSUB ID
      | EA
      |
    '''  
    global variable
    if  p[2] == '<=':
        if len(pila_operandos) >= 1:
            operando1 = pila_operandos.pop()
            cuadr = hacerLista('=', str(operando1), variable)
            cuadruplos.append(cuadr)
    
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
    global varOutput 
    global space
    if p[1] != None:
        varOutput = varOutput + space + str(p[1])
    elif p[1] == None:
        varOutput = varOutput + space + str(p[2])
         
def p_var(p):
    '''
    var : ID 
        | ID IZQCORCH EA DERCORCH
        | ID IZQCORCH EA DERCORCH IZQCORCH EA DERCORCH
    ''' 
    global variable
    variable = p[1]

     
    
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
            cuadr = hacerLista(p[2], str(operando1), str(operando2), temp)
            cuadruplos.append(cuadr)
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
            cuadr = hacerLista(p[2], str(operando1), str(operando2), temp)
            cuadruplos.append(cuadr)
            pila_operandos.append(temp)
    
def p_FA(p):
    '''
    FA : ID
       | CTE
       | IZQPAR EA DERPAR      
    '''    
    global pila_operandos
    if p[1] != '(' and p[1] != None:
        if p[1] in (item[0] for item in simbolos):
            pila_operandos.append(p[1])
        else:
            if isinstance(p[1], int) == True:
                pila_operandos.append(p[1])
            elif isinstance(p[1], float) == True:
                pila_operandos.append(p[1])
            else:
                sys.exit(str(p[1]) + ' no fue definido')
                
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
    if p[2] == 'or' or p[2] == 'and':
       if len(pila_operandos) >= 2:
            operando2 = pila_operandos.pop()
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            if operando2 == temp:
               avail.insert(0, operando2)
            temp = avail.pop(0)
            cuadr = hacerLista(p[2], str(operando1), str(operando2), temp)
            cuadruplos.append(cuadr)
            pila_operandos.append(temp)
   
             
def p_TL(p):
    '''        
    TL : TL NOT FL
       | FL AUX
    ''' 
    global temp
    if p[2] == 'not':
       if len(pila_operandos) >= 2:
            operando1 = pila_operandos.pop()
            if operando1 == temp: 
               avail.insert(0, operando1)
            temp = avail.pop(0)
            cuadr = hacerLista(p[2], str(operando1), temp)
            cuadruplos.append(cuadr)
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
            cuadr = hacerLista(p[2], str(operando1), str(operando2), temp)
            cuadruplos.append(cuadr)
            pila_operandos.append(temp)
        
            
def p_H(p):
    '''     
    H : ID
      | CTE
    '''  
    global pila_operandos
    if p[1] != '(' and p[1] != None:
        if p[1] in (item[0] for item in simbolos):
            pila_operandos.append(p[1])
        else:
            if isinstance(p[1], int) == True:
                pila_operandos.append(p[1])
            elif isinstance(p[1], float) == True:
                pila_operandos.append(p[1])
            else:
                sys.exit(str(p[1]) + ' no fue definido')
                
   

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
    tx = avail.pop(0) 
    id2 =  pila_operandos[-1]     
    cuadruplos.append(hacerLista('=', str(exp2+1), tf))  #le sume uno para cuando sea el ciclo, usar el "<" como menor (a es menor a 4 (va a iterar hasta 3))
    cuadruplos.append(hacerLista('<', id2, tf,tx)) 
    cuadruplos.append(hacerLista('gotoF', tx)) 
    avail.insert(0, tx)
    pila_saltos.append(cont-2)

def p_AUX11(p):        #Tercer auxiliar del ciclo for
    '''     
    AUX11 : 
    '''
    
    id3 = pila_operandos.pop()
    cuadruplos.append(hacerLista('+', id3, str(1), id3)) 
    retorno = pila_saltos.pop()
    cuadruplos.append(hacerLista('goto', str(retorno))) 
    rellenar(retorno+1, cont)
    avail.insert(0, tf)
    
#------------------------ Auxiliares del INPUT y OUPTUT -----------------------------
def p_AUX12(p):        # 1er Auxiliar del Output
    '''     
    AUX12 : 
    '''
    cuadruplos.append(hacerLista('output', varOutput))
    
def p_AUX13(p):        # 2ndo Auxiliar del Output
    '''     
    AUX13 : 
    '''    
    cuadruplos.append(hacerLista('output', variable))

def p_AUX14(p):        # Auxiliar del Input
    '''     
    AUX14 : 
    '''    
    if variable in (item[0] for item in simbolos):
        cuadruplos.append(hacerLista('input', variable))
    else:
        sys.exit(variable + ' no fue definido')   
    

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


def p_error(p):
    print("\tINCORRECTO")

#--------------- Se crea el parser -------------------------
parser = yacc.yacc()

#--------------- Pruebas con diferentes archivos ------------
try:
    #f = open("ejecutor1.txt", "r")
    f = open("prueba_for.txt", "r")
    #f = open("prueba_cuadruplos2.txt", "r")
    #f = open("prueba_variables.txt", "r")
    #f = open("matricesEntrega_A01244818.txt", "r")
    #f = open("arit_logic_ProgramaPrueba.txt", "r")
    contenido = f.read()
    parser.parse(contenido)


except EOFError:
    PASS
    
# =============================================================================
# x = recuperar('hj')
# print(x)
# =============================================================================

#------------- PRINTS -----------------------------------

# =============================================================================
# #---------------------------------------------------------------
# print('----------Tabla de simbolos-------')
# for sim in enumerate(simbolos):
#     print(*sim)
# 
# print('\n--------Código Intermedio ----------')
# for s in cuadruplos:
#     print(s)  #cuadruplos es una lista de listas. Con el * se itera en cada lista e imprime los valores de cada lista sin corchetes ni comas
#     #print(s)   #Formato de listas
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


