"""
* Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
"""
with open("pares.txt", "r") as pares, open("pares_inverse.txt", "w") as pares_inverse:
    L = pares.readlines()
    L.reverse()

    for l in L:
        pares_inverse.write(l)
