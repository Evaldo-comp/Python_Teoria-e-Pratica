"""
Escreva uma função que retorne o maior de dois números

Resolução: Evaldo 2020
"""
def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Números iguais, por favor insira números diferentes"
print(max(3, 1))