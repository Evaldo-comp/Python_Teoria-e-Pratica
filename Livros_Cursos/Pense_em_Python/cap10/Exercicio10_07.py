"""
duas palavras são anagramas se você puder soletrar uma rearrajando as letras da outra. escreva uma função
chamada is_anagram que tome duas strings e retorne True se forem anagramas.
"""

t = [1, 2, 3, 4, 5]


def has_duplicates(t):
    a = 0
    for i in t:
        if t.count(i) > 1:
            a += 1

    if a > 1:
        return True
    return False


print(has_duplicates(t))
