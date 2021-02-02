"""
Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string
"""
string = input("Digite a String")
contador = {}

for i in string:
    contador[i] = contador.get(i, 0) +1
for chave, valor in contador.items():
    print(f"{chave}:{valor}x")

