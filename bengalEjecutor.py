from bengalYacc import (tabla_temporales, simbolos, cuadruplos, recuperar, guardar, printB) 


pc = 0 #Program Counter
pila_ejecucion = []

def regresar_var(x):  
    try:
        c_flt = float(x)
        nombre1 = c_flt
        return nombre1
        
    except ValueError:
        if x in (item[0] for item in simbolos):   #a
           nombre1 = x
        elif (x[-1:], int) == True:                 #array2
           nombre1 = x
        else:                                          #arrayi
           u_dim = x[-1:]
           nombre = x[:-1] 
                     
           u = recuperar(u_dim)
           nombre1 = nombre + u
           if '.' in nombre1:
              nombre1 = nombre1.split('.')[0]  
        return nombre1        


def regresar_var2(x):  
    try:
        c_flt = float(x)
        nombre1 = c_flt
        return nombre1
        
    except ValueError:
        if x in (item[0] for item in simbolos):   #a
           nombre1 = x
        elif (x[-2:], int) == True:                 #matriz23
           nombre1 = x
        else:                                          #matrizij
           u_dim = x[-1:]
           nombre = x[:-1] 
           p_dim = nombre[-1:]
           nombre = x[:-2] 
                     
           p = recuperar(p_dim)
           nombre1 = nombre + p 
           if '.' in nombre1:
              nombre1 = nombre1.split('.')[0]
           u = recuperar(u_dim) 
           nombre1 = nombre1 + u
           if '.' in nombre1:
              nombre1 = nombre1.split('.')[0]  
        return nombre1   

def regresar_var3(x):  
    try:
        c_flt = float(x)
        nombre1 = c_flt
        return nombre1
        
    except ValueError:
        if x in (item[0] for item in simbolos):   #a
           nombre1 = x
        elif (x[-3:], int) == True:                 #cubo123
           nombre1 = x
        else:                                          #cuboijk
           u_dim = x[-1:]
           nombre = x[:-1] 
           p_dim = nombre[-1:]
           nombre = x[:-2] 
           a_dim = nombre[-1:]
           nombre = x[:-3]
            
           a = recuperar(a_dim)
           nombre1 = nombre + a
           if '.' in nombre1:
              nombre1 = nombre1.split('.')[0]    
           p = recuperar(p_dim)
           nombre1 = nombre1 + p 
           if '.' in nombre1:
              nombre1 = nombre1.split('.')[0]
           u = recuperar(u_dim) 
           nombre1 = nombre1 + u
           if '.' in nombre1:
              nombre1 = nombre1.split('.')[0]  
        return nombre1  

while(True):

    c = cuadruplos[pc]
    opcode = c[0]
    
    if opcode == '=':          #Para variables normales
        v = recuperar(c[1])
        guardar(v,c[2])
        pc = pc + 1
         
    if opcode == 'checar':     #Para los Arrays
        x = recuperar(c[3])  
        nombre = c[2] + x
        if '.' in nombre:
            nombre = nombre.split('.')[0]
             
        #print(nombre)
        v = recuperar(c[1])
        guardar(v,nombre)
        pc = pc + 1
        
    if opcode == 'checar2':    #Para las matrices
        x = recuperar(c[3])
        y = recuperar(c[4])
        nombre = c[2] + x 
        if '.' in nombre:
            nombre = nombre.split('.')[0]
        nombre = nombre + y
        if '.' in nombre:
            nombre = nombre.split('.')[0]
            
        #print(nombre)
        v = recuperar(c[1])
        guardar(v,nombre)
        pc = pc + 1

    if opcode == 'checar3':    #Para los cubos
        x = recuperar(c[3])
        y = recuperar(c[4])
        z = recuperar(c[5])
        nombre = c[2] + x 
        if '.' in nombre:
            nombre = nombre.split('.')[0]
        nombre = nombre + y
        if '.' in nombre:
            nombre = nombre.split('.')[0]
        nombre = nombre + z
        if '.' in nombre:
            nombre = nombre.split('.')[0]            
        #print(nombre) 
        v = recuperar(c[1])
        guardar(v,nombre)
        pc = pc + 1
        
    if opcode == '+':
        
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
                   
        va = recuperar(nombre1)   
        vb = recuperar(nombre2) 
        resultado = float(va) + float(vb) 
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '-':

        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        resultado = float(va) - float(vb)  
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '*':

        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        resultado = float(va) * float(vb)  
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '/':
        
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        resultado = float(va) / float(vb)  
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == 'or':
        
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if va == 'False':
            va = False
        else:
            va = True
        
        if vb == 'True':
            vb = True
        else:
            vb = False
            
        if va or vb == True:
            resultado = True
        else:
            resultado = False
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == 'and':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if va == 'False':
            va = False
        else:
            va = True
        
        if vb == 'True':
            vb = True
        else:
            vb = False
            
        if va and vb == True:
            resultado = True
        else:
            resultado = False
        guardar(resultado,c[3])
        pc = pc + 1
    
    if opcode == 'not':
        nombre1 = c[1] 
        
        if(c[3] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
        if(c[3] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
        if(c[3] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if va == 'False':
            va = False
        else:
            va = True
        
        if vb == 'True':
            vb = True
        else:
            vb = False
            
        if va == True:
            resultado = False
        else:
            resultado = True
        guardar(resultado,c[2])
        pc = pc + 1
        
    if opcode == '<':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if (va < vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '>':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if (va > vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1

    if opcode == '=<':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if (va <= vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1

    if opcode == '=>':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if (va >= vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '==':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if (va == vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '!=':
        nombre1 = c[1] 
        nombre2 = c[2] 
        
        if(c[4] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
            nombre2 = regresar_var(c[2])
        if(c[4] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
            nombre2 = regresar_var2(c[2])
        if(c[4] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            nombre2 = regresar_var3(c[2])
            
        va = recuperar(nombre1)
        vb = recuperar(nombre2)
        
        if (va != vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == 'gotoF':
        va = recuperar(c[1])
        if va == 'False':
            pc = int(c[2]) 
        else:
            pc = pc + 1
            
    if opcode == 'goto':
        pc = int(c[1])
        
    if opcode == 'output': 
        nombre1 = c[1] 
        
        if(c[2] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
        if(c[2] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
        if(c[2] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
        printB(nombre1) 
        pc = pc + 1
        
    if opcode == 'input':
        entrada = input("Input: ")
        entrada = float(int(entrada)) 
        nombre1 = c[1]         
        if(c[2] == '1'):                    #Array
            nombre1 = regresar_var(c[1])
        if(c[2] == '2'):                    #Matriz 
            nombre1 = regresar_var2(c[1])
        if(c[2] == '3'):                    #Cubo
            nombre1 = regresar_var3(c[1])
            
        guardar(entrada,nombre1)
        pc = pc + 1
    
    if opcode == 'call':
        pila_ejecucion.append(pc + 1) 
        pc = int(c[1])
    
    if opcode == 'finProcedure':
        pc = int(pila_ejecucion.pop())

        
    if opcode == 'finPrograma':
        break
 
print('\n--------Código Intermedio ----------')
for s in cuadruplos:
    print(s)  #cuadruplos es una lista de listas. Con el * se itera en cada lista e imprime los valores de cada lista sin corchetes ni comas
    #print(s)   #Formato de listas
    
print('----------Tabla de simbolos-------')
for sim in enumerate(simbolos):
    print(*sim)


