"""
Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa
em lista, vistos no cap07

Resolução: Evaldo 2020
"""

def pesquise(lista, valor):
   if valor in lista:
       return lista.index(valor)


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

