# Definição de um dicionário
capitais = {'Ceara':'Fortaleza', 'Bahia': 'Salvador', 'Tocantins':'Palmas', 'Rio de Janeiro':'Rio de Janeiro'}

# Acessando elementos
print('##########################ACESSANDO ELEMENTOS####################################')
# Forma -1: Via Chave
print(capitais['Ceara'])
print(capitais['Rio de Janeiro'])

#Forma - 2:  Via get
print(capitais.get('Tocantins'))
print(capitais.get('B','Não encontrado'))# Recebe um valor padrão para retornar caso não encontre o solicitado

#Verificar a exsitencia de alguma chave no dicionario
print('Tocantins' in capitais)

print('##########################ADICIONANDO ELEMENTOS####################################')
#Adicionando Elementos
#Forma -1

cagece = {'jan':210, 'Fev':120, 'Mar':230}
cagece['Abr']=150
print(cagece)

# Forma - 2
novo = {'Mai':230}
cagece.update(novo)
print(cagece)

print('##########################ATUALIZANDO ELEMENTOS####################################')
# Atualizando Elementos
cagece = {'jan':210, 'Fev':120, 'Mar':230}
# Forma -1
cagece['Abr']=160
print(cagece)

# Forma - 2
cagece.update({'Fev':130})
print(cagece)

print('##########################REMOVENDO ELEMENTOS####################################')
# Removendo Elementos
# Forma - 1:
cagece = {'jan':210, 'Fev':120, 'Mar':230}
rem = cagece.pop('jan') # Ao remover, o pop() também retorna o valor removido
print(cagece)
print(rem)

# Forma 02:
del cagece['Mar']
print(cagece)

print('##########################COPIANDO DICIONARIOS####################################')
# Copiando
# Forma - 1:
cagece = {'jan':210, 'Fev':120, 'Mar':230}
c2 = cagece.copy()
print(c2)

# Forma - 1:
c3 = cagece
print(c3)

print('##########################MÉTODOS IMPORTANTES####################################')
# MÉTODOS IMPORTANTES

dic = {'a':1, 'b':2, 'c':3, 'd':4}
#Limpar um dicionario .clear()
dic.clear()
print(dic)


