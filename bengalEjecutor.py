from bengalYacc import (tabla_temporales, simbolos, cuadruplos, recuperar, guardar, printB) 


pc = 0 #Program Counter

while(True):

    c = cuadruplos[pc]
    opcode = c[0]
    
    if opcode == '=':
        v = recuperar(c[1])
        guardar(v,c[2])
        pc = pc + 1
 
    if opcode == '+':
        va = recuperar(c[1])   
        vb = recuperar(c[2])
        #print(va)
       # print(vb)
        resultado = float(va) + float(vb) 
        #print(resultado)
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '-':
        va = recuperar(c[1])
        vb = recuperar(c[2])
        resultado = float(va) - float(vb)  
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '*':
        va = recuperar(c[1])
        vb = recuperar(c[2])
        resultado = float(va) * float(vb)  
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '/':
        va = recuperar(c[1])
        vb = recuperar(c[2])
        resultado = float(va) / float(vb)  
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == 'or':
        va = recuperar(c[1])
        vb = recuperar(c[2])
        if va or vb == True:
            resultado = True
        else:
            resultado = False
        guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == 'and':
        va = recuperar(c[1])
        vb = recuperar(c[2])
        if va and vb == True:
            resultado = True
        else:
            resultado = False
        guardar(resultado,c[3])
        pc = pc + 1
    
    if opcode == 'not':
        va = recuperar(c[1])
        if va == True:
            resultado = False
        else:
            resultado = True
        guardar(resultado,c[2])
        pc = pc + 1
        
    if opcode == '<':
        va = float(recuperar(c[1]))
        vb = float(recuperar(c[2]))
        if (va < vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '>':
        va = float(recuperar(c[1]))
        vb = float(recuperar(c[2]))
        if (va > vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '==':
        va = float(recuperar(c[1]))
        vb = float(recuperar(c[2]))
        if (va == vb) == True:
            resultado = True
            guardar(resultado,c[3])
        else:
            resultado = False
            guardar(resultado,c[3])
        pc = pc + 1
        
    if opcode == '!=':
        va = float(recuperar(c[1]))
        vb = float(recuperar(c[2]))
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
        printB(c[1])  
        pc = pc + 1
        
    if opcode == 'input':
        entrada = input()
        guardar(entrada,c[1])
        pc = pc + 1
        
    if opcode == 'finPrograma':
        break
 
print('\n--------Código Intermedio ----------')
for s in cuadruplos:
    print(s)  #cuadruplos es una lista de listas. Con el * se itera en cada lista e imprime los valores de cada lista sin corchetes ni comas
    #print(s)   #Formato de listas
    
print('----------Tabla de simbolos-------')
for sim in enumerate(simbolos):
    print(*sim)


