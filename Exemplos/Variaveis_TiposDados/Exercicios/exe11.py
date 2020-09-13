"""
Crie uma função que receba um número inteiro e retorne a quantidade de algarismos deste número
"""

def qtd_digitos(num):
	return len(str(num))  # Método len() retorna o tamanho e o método str(), converte para string

print(qtd_digitos(1234))