"""
Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne True se  a lisata
estiver classificada e em ordem ascendente, e False se não for o caso.
"""

t = [1, 2, 3, 4, 5]


def is_sorted(w1, w2):
    if sorted(w1.upper()) == sorted(w2.upper()):
        return True
    return False


print(is_sorted("Celia", "alice"))
