"""Prática: Imagine que é seu aniversário, mas você quer ter certeza de que o bolo irá dar para
todos os convidades. Faça uma função que faça essa verificaçaõ recebendo 3 argumentos:
Número de pedaços, Número de convidados e Número de pedaços que cada pessoa come.
"""
def bolo(total, pessoas, pedaco_pessoa):
	if pessoas * pedaco_pessoa <= total:
		return True
	return False

print(bolo(12,4,4))