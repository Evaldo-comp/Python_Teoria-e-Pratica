"""
Altere o Programa 6.11 d eforma a imprimir o menor elemento da lista
"""


L = [3, 7, 2, 4]
menor = L[0]
for e in L:
    if e < menor:
        menor = e
print(menor)