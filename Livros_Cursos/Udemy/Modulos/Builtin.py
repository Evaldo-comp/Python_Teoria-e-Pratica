"""
Módulos Builtins são módulo que fazem parte  da linguagem e a acompanham na instalação padrão.

OBS:  abaixo seguem vários exemplos, execute individualmente comentando so demais.
"""
####################################################################################
# Utilizando alias (apelidos) no módulo

import random as rdm

print(rdm.random()
#####################################################################################
# Utilizando alias (apelidos) na função
from random import randint as rdi
print(rdi(10, 100))

######################################################################################
# Ao utilizar um * no import estaremos importando todas as funções de um módulo

import random*
print(random()))
