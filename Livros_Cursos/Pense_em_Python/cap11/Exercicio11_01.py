""""
Escreva uma função que encontre todos os pares inversos da lista de palavras
"""
t = []


def open_words():

    fin = open("Livros_Cursos/Pense_em_Python/cap11/palavras.txt")
    d = {x.strip(): x.lower().strip() for x in fin}
    return d


print(open_words())
