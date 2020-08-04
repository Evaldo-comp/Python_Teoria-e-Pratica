'''Exercício05 - Crie duas tuplas e troque os itens entre elas'''

tupla1 = (1, 2, 3)
tupla2 = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

print(f'Tupla 1 antes da troca {tupla1}')
print(f'Tupla 2 antes da troca {tupla2}')

tuplatemp = tupla1
tupla1 = tupla2
tupla2 = tuplatemp

print(f'Tupla 1 depois da troca {tupla1}')
print(f'Tupla 2 Depois da troca {tupla2}')

'''Outra solução possivel
tupla1, tupla2 = tupla2, tupla'''