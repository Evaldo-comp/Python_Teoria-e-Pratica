"""
Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor
seja o número desse caractere encontrado em uma frase lida
"""
oco = 0
frase = input("Digite a frase ")
dict = {}

for i in frase:
    if i in dict:
        dict[i]= dict[i]+1
    else:
        dict[i] = 1
print(dict)