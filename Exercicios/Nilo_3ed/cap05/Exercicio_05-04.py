"""
ADAPTADO: Escreva um programa que imprima de 1 até o número inserido pelo usuário, mas
apenas os ímpares

"""

# Solução

fim = int(input('Digite o número que irá finalizar a sequẽncia: '))

x = 1
while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1
