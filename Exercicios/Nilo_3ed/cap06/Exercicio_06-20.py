"""
Escreva um programa que compare duas listas. Considere a primeira
lista como a versão inicial e a segunda como a versão após alterações.
Utilizando operações com conuntos, seu programa deverá imprimir a lista
de modificações entre essas duas versões, listando:
* Os elementos que não mudarão
* Os novos elementos
* Os elementos que foram removidos
"""
lista1 = [2, 4, 6, 8, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Lista inicial sem modificaçãoes: {lista1}')
print(f'Elementos que não mudarão: {set(lista1).intersection(lista2)}')
print(f'Novos elementos: {set(lista2)-set(lista1)}')
print(f'Elementos que não forão removidos: {set(lista1)-set(lista2)}')
