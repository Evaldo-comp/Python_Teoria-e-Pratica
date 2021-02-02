"""
    Exemplo de ordenação de lista utilizando Bubble Sort
    Fonte: Introdução à Programação com Python by Nilo Ney Coutinho
"""

L = [7, 4, 3, 12, 8]
fim = len(L) # indica a quantidade de elementos da lista
while fim > 1:
    trocou = False
    x = 0
    while x <(fim-1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x + 1] = temp
        x+=1
    if not trocou:
        break
    fim -=1
for e in L:
    print(e)
