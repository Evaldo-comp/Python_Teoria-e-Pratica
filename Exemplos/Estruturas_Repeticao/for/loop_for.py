#Utilizando laços de repetição com for
################UTILIZANDO FOR#################################
"""
nome = "Evaldo"
lista =[1, 'eu', 3, 'a']
semana = range(1, 8)
#Iterando em uma String
for letra in nome:
    print(letra)
#Iterando em Lista
for itens in lista:
    print(itens)
#Iterando em um range
for dia in semana: #O range ignora o último valor
    print(dia)


Enumerate: Pega uma string e coloca dentro de uma tupla
"""
nome =  'Evaldo'
for i, letra in enumerate(nome):
    print(i, letra, end='')  #imprime o indice e sua respectiva letra
                            # end ='' faz com os itens apareçam todos na mesma linha