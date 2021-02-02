"""
Altere o programa do Exercicio_05-11 de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês,
e você deve considerá-lo para o cálculo de juros do mês seguinte

"""

deposito = float(input("Digite o valor do depósito"))
taxa = float(input("digite a taxa de juros ao mês"))

periodo = 1
valorMensal = deposito
depositoMensal = float(input(f" Quanto deseja depósitar no inicio de cada Mês?"))
while periodo <= 24:
    valorMensal = valorMensal + (valorMensal * taxa/100)
    print(f'Mês: {periodo} Valor: R$ {valorMensal:5.2f} Reais')
    valorMensal += depositoMensal
    periodo += 1
print(f'O valor ganho com juros foi R$ {valorMensal - deposito:5.2f} Reais')