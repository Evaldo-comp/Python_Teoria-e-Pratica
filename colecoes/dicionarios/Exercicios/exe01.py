"""
Alguns dos métodos utilizados em strings também podem ser normalmente utilizados
em estruturas como listas, tuplas e dicionários, um desses métodos é o len(), que serve para retornar
o tamanho do que for dentro do parênteses.
"""

def vazio(dic):
	if len(dic) == 0:
		return True
	return False

dic = {'a' : '1'}
print(vazio(dic))