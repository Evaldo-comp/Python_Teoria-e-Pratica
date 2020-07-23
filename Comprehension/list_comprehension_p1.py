"""
Essas funcionalidade do Python permite que possamos gerar uma lista de dados a partir de outrso
dados iteráveis.
Estrutura: [dado for dado iterável]
"""

#Exemplo:
numeros= [1,2,3,4,5]

res=[numero * 10 for numero in numeros]
print(res)

par = [numero%2==0 for numero in numeros]
print(par)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

# Utilizando funções

def quadrado(valor):
    return valor ** 2

qua = [quadrado(numero) for numero in numeros]
print(qua)

# Utilizando Loops sem comprehension
triplo = []

for numero in numeros:
    num_tri = numero * 3
    triplo.append(num_tri)
print(triplo)

# Utilizando range

print([numero * 4 for numero in range(1, 40)])

# Convertendo numero em string

print([str(numero) for numero in [1,2,3,4,5,6,7,8]])

# O inverso

print([int(numero) for numero in ['1', '2', '3']])