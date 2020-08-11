"""
Calcule o resultado da expressão A > B and C or D, utilizando os valores da tebela aseguir:
A   B   C        D
1   2   True   False
10  3   False  False
5   1   True   True
"""
res1 = 1 > 2 and True or False
res2 = 10 > 2 and False or False
res3 = 5 > 1 and True or True

print(f'O resultado da linha 1 da tabela é {res1}' )
print(f'O resultado da linha 2 da tabela é {res2} ')
print(f'O resultado da linha 3 da tabela é {res3}' )

#Fonte: Introdução à Programação com Python - Nilo Ney Coutinho- 3º ed

