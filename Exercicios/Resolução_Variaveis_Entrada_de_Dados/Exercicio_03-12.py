"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média  esperada para a viagem

"""
# Solução

dist = float(input("Qual a distância em Km pretende percorrer?"))
VM = float(input("Qual a velocidade média que pretende percorrer? "))

tempo = dist / VM

print(f'Você levará {tempo} horas para finalizar o trajeto')
