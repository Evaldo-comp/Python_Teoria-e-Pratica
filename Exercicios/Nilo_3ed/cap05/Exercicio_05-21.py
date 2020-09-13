"""
Reescreva o programa 5.1 de forma a continuar executando até que o valor digitado seja 0.
Utilize repetições aninhadas

"""
while True:

    valor = int(input("Digite o valor a pagar"))
    if valor == 0:
        break
    cedulas = 0
    atual = 50
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            print(f"{cedulas} cédula(s) de R${atual} ")
            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            if atual == 20:
                atual = 10
            if atual == 10:
                atual = 5
            if atual == 5:
                atual = 1
            cedulas =0