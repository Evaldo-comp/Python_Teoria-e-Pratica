# Escreva uma função void que receba uma palavra e uma série de letras proibidas, e retorne True se a
# palavra não usar nenhuma das letras proibidas.

def avoids(word, proibidas):
    for i in proibidas:
        if i in word:
            return True
        else:
            return False


L = ['a', 'c', 'd']

print(avoids("Ovo", L))
