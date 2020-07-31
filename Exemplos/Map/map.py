# o map faz o mapeamento entre valores e funções. Basicamente map é uma função que recebe
# dois parâmetros onde o primeiro é uma função e o segundo um iterável

def dobro(n):
    """Calcula o dobro de um número"""
    return n * 2

lst = [1, 2, 3, 4, 5]

dob = map(dobro, lst)
print(list(dob)) # Os dados são convertidos para lista, não podem ser imprimidos na forma de map Object

# Exemplo anterior utilizando expressão lambda
dobro_lambda = lambda x: x * 2

dob = map(dobro_lambda, (lst))
print(list(dob))

# Melhorando o código anterior
print(list(map(lambda x: x*2, lst)))

# OBS: Apos a primeira utilização da função map ela zera

