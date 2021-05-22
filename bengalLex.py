import ply.lex as lex

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
    
    'EQUAL',
    'NOTEQUAL',
    'MAYOR',
    'MENOR'
        
] + list(reserved.values())

literals = "+-/\*()[]=,!;:^<>.|#" 

#Ignoramos los espacios, tabs y enters
t_ignore = r' '  
t_ignore_enter = r'\n'
t_ignore_tabs = r'\t'

#Ignora los comentarios (//)
t_ignore_COMMENT = r'\//.*'
 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_\d\[\]]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
 
def t_CTE(t):
        r'\d+\.*\d*'
        #r'\d+
        t.value = float(t.value)    
        return t 

# =============================================================================
# def t_CTE_FL(t):
#     r'\d+\.\d+'
#     t.value = float(t.value)
#     return t    
# =============================================================================
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
t_MAYOR = r'\>'
t_MENOR = r'\<'
 
 
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

