"""
# Filtra uma lista de números e gera um novo arquivo com múltiplos de 4

Fonte: Nilo 3 ed
"""

with open("multiplos de quatro.txt", "w") as multiplos4:

    with open("pares.txt",) as pares:
        for i in pares.readlines():
            if int(i) % 4 == 0:
                multiplos4.write(i)
