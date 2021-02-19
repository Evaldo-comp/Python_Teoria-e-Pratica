# Escreva uma função void que receba uma palavra e uma série de letras proibidas, e retorne True se a
# palavra não usar nenhuma das letras proibidas.
L = []
a = ''
print("Insira as letras proibidas e 3 para sair")
while a != '3':
    a = input("Palavra: ")
    L.append(a)
print(L)

with open("words.txt", 'r') as words:
    line = words.readlines()
    for i in L:
        if i.upper() not in line:
            print(line)
print(L)
