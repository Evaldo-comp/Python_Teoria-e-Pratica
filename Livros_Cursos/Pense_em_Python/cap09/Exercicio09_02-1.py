# Escreva uma função que receba um palavra e retorne True se ela não possuir a letra 'e'
# e False se ela tiver


def has_no_e(word):
    cont = 0
    for i in word:
        if i.lower() == "e":
            cont = +1
            return False
        elif cont == 0:
            return True


print(has_no_e("avaldo"))
