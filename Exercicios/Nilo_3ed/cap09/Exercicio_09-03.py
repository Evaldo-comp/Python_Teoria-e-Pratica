"""
* Crie um programa que leia os arquivos pares.txt e imapres.txt e que crie um só arquivo
* pareseimpares.txt com todas s linhas dos outros arquivos, de forma a preservar a ordem
* númerica.
"""


def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip() != "":
            return int(número)


def escreve_número(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
impares = open("impares.txt", "r")
pares_impares = open("pareseimpares.txt", "w")
npar = lê_número(pares)
nímpar = lê_número(impares)
while True:
    if npar is None and nímpar is None:  # Termina se ambos forem None
        break
    if npar is not None and (nímpar is None or npar <= nímpar):
        escreve_número(pares_impares, npar)
        npar = lê_número(pares)
    if nímpar is not None and (npar is None or nímpar <= npar):
        escreve_número(pares_impares, nímpar)
        nímpar = lê_número(impares)

pares_impares.close()
pares.close()
impares.close()
