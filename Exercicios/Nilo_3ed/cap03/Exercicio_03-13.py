"""
Escreva um programa que converta uma temperatura digitada em Celsius em Fahrenheit
A fórmula para conersão: F = (9 x C )/ 5) + 32

"""
# Solução

temp = float(input("Digite a temperatura em Celsius"))
conv = ((9 * temp) / 5 ) + 32

print(f'{temp} Cº é igual a {conv} Fº')