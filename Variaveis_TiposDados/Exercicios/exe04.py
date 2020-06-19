""" a função eval()
Esta função resolve alguma equação que é passada como argumento
se este argumento estiver em forma de string, uma conversão deverá ser feita
para que a função eval() rresolva
"""

#Prática: Crie uma função que devolva o valor de uma equação passada como texto

def eq(evaluate):
    return eval(str(evaluate))

exp = input("Insisra uma equação")
print(eq(exp))