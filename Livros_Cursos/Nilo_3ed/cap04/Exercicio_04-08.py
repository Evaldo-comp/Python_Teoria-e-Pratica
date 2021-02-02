"""
Escreva um programa que leia dois números e que pergunte qual operação
você deseja realizar. Você deve poder  calcular soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

"""
n1 = int(input("Insira o primeiro número: \n"))
n2 = int(input("Insira o segundo número: \n"))

print("Qual operação você deseja realizar?")
oper = int(input('''
Digite 1 - Para Soma
Digite 2 - Para Subtração
Digite 3 - Para Multiplicação
Digite 4 - Para Divisão
'''))
print("\n")

if oper == 1:
    print(f'{n1} + {n2} = {n1 + n2}')
elif oper == 2:
    print(f'{n1} - {n2} = {n1 - n2}')
elif oper == 3:
    print(f'{n1} x {n2} = {n1 * n2}')
else:
    print(f'{n1} / {n2} = {n1 / n2}')
