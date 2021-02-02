"""
Utilizando a função type, escreva uma função recursiva que imprima os elementos de uma lista
. Cada elemento deve ser impresso separadamente, um por linha. considere o caso de listas dentro 
de listas. A cada nível, imprima a lista mais à direita, como fazemos ao identar blocos
em python. 

Resolução: Evaldo 2020
"""

L = ["a", ["b", "c", "d"], "e"]


def typeList(L, n):

    for x in L:
        if x == L[0]:
            print(f"  {type(x)} ")
        elif x == L[1]:
            print(f"     {type(x)}")
        elif x == L[2]:
            print(f"       {type(x)}")


print(typeList(L, 1))
