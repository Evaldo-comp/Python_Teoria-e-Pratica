"""
Escreva uma função chamada cunsum que receba uma lista de listas de números inteiros
e retorne a soma cumulativa;
"""

t = [1, 2, 3, 4]

m = []


def cumsum(t):
    a = 0

    for i in t:
        a += i
        m.append(a)
        # print(a)
    return m


print(cumsum(t))
