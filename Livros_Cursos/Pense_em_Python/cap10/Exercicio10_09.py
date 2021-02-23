
def make_word_list1():
    t = []
    fin = open("Livros_Cursos/Pense_em_Python/cap10/palavras.txt")
    for line in fin:
        word = line.strip()
        t.append(word)
    print(t)


def make_word_list2():
    t = []
    fin = open("Livros_Cursos/Pense_em_Python/cap10/palavras.txt")
    for line in fin:
        t += [line.strip()]

    print(t)


make_word_list1()
make_word_list2()
"""
t = []
fin = open("Livros_Cursos/Pense_em_Python/cap10/palavras.txt")
for line in fin:
    word = line.strip()
    t.append(word)
print(t)
"""
