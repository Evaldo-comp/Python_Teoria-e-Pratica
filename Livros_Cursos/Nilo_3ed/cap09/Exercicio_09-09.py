"""
    Escreva um programa que receba uma lsita de nomes de um arquivo e os imprima 
    um por um
"""

with open("listaNomes.txt") as nomes:
    for i in nomes.readlines():
        if i[0] != "*":
            print(i)
        else:
            break
