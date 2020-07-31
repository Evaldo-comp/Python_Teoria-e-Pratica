"""
Podemos contar quantas vezesdeterminado caractere se repete dentro de uma string, ou seja
a sua incidência, parqa isso utilizanos o metodo txt.count()
"""

#Prática: Existem muitas formas de demonstrar uma risada ou gargalhada na internet
# podendo ser "HAHAHAHA", ou "KKKKKKKKKK", ou até mesmo "jkashdaksdhas". crie uma função
# que conte quantas garglhadas foram dadas sendo que cada"Ha" é uma gargalhada.

def gargalhadas(txt):
	return txt.count('H')

ha = input("Insisra sua gargalhada")
print(gargalhadas(ha))