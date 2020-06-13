# Escreva um código que pegue um número e retorne uma lista com:
# O número, a metade do número, um quarto do número e um oitavo do número



def num_dv(n):
    lst = [n,n/2, n/4,n/8]
    return lst
num = int(input("Digite um número\n"))
print(num_dv(num))