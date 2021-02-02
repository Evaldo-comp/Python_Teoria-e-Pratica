"""
Escreva um programa que leia dois números. imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender o quociente da divão de dois números como
quantidade de vezes que podemos retirar o divisor do dividendo.
logo, 20 /4 =5, uma vez que podemos subtrair 4 cinco vezes de 20.

"""

# Solução

n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
quociente = 0
sub = n1 - n2
while sub >= n2:

    sub -= n2

    quociente += 1

if sub == 0: # teste do resto
    print(f' {n1} / {n2}  =  {quociente +1} e resto 0')
else:
    print(f' {n1} / {n2}  =  {quociente + 1} e resto {sub}')
