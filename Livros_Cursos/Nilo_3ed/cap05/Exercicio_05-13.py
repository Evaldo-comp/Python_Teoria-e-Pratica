"""
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago. Imprima o número  de meses para que
a dívida seja paga, o total pago e o total de juros pago.

"""
divida = float(input("Qual o valor da dívida?"))
juroMensal = float(input("Qual a taxa de juros mensais?"))
pgtMensal = float(input("Qual o valor que será pago mensalmente? "))
dividaTotal = divida
valorFinal = 0
meses =1
while valorFinal <= dividaTotal:
    dividaTotal +=  dividaTotal * (juroMensal/100)

    meses +=1

    valorFinal += dividaTotal -  pgtMensal
    dividaTotal-=pgtMensal

print(f'''A dívida será paga em {meses} Meses
Total pago: R$ {valorFinal:.2f}Reais
Total de juros: {valorFinal - divida:.2f}''')
