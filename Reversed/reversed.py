"""
reversed() Tem como função inverter um iterável
"""
# Exemplo01
'''lista = list(range(50))
res = reversed(lista)
print(lista)
print(res) # Ele não imprime, mas gera um objeto

print(list(res)) #o mesmo objeto anterior mas convertido em lista
'''
# Exemplo 02 - interando com reversed()

for letra  in reversed('Evaldo'):
    print(letra, end='')
print("\n")
# Realizando a mesma coisa sem o for
print(''.join(list(reversed('Evaldo'))))# Transforma o reversed em lista e o join(), transforma alista em string