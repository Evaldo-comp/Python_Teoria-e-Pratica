"""
Escreva uma função chamada middle que receba uma lista de números e retorne uma nova
lista com todos os elementos originais exceto os primeiros e os últimos. 
"""

t = [1, 2, 3, 4, 5]

m = []


def midle(t):
    for i in t:
        if i != t[0] and i != len(t):
            m.append(i)
        # print(a)
    return m


print(midle(t))
