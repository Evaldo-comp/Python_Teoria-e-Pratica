"""
Faça  um programa para escrever a contagem regressiva do lançamento
de um foguete. O programa deve imprimir 10, 9, 8..., 1, 0 e fogo! na tela.

"""

# Solução

x = 10
while(x >=0):
    print(x, end=', ')
    x -= 1
print("e Fogo!")