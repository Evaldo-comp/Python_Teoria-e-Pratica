# OBS: Cada trecho separado por # é uma solução para um enuciado diferente, para executá-los individualmente
# isole os trechos que for executar com cometários de múltiplas linhas


# 1 Escreva um exemplo da função do_twice em um script
def print_span():
    print("Hello world")

def do_twice(f):
    f()
    f()

do_twice(print_span)

#############################################################################################3
# 2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e chame 
# a função 2 vezes, passando o valor como argumento
 
def do_twice(f,n1, n2):
    f(n1, n2)
    f(n1, n2)

def soma(n1, n2):
    soma = n1 + n2
    print(soma)

def do_twice(soma, n1, n2):
    soma(n1, n2)
    soma(n1, n2)

do_twice(soma, 1, 2)

####################################################################
# 4. Use a versão alterada de do_twice para chamar print_twice  duas vezes, passando 'span' como argumento

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f,n1):
    f(n1)
    f(n1)
do_twice(print_twice, 'span')

#####################################################################
# 5. Defina uma função nova chamada do_four que receba um objeto de função
# e um valor e chame a função quatro vezes, passando o valor como um parâmentro.
# Deve haver só duas afirmações no corpo desta função, não quatro
def do_twice(f, valor):
    f(valor)
    f(valor)

def pares(n):
    print( n * 2)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)
    
  

do_four(pares, 2) 