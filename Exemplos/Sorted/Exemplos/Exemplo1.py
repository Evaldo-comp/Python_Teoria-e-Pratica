"""
@Evaldo 2020
O programa a seguir ordena uma lista de estudantes, utilizando sorted()
Adaptado de  https://docs.python.org/pt-br/dev/howto/sorting.html

"""

tupla_estudantes = [
    ('Ana', 'A', 18),
    ('Pedro', 'B', 17),
    ('Roberto', 'C', 12),
]

print(sorted(tupla_estudantes, key = lambda estudante: estudante[2])) # vai ordenar pela idade

# a mesma operação utilizando funções do móodulo operator
from operator import itemgetter, attrgetter

print(sorted(tupla_estudantes, key=itemgetter(2))) # ordena pleo item 2


