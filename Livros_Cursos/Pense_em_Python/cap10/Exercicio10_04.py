"""
Escreva uma função chamada chop que tome uma lista alterando-1 para remover o primeiro e o último 
elementos e retorne None. 
"""

t = [1, 2, 3, 4, 5]


def chop(t):
    return t[1:-1]


print(chop(t))
