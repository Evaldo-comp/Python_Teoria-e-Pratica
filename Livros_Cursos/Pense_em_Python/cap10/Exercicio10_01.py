"""
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros
e adicione os elementos de todas as listas aninhadas.
"""

t = [[1, 2, 3], [2], [4, 5, 6]]


def nested_sum(t):
    a = 0

    for i in t:
        a += sum(i)
        # print(a)
    return a


print(nested_sum(t))
