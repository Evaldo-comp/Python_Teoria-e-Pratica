"""
Escreva um programa que leia um número e verifique se é ou não um número primo.
Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois
por todos os números impares até o número lido. Se o resto de uma dessas divisões
for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2
é o único primo que é par.
"""

num = int(input("digite um número"))

if num < 0:
    print("Inisra apenas números positivos")
if num == 0 or num == 1:
    print("Casos especiais")
else:
    if num == 2:
        print("Dois é primo")
    elif num % 2 == 0:
        print(f'{num} não é primo')
    else:

        x = 3
        while (x < num):
            if num % x ==0:
                break
            x += 2
        if x == num:
            print(f'{num} é primo')
        else:
            print(f'{num} nao é primo, pois é divisivel por {x}')



