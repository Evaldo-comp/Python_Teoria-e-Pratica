"""
Você recebe os ingredientes de um sandwich dentro de uma lista. Devolva essa lista
apenas com os ingredientes do meio, ou seja, ignore o pão.
"""

def sanduba(s):
    return s[1:-1]

ingredientes=['Pão', 'Queijo', 'Tomate', 'Bacon', 'Ovo', 'Alface', 'Pão']

print(sanduba(ingredientes))

# A mesma solução utilizando list comprehension
def sanduba(sandwich):
	return([s for s in sandwich if s != 'Pão'])
print(sanduba(ingredientes))