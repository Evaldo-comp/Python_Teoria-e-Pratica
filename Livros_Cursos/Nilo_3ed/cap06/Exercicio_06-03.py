"""
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""

lista1 = [1, 2,3, 4,  5]
lista2 = [2, 4, 6, 8, 10]
lista3 = []

for i in lista1:
    if i not in lista3:
        lista3.append(i)
        for x in lista2:
            if x not in lista3:
                lista3.append(x)


print(lista3)




