"""

# Definindo um conjunto
# Forma - 1
con = set({1,2,3,4,5,5, 6,7,8,9}) # Não imprime o item repetido
print(con)

# Forma 2 -
s = {1,2,3,4,5}
print(s)

# Convertendo uma string em um conjunto
nome = set('Evaldo')
print(nome) #  Imprime de forma desordenada

# Verificar a ocrencia de algum elemento do conjunto
if 1 in s:
    print('Esta presente')
else:
    print('Não tem')

# Conjuntos nao repetem valores
lista = [1,2,3,4,5,5,3]
print(f' Lista: {lista} com {len(lista)} elementos')

tupla = 1,2,3,4,5,5,3
print(f' Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([1,2,3,4,5,5,3], 'valor')  # Dicionarios não repetem chaves
print(f' Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = {1,2,3,4,5,5,3} # Conjuntos não repetem intens
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Adicionando elemento em um conjunto
con2 = {1,2,3,4}
con2.add(5)
print(con2)

# Removendo itens de um conjunto
# Forma 1
con2.remove(5)
print(con2)

# Forma 2
con2.discard(4)
print(con2)


# Copiando um conjunto para outro
con3 = {1,2,3,4,5}
con4 = {5,6,7,8,9}

# Forma 1 - Deep Copy
novo = con3.copy()
print(novo)
novo.add(6)
print(novo)
print(con3)

# Forma 2 - Shallow Copy
novo1 = con4
novo1.add(10)
print(novo1)
print(con4)

# Removendo todos os itens de um conjunto
novo1.clear()
print(novo1)
"""

# Métodos Matemáticos de conjuntos
NL ={'Pedro', 'José', 'Maria', 'Roberta'}
IC = {'Ana', 'André', 'Patrícia', 'Roberta', 'José'}

# Gerando um conjunto com nomes de estudantes únicos
# Forma 1
unicos1 = NL.union(IC)
print(unicos1)

# Forma 2
unicos2 = NL | IC
print(unicos2)

# Gerando um conjunto de elementos presentes em ambos os conjuntos
# Forma 1
ambos1 = NL.intersection(IC)
print(ambos1)

# Forma 2
ambos2 = NL & IC
print(ambos2)

# Gerando um conjunto de elementos que estão em um conjunto mas não estão no outro , ou seja a diferença
soNL = NL.difference(IC)
print(soNL)

soIC = IC.difference(NL)
print(soIC)

