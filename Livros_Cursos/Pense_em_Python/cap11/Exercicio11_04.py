""""
Aplique a função has_duplicated (Exercicio 10.7) em um dicionário
"""
from collections import Counter
d = {"1": "Edson", "2": "Ana", "3": "Pedro", "4": "José", "5": "José"}


def has_duplicates(d):

    duplicados = dict(Counter(k for k in d.values()))
    for i in duplicados.values():
        if i != 1:
            return True
            print(i)
        else:
            a = False
            print(i)
    return a


print(has_duplicates(d))
