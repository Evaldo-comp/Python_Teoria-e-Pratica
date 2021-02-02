"""
Escreva um programa que leia a quantidade de dias, horas, minutos e
segundos do usuário. Calcule o total em segundos

"""

#Solução

dia = int(input("Entre com a quantidade de dias"))
hora = int(input("Entre com a quantidade de horas"))
minuto = int(input("Entre com a quantidade de minutos"))
segundo = int(input("Entre com a quantidade de segundos"))

totalSegundo = ((((((dia * 24) + hora)*60) + minuto)*60))

print(f'O total em segundos é: {totalSegundo}')