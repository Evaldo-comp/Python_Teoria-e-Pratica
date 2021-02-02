"""
Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
* Os valores comuns às duas listas
* Os valores que só existem na primeira
* Os valores que existem apenas na segunda
* Uma lista com os elementos não repetidos das duas listas
* A primeira lista sem os elementos repetidos na segunda
"""

lista1 = [1, 1, 1, 3, 5, 8, 10, 12]
lista2 = [0, 1,  3, 3, 5, 10]

# Os valores comuns às duas listas
print (set(lista1).intersection(lista2))

# Os valores que só existem na primeira
print (set(lista1) - set(lista2))

# Os valores que existem apenas na segunda
print (set(lista2) - set(lista1))

# Uma lista com os elementos não repetidos das duas listas
nrepeat=[]
for i in lista1 and lista2:
    if (lista1.count(i) or lista2.count(i)) == 1:
        nrepeat.append(i)
print(nrepeat)

# A primeira lista sem os elementos repetidos na segunda
replista2 = []
for i in lista2:
    if lista2.count(i)>1:
        replista2.append(i)
print(set(lista1) - set(replista2))