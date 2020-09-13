"""
ADAPTADO:
Crie um pograma que calcule a média de uma aluno, utilizando uma lista de 7 notas

"""

notas = [0, 0, 0, 0, 0, 0, 0]
i = 0
soma =0
while i < 7:
    notas[i] = float(input(f'Digite a nota {i+1}\n'))
    soma+=notas[i]
    i+= 1
print(f'A média é {soma/i:.2f}')