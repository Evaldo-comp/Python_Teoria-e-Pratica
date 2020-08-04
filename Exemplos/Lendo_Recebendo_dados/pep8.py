"""
PEP8 - Python Enhacement Proposal

São propostas de melhorias a Linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica
************************************************************************************
[1] - Utilizar camel case para nomes de classes
************************************************************************************
class Calculadora:
    pass
************************************************************************************
[2] - Utilizar nomes minusculos, separados por underlaine para funções ou cariáveis
************************************************************************************
def soma():
    pass

def soma_dois():
    pass

numero = 4
************************************************************************************
[3] - Utilize 4 espaços para identação!(não use o tab)
************************************************************************************
if 'c' in 'banana':
    print('tem')
else:
    print('Não tem')

[4] Linhas em branco
- Separar funções e definições de classes com duas linhas em branco:
- Métodos dentro de uma classe devem ser separados com uma unica linha em, branco

[5] - Imports

- Imports deve ser sempre feitos em linhas separadas:

#import Errado
import sys, os

#import Certo
import sys
import os

#Não há problemas em utilizar:
from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType
    ListType
    SetType
    SetType
    OutroType
)
# import devem ser colocados no top dos arquivos logo depois de qualquer
comentários ou qualquer docstrings, antes de constantes ou variaveis globais

[6] - Espaços em expressoes e instruções

#Não faça

funçõa( algo[ ] , { outro: 2})

#Faça:

funcao(algo[]), (outro:2})

#Não Faça:
algo (1)

#Faça:
algo(1)

#Não Faça

dict ['chave'] = lista [indice]

#Faça:

dic['chave'] = lista[indice]

#Não Faça:
x   =1
y   =2

#Faça:
x=1
y=2
[7] - Termine sempre uma instrução comm uma nova linha
"""
import this



