# -*- coding: utf-8 -*-

"""
Escreva um programa que leia três números e que imprima o maior e o menor
"""

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

# inicialização das variáveis
maior = None
menor = None

# Definição do maior número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 >  n1 and n3 > n2:
    maior = n3

# Definição do menor número
if n1 < n2 and n1 < n3 :
    menor = n1
if n2 < n1 and n2 < n3 :
    menor = n2
if n3 < n1 and n3 < n2 :
    menor = n3
# Definição do menor número
print(f'O maior número é {maior} e o menor é {menor}')

"""
OBS: Há caminhos mais simples para a resolução desse probelma, mas eu optei 
por utilizar apenas artificios que foram apresetnados no livro até o 
momento do exercício
"""

# Utilizando max()
print(f' o maior número é {max(n1, n2, n3)} e o menor é {min(n1, n2, n3)}')