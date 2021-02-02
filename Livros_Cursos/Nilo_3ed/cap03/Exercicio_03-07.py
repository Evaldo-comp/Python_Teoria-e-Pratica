"""
Faça um programa que peça dois números inteiros.
Imprima a soma desses dois números na tela
"""

# Solução

# Solicita o primeiro número fazendo uma conversão de string para inteiro
numero1 = int(input("Digite o primeiro número\n"))
numero2 = int(input("Digite o segundo número\n"))
soma = numero1 + numero2
print(f'A soma de {numero1} + {numero2} = {soma}')

"""
OBS: as variáveis em Python são fracamente tipadas, ou seja
não é necessaŕio definir o tipo de dados nesse exemplo
"""