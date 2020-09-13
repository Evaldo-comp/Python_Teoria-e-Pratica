"""
Para utilizar módulos externos é preciso fazer uso de um gerenciador de pacotes
chamado PIP - Python Insaller Package

O módulo importado neste exemplo chama-se Colorama:(permite a impressão de
textos coloridos no terminal)

Site para baixar módulos: https://pypi.org
"""

from colorama import init, Fore
init()

print(Fore.LIGHTBLACK_EX + 'Evaldo')