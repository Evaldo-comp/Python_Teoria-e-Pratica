"""
Diferente do sort() utilizado nas listas, o sorted é utilizável em qualquer iterável
mas em tese eles possuem a mesma função, ordenar elementos

sort() x sorted(): O sort() modifica alista existente, já o sorted() gera uma nova lista

OBS 1 : idependentemente do iterável que você utilizar, o sorted() sempre vai retornar uma lista
OBS 2 : Caso queira outro objeto a partir do sorted(), como por exemplo uma tupla,
basta converter a saída - tuple(sorted(lista))

link útil: https://docs.python.org/pt-br/dev/howto/sorting.html
"""
#Exemplo de sort()
lst1 = [1, 4, 2, 8, 12, 34, 56]
print(lst1.sort())

# Exemplo de sorted() em uma tupla
tuple = (1, 4, 2, 8, 12, 34, 56)
print(sorted(tuple))

# Exemplo de sorted() em uma lista
lst1 = [1, 4, 2, 8, 12, 34, 56]
print(sorted(lst1))

# É possível adicionar parâmetros para manipular a ordenação

print(sorted(tuple, reverse = True))     # Ordena na decrescente

""" É possível importar o módulo operator para utilizar duas funções que facilitarão 
muito a ordenação a importação da modulo de da da seguinte forma:
from operator import itemgetter, attrgetter
"""

