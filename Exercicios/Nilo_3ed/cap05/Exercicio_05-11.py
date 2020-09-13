"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com
juros no período.

"""

deposito = float(input("Digite o valor do depósito"))
taxa = float(input("digite a taxa de juros ao mês"))

periodo = 1
valorMensal = deposito

while periodo <= 24:
    valorMensal = valorMensal + (valorMensal * taxa/100)
    print(f'Mês: {periodo} Valor: R$ {valorMensal:5.2f} Reais')
    periodo += 1
print(f'O valor ganho com juros foi R$ {valorMensal - deposito:5.2f} Reais')