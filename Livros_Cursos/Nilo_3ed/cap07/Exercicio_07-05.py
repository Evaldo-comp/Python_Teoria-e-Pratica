"""
Escreva um programa que leia duas strings e gere uma terceira, na qual
os caracteres da segunda foram retirados da primeira
"""
string1 = input("Digite a primeira string")
string2 = input("Digite a segunda string")
string3 = ""

for i in string1:
    if i not in string2 :
        string3 += i


print(string3)