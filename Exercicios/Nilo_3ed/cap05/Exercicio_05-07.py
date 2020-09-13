"""
Modifique o programa do exercício 5.6 de forma que o usuário também digite
o início e o fim da tabuada, em vez de começar  com 1 e terminar com 10

"""

# Solução


n = int(input(" Tabuda de : "))
x = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

while x <= fim:
    print(f'{n} x {x} = {n * x}')
    x += 1