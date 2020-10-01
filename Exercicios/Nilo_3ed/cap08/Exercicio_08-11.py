"""
Escreva uma função para validar uma variável string. Essa função deve receber como parâmetro
a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string
estiver entre os valores de máximo e mínimo, e falso, coso contrário
"""

def val_string(string, min, max):
    if min <= len(string) <= max :
        return True
    return False

print(val_string("arroz", 3, 3))