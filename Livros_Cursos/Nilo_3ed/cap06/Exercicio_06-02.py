"""
Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras
"""
from random import randint
lista1 = []
lista2 = []
lista3 = []

# Laço for para preencher de forma automática as duas listas
for i in range(10):
    lista1.append(randint(i, 10))
    lista2.append(randint(i, 10))

print(lista1)
print(lista2)
lista3.extend(lista1) # Adiciona a lista 1 a lista 3
lista3.extend(lista2) # por fim adiciona a lista 2 a lista 3
print(lista3)