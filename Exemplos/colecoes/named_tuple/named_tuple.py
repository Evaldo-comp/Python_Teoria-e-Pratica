# São tuplas que recebem nomes e parâmentros

from collections import namedtuple

# Definindo nome e parâmetros para a tupla
# Forma 1
aluno = namedtuple('aluno', 'matricula semestre media')

# Forma 2
aluno = namedtuple('aluno', 'matricula, semestre, media')

# forma 3
aluno = namedtuple('aluno', ['matricula', 'semestre', 'media'])

Jose = aluno(matricula = 12231, semestre= 2,  media = 7)
print(Jose)
