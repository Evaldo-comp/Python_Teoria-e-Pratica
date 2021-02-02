"""
    Escreva uma função chamada right_justify, que receba uma string chamada s como parãmentro e exiba
    a string com espaços sufucuentes à frente para  que a última letra da string esteja na coluna 70 da tela.
"""

def right_justify(s):
    numero_espacos = 70 - len(s)
    #print("{0:>numero_espacos}".format(s))
    espaco = "0"
    print(f"{espaco * numero_espacos}{s}")


right_justify("Eu amo abacate")