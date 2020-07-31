# Crie uma função que receba três valores, e retorne a difenreça entre o maior e o menor

def dif(v1,v2,v3):
    lst = [v1, v2, v3]
    return max(lst) -  min(lst)

v1= int(input("Digite o primeiro valor\n"))
v2= int(input("Digite o segundo valor\n"))
v3= int(input("Digite o terceiro valor\n"))

print(f'A diferença entre o maior valor e o menor é {dif(v1,v2,v3)}')