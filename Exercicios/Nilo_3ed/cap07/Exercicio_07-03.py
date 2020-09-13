"""
Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres
que aparecem em uma delas
"""
string1 = input("Insira a primeira String ")
string2 = input("Insira a segunda String ")
D = []


for i in string1:
    if string2.count(i) == 0:
        D.append(i)
for j in string2:
    if string1.count(j) == 0:
        D.append(j)



print(f'{", ".join(D)}')