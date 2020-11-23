# Utilizando o with

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
# arquivo.close()  nesse caso, não é necessário utilizar o método close(0)
