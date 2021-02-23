"""
Escreva uma função chamada in_bisec que receba uma lista ordenada, um valor alvo e devolva
o indice do valor na lista se ele estiver lá ou None se ele não estiver.
"""

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]


def in_bisec(t, n):
    a = len(t)//2
    t1 = t[:a]
    # print(t1)
    t2 = t[a:]
    # print(t2)
    if n in t1:
        return t.index(n)
    elif n in t2:
        return t.index(n)
    else:
        return None


print(in_bisec(t, 150))
