"""
 Args não é uma palavra reservada para este caso, sendo assim a nomeclatura *args é apenas convensão, podendo desta forma
 ser nomedado como te convenha.
 a função do *args é receber argumentos e aloca-los em um a tupla


# Exemplo de uma função simples sem *args
# no caso do exemplo abaixo a quantidade de argumentos
# deve ser igual a quantidade de parâmentros e vice versa.
def soma(n1, n2, n3):
    return n1+n2+n3


print(soma(1, 3, 5))


# Utilizando o args
def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma(19,2,1,2))
"""
# Utilizando o args de maneira mais compacta
def soma(*args):
    return sum(args)

print(soma(19,2,12,2))

# Utilizando args para fazer verificação

def verifica(*args):
    if 'Maria' in args and 'José' in args:

        return 'Maria e Jośe encontrados'
    return 'Não encontrados'

print(verifica('José', 'Pedro', 'Jonatas', 'Ana', 'Maria'))