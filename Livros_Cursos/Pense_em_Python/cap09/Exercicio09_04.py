# escreva uma função chamada use_only que receba uma palavra e uma série de letras obrigatórias
# e retorne True, se a palavra só contiver letras da lista
a = 0


def uses_only(word, L):
    a = 0
    for i in L:
        if i in word:
            a += 1
    if a == len(word):
        return True
    else:
        return False


L = ['a', 'c', 'e', 'f']
print(uses_only('acef', L))
