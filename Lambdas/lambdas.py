# lambdas são funções anônimas, sem nome

# exemplo de função Python
def quadrado(x):
    return x ** 2

# A mesma expressão anterior, utilizando lambda
quad = lambda x:  x ** 2

print(quad(4))
print(quadrado(3))

#Lambda sem entrada
msg = lambda: 'Essa é uma lambda sem entradas'

# Lambda com uma entrada
quad = lambda x:  x ** 2

# lambda com duas entradas
atri = lambda b, h: b * h /2

# Lambida com três entradas
med = lambda n1, n2, n3: (n1 + n2 + n3)//3

# execução das lambdas
print(msg())
print(quad(4))
print(atri(4, 6))
print(med(5, 6, 8))

