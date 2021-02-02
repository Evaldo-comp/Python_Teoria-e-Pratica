"""
Exemplo necessário para resolução dos exercicios 5.16, 5.17, 5.18, 5.19, 5.20 e 5.21

O programa ler um valor e imprime a quantidade de cédulas necessaŕias para pagar esse valor.
Os valores trabalhados são apenas inteiros e as cédulas são R$ 50, R$ 30, R$ 10, R$ 5 e R$ 1
"""
valor = int(input("Digite o valor a pagar"))
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