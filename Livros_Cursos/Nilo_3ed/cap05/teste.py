"""
Escreva um programa que leia um número e verifique se é ou não um número primo.
Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois
por todos os números impares até o número lido. Se o resto de uma dessas divisões
for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2
é o único primo que é par.
"""

num = int(input("digite um número"))
pri = 0
while pri <= num:

    x = 3
    while (x < 100) :
        if 100 % x==0 :
            break
        x += 2
    if x==100 :
        print(f'{x} é primo')
        pri+=1
    else :
        print(f'{x} nao é primo, pois é divisivel por {x}')



