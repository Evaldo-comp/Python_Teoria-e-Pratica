"""
Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número. O programa
termina se o usuário acertar ou errar três vezes.
"""

import random
n = random.randint(1, 5)
cont = 0
cont2 = 0
control = 1
a = 1
while (a != 0):
    print("Escolha  um numero:")
    control = 1
    while control <= 3:
        x = int(input())
        if x == n:
            print("Você acertou!")
            cont += 1
            control += 1
            if cont == 3:
                a = 0
        else:
            print("Você Errou.")
            cont2 += 1
            control += 1
            if cont2 == 3:
                a = 0
        # if cont2 == 3 or cont == 3:
         #   break
