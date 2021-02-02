"""
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

"""

# Solução
qtdCigarro = int(input("Quantos cigarros você fuma por dia?"))
qtdAnos = int(input("Quantos anos faz que você fuma?"))

qtdDias = qtdAnos * 365
tempoPerdido = int(((qtdCigarro * qtdDias) * 10) /1440) # 1.440 é a quantidade de minutos por dia

print(f'Você perdeu {tempoPerdido} dias da sua vida')
