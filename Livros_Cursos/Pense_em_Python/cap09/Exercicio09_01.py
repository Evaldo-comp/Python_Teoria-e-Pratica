# Escreva um programa que leia words.txt e imprima apenas as palavras com mais de 20
# caracteres(sem contar espaços em branco)

fin = open("words.txt")
for line in fin:
    if len(line.strip()) > 20:
        print(line)
fin.close()
