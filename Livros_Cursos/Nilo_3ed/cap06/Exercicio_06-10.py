"""
Modifique o programa do Exercicio 6.9 de forma a pesquisar p e v em toda a lista e informando
 o usuário a posição onde p e a posição onde v foram encontrados
"""

L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o  segundo valor a procurar: "))
achou = False
encontrado =None
x = 0
a = 0
b = 0
while x < len(L):
    if L[x] == p:
        #achou = True
        encontrado = p
        a = L[x]
        break
    if L[x] == v:
        encontrado = v
        b = L[x]
        break
    x+=1

if x < len(L):
    if  a or b != 0:

        if a > b :
            print(f'{encontrado}  primeiro achado na posição {x}')
        elif a < b:
            print(f'{encontrado}  primeiro achado na posição {x}')
    if a == 0:
        print(f'{p}  não encontrado ')
    if b == 0:
        print(f'{v}  Não encontrado ')

else:
    print(f'{p} e {v} não encontrado')