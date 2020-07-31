"""
o zip() junta dois ou mais iteráveis e retorna uma tupla  formada por  um item de cada iterável
"""

# Exemplo01
ls1 = [1, 2, 3, 4]
ls2 = ['evaldo', 'Ana', 'Sérgio', 'Silvia']

zip1 = zip(ls1, ls2)
print(list(zip1))