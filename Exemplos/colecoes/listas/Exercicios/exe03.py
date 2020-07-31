# Prática: Crie uma função que receba duas listas e compare, retornando True
# se forem iguais ou False se forem diferentes


def check_equals(lst1, lst2):
	if lst1 == lst2:
		return True
	else:
		return False
lista1 = [1,3,3]
lista2 = [1,2,3]

print(check_equals(lista1, lista2))