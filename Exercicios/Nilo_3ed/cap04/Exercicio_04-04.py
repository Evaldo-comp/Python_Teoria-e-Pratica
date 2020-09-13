"""
Escreva  um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00 Reais, calcule um aumento de 10%
Para os inferiores ou iguais , de 15%.

"""

# Solução

salario = float(input("Qual o seu salário? "))

aumento = None


if salario > 1250:
    aumento = salario * (10/100)
    print(f'você recebeu um aumento de R${aumento} '
          f'Reais e agora receberá u total de R$ {aumento + salario})')
if salario <= 1250:
    aumento = salario * (15/100)
    print(f'você recebeu um aumento de R${aumento} '
          f'Reais e agora receberá um total de R$ {aumento + salario})')

