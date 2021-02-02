lista1 = [1, 3, 4, 3, 2, 4, 2]
lista2 = ['1', 'e', 'r']
lista3 = []
lista4 = list(range(11))
lista5 = list('Evaldo')

# Checando a existência de algum item em uma lista

if 'a' in lista2:
    print(True)
print(False)

# Ordenação de uma lista---sort()
lista1.sort()
print(lista1)

# Contagem de ocorrências de um determinado item dentro de uma lista --count()
print(lista1.count(2))

# adicionando itens em uma lista --append()
print(lista2)
lista2.append('adicionado')
print(lista2)

# Adicionando uma lista dentro de outra lista  --append()
lista2.append(['a', 'b', 'c'])  # Adicionando em forma de sub-lista
print(lista2)

# Adicionando uma lista dentro de outra lista de forma separada --extend()
lista2.extend(['d', 'f', 'g'])  # Itens adicionandos de forma separada
print(lista2)
# Obs: extend não aceita item único apenas iteráveis

# Inserindo item na lista em uma posição pré-determinada -- insert()
lista2.insert(1, '2')  # O primeiro parâmetro é o índice onde será armazenado o valor do parâmetro 2
print(lista2)

# Juntando listas (+)
lista6 = lista1 + lista2
print(lista6)

# Juntando listas --extend()
# lista1.extend(lista2)
# print(lista1)

# Invertendo a ordem de intens de uma lista --reverse()
lista2.reverse()
print(lista2)



# Ivertendo intens de uma lista com slicing -- [::-1]
print(lista2[::-1])

# Copiando uma lista --copy()
lista7 = lista1.copy()
print(lista7)

# Verificando tamanho de uma lista --len()
print(len(lista7))

# Removendo o último elemento de uma lista --pop()
print(lista7)
lista7.pop()
print(lista7)
# O pop() remove o último elemento e retorna o mesmo

# Removendo um item pelo índice --pop(i)
lista7.pop(3)
print(lista7)

# Remover todos os elementos de uma lista --clear()
print(lista7)
lista7.clear()
print(lista7)

# Convertendo uma string em lista  -split()
nome = 'Francisco Evaldo Pereira '
nome = nome.split() # Separa os itens da lista em cada espaço
print(nome)

# Escolhendo o separador do split(0)
nome2 = 'Evaldo pereira mariano'
nome2 = nome2.split('a') # Vai cortar a string nos 'a's
print(nome2)

# Convertendo uma lista em string --join()
lista8 = ['1', '2', '3', '4', '5']
print(lista8)
num = ' '.join(lista8) # Coloca um espaço entre cada elemento e tranforma em uma string
print(num)

# Interando sobre listas com for
for elemento in lista1:
    print(elemento)

# Interando sobre listas com While
'''lista =[]
item = ' '
while item != 'sair':
    print("Adicione um item a lista ou digite 'sair'")
    item = input()
    if item != 'sair':
        lista.append(item)

for item in lista:
    print(item)
 '''
# Gerar índice em um for
cores = ['Azul', 'Amarelo', 'Verde', 'Vermelho']
for indice, cor in enumerate(cores):
    print(indice, cor)

# Encontrar o índice de determinado valor --index()
lista9 = [1, 2 ,3 ,4 ,5,6 ,7 ]
print(lista9.index(3))

# Fazendo a busca de índice a partir um determinado valor de inicio, ou seja, range
print(lista9.index(3, 2)) # Busca o índice do ítem 5 a partir do índice 2

# Fazendo a busca de índice a partir de um determinado valor de início e fim, ou seja, range
print(lista9.index(3, 2, 4)) # Busca o índice do ítem 5 a partir do índice 2 até o índice 4


# Imprimindo íntens da lista utilizando slice

lista10 =[1, 2, 3, 4, 5, 6, 7, 8, 9, ]

print(lista10[1:])    # Imprime do índice 1 até o final
print(lista10[::])    # Imprime todos os elementos
print(lista10[-1:])   # Imprime apenas o último elemento
print(lista10[:4])    # Imprime do índice 0 ao índice 4
print(lista10[2 :4])  # Imprime do índice 2 ao índice 4
print(lista10[1::2])  # Imprime todos os elementos do índice 1 de dois em dois
print(lista10[::2])   # Imprime todos os elementos do início ao fim de dois em dois


# Invertendo valores em uma lista  --reverse()
lista10 = [1 , 2, 3]
lista10.reverse()
print(lista10)

# Encontrando a soma, Valor Máximo, Valor Mínimo, Tamanho

print(sum(lista10))  # Soma
print(max(lista10))  # Valor Máximo
print(min(lista10))  # Valor Mínimo
print(len(lista10))  # Tamanho

# Converter uma lista em tupla
lista11 = [1, 2, 3, 4, 5, 6]
print(lista11)
print(type(lista11)) # Verificando o tipo de dado

tupla = tuple(lista11)
print(tupla)
print(type(tupla))  # Verificando o tipo de dado

# Desenpacotamento de uma lista
lista12= [1, 2, 3]
n1, n2, n3 = lista12 # As variáveis recebem como valor os itens da lista
print(n1)
print(n2)
print(n3)

# Criando uma cópia de uma lista (Deep Copy)
# Deep Copy é quando a alteração na cópia de uma lista não afeta a orignal
lista13=[1, 2, 3]
print(lista13)

nova = lista13.copy() # Realizou a cópia da lista13 para a lista nova
print(nova)

nova.append(4)
print(nova)

# Criando um cópia de uma lista (Shallow Copy)
# Na cópia via atribuição a modificação de uma reflete na original (Shallow Copy)
lista14=[1, 2, 3]
print(lista14)

nova1 = lista14
print(nova1)

nova1.append(4)

print(lista14)
print(nova1)