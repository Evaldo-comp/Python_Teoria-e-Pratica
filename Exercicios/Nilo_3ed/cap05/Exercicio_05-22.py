"""
Escreva um programa que exiba uma lista de opções(menu):
adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.
"""

while True:


    print("Escolha a opção equivalente a operação desejada")
    opcao = int(input('''
    ADIÇÃO = 1
    SUBTRAÇÃO = 2
    DIVISÃO = 3
    MULTIPLICAÇÃO = 4
    SAÍDA = 5 
    '''))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        num = int(input("Qual tabuada deseja resolver?" ))
        tabuada = 1
        while tabuada <=10:
            if opcao == 1:
                print(f'{num} + {tabuada} = {num + tabuada}')
            elif opcao == 2:
                print(f'{num} - {tabuada} = {num - tabuada}')
            elif opcao == 3:
                print(f'{num} / {tabuada} = {num / tabuada}')
            elif opcao == 4:
                print(f'{num} * {tabuada} = {num * tabuada}')
            tabuada +=1
    else:
        print("a opção digitada não é válida")


