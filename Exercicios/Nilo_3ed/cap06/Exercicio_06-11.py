"""
Modifique o progrmaa 6.6 usando for:
"""
L=[]
qtd = int(input("Quantos elementos deseja adicionar à lista?"))

for i in range(qtd):
    n = int(input("Digite um número (0  sai)"))
    if n == 0:
        break
    L.append(n)
x = 0

for i in L:
    print(i)
