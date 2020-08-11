"""
Escreva um programa que leia um valor em metros e o exiba
convertido em milímetros

"""

#Solução

metros = float(input("Digite a quantidade de metros que deseja converter\n"))
metroConv = float(metros * 1000) # Conversão

print(f'{metros} metros é equivalente a {metroConv} milimetros')

#OBS: a entrada de pontos flutuantes deve ser feita com ( . ) e não com vírgula