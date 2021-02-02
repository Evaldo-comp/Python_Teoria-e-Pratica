'''Exercício03 - Escreva um programa que escolha uma determianda letra e indique quantas vezes ela occore no seu nome'''

nome = input('Digite seu nome completo')
l = input('Qual letra você quer verificar a repetição no seu nome?')
tupla = tuple(nome)
print(tupla.count(l))