"""
Escreva uma função que receba como argumento uma lista de strings, e uma dessas strings.
Essa função deve retornar o indice da string que foi passada como argumento
"""
# Modo 1:
def indice(lst, txt):
	local = 0
	for i in lst:
		if i ==txt:
			return local
		local +=1

lst = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
print(indice(lst,"Terça"))

# Modo 2:
def indice(lst, str):
    return lst.index(str)

lst = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
print(indice(lst,"Quinta"))