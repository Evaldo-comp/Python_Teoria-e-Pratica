"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número
de meses a pagar.

"""

# Solução

valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
qtdanos = int(input("Em quantos anos voê pretende quitar a dívida?"))

limite = salario * (30/100)
valorPrestacao = valorCasa / (qtdanos * 12)

if valorPrestacao <= limite:
    print(f"Seu empréstimo foi aprovado. a prestação será de R${valorPrestacao:.2f} Reais")
else:
    print(f'Infelizmente seu empréstimo foi negado')

