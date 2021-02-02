"""
Escreva uma função que receba dois números e retorne  True se o
primeiro númeo for múltiplo do segundo

Resolução: Evaldo 2020
"""

def mul(a, b):
    if a % b == 0:
        return True
    return False
print(mul(10, 2))