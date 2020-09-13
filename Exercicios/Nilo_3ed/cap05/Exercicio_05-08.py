"""
Escreva um programa que leia dois números, imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores
de soma e subtração para calcular o resultado. Lembre-se de que podemos
entender a multiplicação de dois números como somas sucessivas de um deles.
assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

"""

# Solução
produto = 0
n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))

x = 1
while x <= n2:
    produto += n1  # n1 + n1 + n1 +n1 ...
    x += 1
print(f' {n1} x {n2}  =  {produto}')

