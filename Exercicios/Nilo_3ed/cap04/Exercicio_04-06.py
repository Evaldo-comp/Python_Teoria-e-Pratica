"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer
em km. Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até
200 km, e R$ 0.45 para viagens mais longas.
"""

# Solução

dis = int(input("Qual a distância que você pretende percorrer? "))
passagem = None

if dis <= 200:
    passagem = dis * 0.50
    print(f'Sua passagem será R$ {passagem} Reais')
else:
    passagem = dis * 0.45
    print(f'Sua passagem será R$ {passagem} Reais')