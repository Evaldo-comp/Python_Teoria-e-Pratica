"""

all() - retorna True se todos os iteráveis são verdadeiros ou ainda se o conjunto de interáveis estiver vazio
any () - retorna True se algum elemento do iterável for verdadeiro, se o iterável estiver vazio, retorna False
"""
#Exemplo all()

print(all([0,1,2,3,4,5]))

# Exemplo 2

print(all([num for num in [4, 2, 10, 8] if num %2 ==0]))

# Exemplo any()

print(any([1,2,3,4,5,6]))