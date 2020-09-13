"""
* Escreva um programa que leia duas strings e gere uma terceira com
* os caracteres comuns às duas strings lidas.
"""

string1 = input("Insira a primeira String ")
string2 = input("Insira a segunda String ")
L =[]

for i in string1:
    for j in string2:
        if i == j:
            L.append(i)
print(f'{", ".join(L)}')

