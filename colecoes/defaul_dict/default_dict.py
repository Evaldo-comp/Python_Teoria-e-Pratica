# O default dict evita que o programa retorne o Keyerror caso seja chamado uma chave sem valor
# Se acontecer de ser chamado uma chave e um valor que não exsite, uma chave é criado e um valor
# default é atribuido a ela.


#Realizando o import
from collections import defaultdict


dic = {'Segunda':'NL', 'Terça':'IC', 'Quarta':'IE'}
print(dic)

dicionario = defaultdict(lambda: 0)

print(dicionario)

print(dicionario['chave inexistente'])
print(dicionario)