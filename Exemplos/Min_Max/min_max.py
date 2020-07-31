"""
max() retorna o maior valor de iterável ou maior de dois elementos ou mais elementos
min() retorna o maior valor de iterável ou maior de dois elementos ou mais elementos

"""

# Exemplo01

lista = []
lista = list(range(100))
print(f'{max(lista)} é o maior número e {min(lista)} é o menor')

#Exemplo02 - dicionários
# no caso de dicionários ele por padrão retorna o máximo da chave

dic = {"a": 1, "b": 65, "c": 45, "d": 23, "e": 5, "f": 13 }
print(max(dic)) # por padrão retorna a maior chave

print(max(dic.values())) # para retornar o maior valor tem especificar .values()

# Exemplo 03 - Retonando o maior de 3 valores
'''
v1 = int(input("Digite um número: "))
v2 = int(input("Digite um número: "))
v3 = int(input("Digite um número: "))

print(f' O maior valor dos três é {max(v1, v2, v3)} e o menor é {min(v1, v2, v3)}')
'''

# Ordenação de nomes
lista_nomes = ['Edson', 'Ana', 'Zezinho', 'George', "Albuquerque"]
print(max(lista_nomes)) # retorna o máximo com base na ordem alfabética

print(max(lista_nomes, key = lambda nome: len(nome)))# retorna o máximo com base no tamanho