# TAGS &Bool

"""Dados booleanos podem ser represetados por 0 = False e 1 = true. Faça um progrmaa que retorne
# o opsoto
inverso_bool(True) ➞ 0

inverso_bool(False) ➞ 1

inverso_bool(1) ➞ 0

inverso_bool(0) ➞ 1
"""

def inverso_bool(status):
    if status == True or status == 1:
        return 0
    return 1

print(inverso_bool(False))