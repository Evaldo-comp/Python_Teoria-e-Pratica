"""
Modifique o programa do exemplo 5.1 para, também, trabalhar com notas de 100

"""

valor = int(input("Digite o valor a pagar"))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${atual} ")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        if atual == 20:
            atual = 10
        if atual == 10:
            atual = 5
        if atual == 5:
            atual = 1
        cedulas =0