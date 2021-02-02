"""
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
"""

T = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = T[0]
maior = T[0]
soma = 0
for e in T:
    if e > maior:
        maior = e
    elif e < menor:
        menor = e
    soma += e
print(f""" 
Maior: {maior}
Menor: {menor}
Média: {soma/len(T)}
""")
