'''Exercício02 - Escreva um programa que receba do usuário o tamanho de uma tupla e seus respectivos itens'''

r = int(input('qual o tamanho da sua tupla+'))
tupla = range(r)
tuplex = ()

for i in tupla:
    a = int(input('Digite um item para a sua tupla\n'))
    tuplex = tuplex + (a,)
print(tuplex)
