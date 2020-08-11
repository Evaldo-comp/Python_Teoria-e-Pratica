"""
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
e R$ 0,15 por km rodado.

"""

# Solução

km = float(input("Quantos quilômetros foram percorridos?"))
dias = int(input("Por quantos dias vocẽ alugou o veículo?"))

total = (dias * 60) + (km * 0.15)

print(f'O valor final a pagar é : R${total} Reais')