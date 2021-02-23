""""
Escreva uma função que encontre todos os pares inversos da lista de palavras
"""
t = []


def open_words():
    fin = open("Livros_Cursos/Pense_em_Python/cap10/palavras.txt")
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


rever = []


def par_inverso():
    for i in open_words():
        if i[::-1] == i:
            rever.append(i)
    return rever


print(open_words())
print(par_inverso())
