"""
Escreva um programa que verifica se um número é palíndromo.
Um número palíndromo é palíndromo se continua o mesmo caso seus
digitos sejam invertidos
"""
lst = list(input("Digite um numero"))
print(lst.reverse())
if lst == list(reversed(lst)):
    print(f'{lst} é palíndromo')
else:
    print(f'{lst} não é palíndromo')


