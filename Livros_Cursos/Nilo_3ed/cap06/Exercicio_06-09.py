"""
Modifique o exemplo para pesquisar dois valores. Em vez de apenas p,
leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro.

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