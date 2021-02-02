"""
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário

"""

# Solução

salario = float(input("Digite o valor do seu salário"))
aumento = float(input("Entre com a porcentagem de aumento"))

salarioAtual = salario + (salario * aumento/100)

print(f'O salário antigo é R${salario} Reais, após aumentar {aumento}% '
      f'seu salário fica R${salarioAtual} Reais')
