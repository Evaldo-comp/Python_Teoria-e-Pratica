# As tuplas são representadas por  parênteses, mas podem ser inscritas no código sem eles

tupla1 = (1, 3, 4, 5,)  # correto
tupla2 = 1, 3, 4, 5,  # correto

# Tupla de apenas um elemento
print('#############################################################################')
print("Tupla com apenas 1 elemento tem que vir com uma vírgula no final")
tupla3 = (3,)  # Tuplas são definidas pela vírgula
print(tupla3)

# Gerando uma tupla com range()
print('#############################################################################')
print("Tupla gerada a aprtir de um range(20)")
tupla4 = tuple(range(20))
print(tupla4)

# Desempacotamento de uma Tupla
print('#############################################################################')
print("Realizando o desenpacotamento de uma tupla")

tupla5 = (22, 1.75, "Anderson")
idade, altura, nome = tupla5  # Desempacotamento
print(idade)
print(altura)
print(nome)

# OBS: Devido ao fato das tuplas serem imutáveis, não existem métodos para adição e remoção de elementos

# Soma, Valor Máximo, Valor Mínimo, Tamanho (Apenas números inteiros ou reais)
print('#############################################################################')
print("Soma, Valor Máximo, Valor Mínimo, Tamanho (Apenas números inteiros ou reais")
tupla6 = (1, 2, 3, 4, 5)
print(sum(tupla6))
print(f'A soma da tupla é {sum(tupla6)}')
print(f'O valor Máximo da tupla é {max(tupla6)}')
print(f'O valor Mínimo  da tupla é {min(tupla6)}')
print(f'O tamanho da tupla é {len(tupla6)}')

# Cocatençaõ de tuplas
print('#############################################################################')
print("Cocatenação de Tuplas")
tupla7 = (1, 2, 3)
tupla8 = (4, 5, 6)
print(tupla7 + tupla8)

# Verificar a ocorrência de determinado elemento em uma tupla
print('#############################################################################')
print("Verificar a ocorrência de determinado elemento em uma tupla")
tupla9= (12, 23, 34, 23, 23,)
print(23 in tupla9)

#Iterando sobre uma tupla
print('#############################################################################')
print("Iterando sobre uma tupla")
tupla10 = range(20)
for i in tupla10:
    print(i, end=" ")

for indice, valor in enumerate(tupla10):
    print(indice, valor)

#Contar elementos em uma tupla
print('#############################################################################')
print("Contar elementos em uma tupla")

tupla11= ('a', 'e', 'i', 'o','u','e','a')
print(tupla11.count('a'))


#Copy de tupla
print('#############################################################################')
print("Copiar uma tupla para outra")
tupla12 = (1, 2, 3)
tupla13 = tupla12 # Copia realizada
print(tupla13)
