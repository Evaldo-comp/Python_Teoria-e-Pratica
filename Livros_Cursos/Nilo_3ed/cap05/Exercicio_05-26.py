"""
Escreva um programa que calcule o resto da divisão inteira entre
dois números. Utilize apenas as operações de soma e subtração
para calcular o resultado

Resolução do autor: https://python.nilo.pro.br/exercicios3/capitulo%2005/exercicio-5-26.html
"""

num1= int(input("Insira o primeiro número"))
num2= int(input("Insira o segundo número"))
div = num1

while num1 >= num2:
    num1 -= num2
if num1 == 0:
    print(f"O resto de {div} por {num2} é 0")
else:
    print(f"O resto de {div} por {num2 } é {num1}")


