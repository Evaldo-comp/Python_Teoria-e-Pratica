# OBS: Este Exeercicio deve solucionado utilizando apenas fundamentos aprendidos até agora no livro

# 1. Escreva um função que desenhe uma grade como a seguinte
'''
 + - - - - + - - - - +
 |         |         |
 |         |         |
 |         |         |
 |         |         |
 |         |         |
 + - - - - + - - - - +
 |         |         |
 |         |         |
 |         |         |
 |         |         |
 |         |         |
 + - - - - + - - - - +
 
'''

# Resolução 1
def faca_duas(f):
    f()
    f()

def faca_quatro(f):
    faca_duas(f)
    faca_duas(f)

def print_horizontal():
    print("+ - - - -", end=" ")

def print_vertical():
    print("|        ", end=" ")

def print_horizontais():
    faca_duas(print_horizontal)
    print("+")

def print_verticais():
    faca_duas(print_vertical)
    print("|")

def print_linha():
    print_horizontais()
    faca_quatro(print_verticais)

def print_grade():
    faca_duas(print_linha)
    print_horizontais()

print_grade()


'''
# Resolução 2
def horizontal():
    print("|         |         |")
def quatro(f):
    f()
    f()
    f()
    f()

def grade(quatro):
    print(("+" + " -"*4+" +"+" -"*4+" +"))
    quatro(horizontal)
    print(("+" + " -"*4+" +"+" -"*4+" +"))
    quatro(horizontal)
    print(("+" + " -"*4+" +"+" -"*4+" +"))


grade(quatro)

###########################################################################################
# 2. Escreva um função que desenhe uma grade semelhante com quatro linhas e quatro colunas
def horizontal():
    print("|         |         |         |")
def quatro(f):
    f()
    f()
    f()
    f()

def grade(quatro):
    print(("+" + " -"*4+" +"+" -"*4+" +"+" -"*4+" +"))
    quatro(horizontal)
    print(("+" + " -"*4+" +"+" -"*4+" +"+" -"*4+" +"))
    quatro(horizontal)
    print(("+" + " -"*4+" +"+" -"*4+" +"+" -"*4+" +"))
    quatro(horizontal)
    print(("+" + " -"*4+" +"+" -"*4+" +"+" -"*4+" +"))


grade(quatro)
'''