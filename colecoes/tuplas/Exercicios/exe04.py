'''Exercício04 - Acesso a itens, faça o que se pede'''

tupla =(('Azul', 2.4), ('Evaldo', 1, 4,True), ('Segunda', 'Terça','Quarta'), (12, 13, 14,))

#Acesse o item 'Segunda'
print(tupla[2][0])

#Acesse os respectivos itens 'Evaldo, 1',   '13,14', True
print(tupla[1][:2])
print(tupla[3][1:])
print(tupla[1][3])

#Acese os dias da semana e imprima de forma reversa
print(tupla[2][::-1])

# Desempacote alguma tupla
tuplex = tupla[3]
n1, n2, n3 = tupla[3]
print(f'Os itens desempacotados são {n1} {n2} {n3}')
