"""
* Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira
* e imprima a posição de início.
"""
string1 = input("Digite um texto")
string2 = input("Digite um texto")

# OBS: para deixar o código menos suceptível a erros, pode-se utilizar
# .upper() ou .lower()

if string2 in string1:
    print(f'{string2} foi encontrada na Posição: {string1.find(string2)} de {string1}')
else:
    print("O segundo texto não ocorre dentro do primeiro")