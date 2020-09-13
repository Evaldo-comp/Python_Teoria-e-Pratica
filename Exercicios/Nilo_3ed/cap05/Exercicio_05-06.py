"""
ADAPTADO: Utilizando while imprima os resultados da tabuada de 2:
A saída deve ser semelhante a: 2 x 1 = 2, 2 x 2 =4 ...

"""

# Solução

n = int(input(" Tabuda de : "))
x = 1
while x <= 10:
    print(f'{n} x {x} = {n * x}')
    x += 1
