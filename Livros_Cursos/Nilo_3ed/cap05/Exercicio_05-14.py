"""
Escreva um programa que leia números inteiros do teclado.
o programa deve ler os números até que o usuário digite 0.
No final da execução, exiba a quantidade de númeeros digitados,
 assim como a soma e a média aritmética

"""
qtdnumeros = 0
soma = 0

while True:
    n = int(input("Digite um número"))
    soma += n
    qtdnumeros +=1
    if n == 0:
        break
print(f'''
Quantidade de números digitados: {qtdnumeros}
Soma: {soma}
Média: {soma/qtdnumeros}
''')