# Um dicionário comum não garante a ordem de seus elementos
# O ordered_dict supre esta necessidade

from collections import OrderedDict

dicionario =OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor= {valor}')