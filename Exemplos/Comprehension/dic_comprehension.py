# Sintaxe: {chave: valor for valor in iterável}

# Exemplo

numeros = {'a': 1, 'b': 2, 'c': 3, 'c': 4, 'd': 5}

quadrado = {chave.upper(): valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# Gerando um dicionário a partir de uma lista
lst = [1, 2, 3, 4, 5]

triplo = {valor: valor *3 for valor in lst}
print(triplo)

# Combinando
chaves = "abcde"
valores = [1, 2, 3, 4, 5]

comb = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(comb)

# Utilizando condicionais

numeros = [1, 2 , 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
