"""
Crie uma função que determine quando uma palavra está no plural, retornando True ou False
"""
def is_plural(word):
    return word.endswith("s")

print(is_plural("Evaldos"))