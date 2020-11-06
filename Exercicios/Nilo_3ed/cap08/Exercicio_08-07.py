"""
Defina uam função recursiva que calcule o maior divisor comum(M.D.C) entre dois
números a e b, em que a > b.

"""


def mdc(a, b):
    if a <= b:
        return "O primerio número deve ser maior do que o segundo"
    else:
        return mdc(b, a - b(a/b))


print(mdc(9, 6))
