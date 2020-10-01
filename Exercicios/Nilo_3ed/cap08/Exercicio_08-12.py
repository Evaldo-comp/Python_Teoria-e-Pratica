"""
Escreva uma função que receba uma string e uma lista. A função deve comparar
a string passada com os elementos da lista, também passada como parâmentro
Retorne verdadeiro se a string for encontrada dentro da lista e falso, caso contrário.
"""

def val_str_lst(string, lista):
    for i in lista:
        if i == string:
            return True
        return False

lista = ["Evaldo", "Ana", "Pedro"]

print(val_str_lst("Evaldo", lista))
