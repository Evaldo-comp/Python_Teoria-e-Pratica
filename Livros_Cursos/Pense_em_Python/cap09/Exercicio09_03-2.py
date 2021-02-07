# Escreva um programa que leia words.txt e imprima apenas as palavras com mais de 20
# caracteres(sem contar espaços em branco)

fin = open("words.txt")

cont, cont2 = 0, 0


for i in fin:
    if "e" not in i.lower():
        print(i)
        cont += 1
    else:
        cont2 += 1
    total = cont+cont2
por = (cont/total)*100
print(f"    Existem {por:.2f}% de palavras sem a letra 'e'")
