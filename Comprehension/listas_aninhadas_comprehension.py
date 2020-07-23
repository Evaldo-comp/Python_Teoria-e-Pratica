listas= [[1,2,3],[4,5,6],[7,8,9]] # Matriz 3 x 3
print(listas)
print(listas[0][2]) # imprime o primeiro terceiro item da lista 1

# Listas comprehension

[[print(valor) for valor in lista] for lista in listas]

#Gerando uma lista aninhada

lista_aninhada =[[numero for numero in range(1,10)] for valor in range(1,6)]
print(lista_aninhada)