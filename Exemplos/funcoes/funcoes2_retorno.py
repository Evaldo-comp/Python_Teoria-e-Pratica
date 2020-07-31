'''Um afunção para retornar algo, deve vir com o comando retun dentro de seu coprpo principal
'''

def quadrado(n):
    return n * n

num = int(input("Digite o número para que o quadrado dele possa ser  retonado pela função"))

print(f' O quadrado de {num} é: {quadrado(num)}')

#OBS: Se uma função não tem a função de print() no seu corpo. ela deve ser acionado com o print para
#que seja posivel ver o seu retorno

# Obs sobre a plavra reservada return


#3 - Podemos retirnar varios d tipso de dados diferentes
#1 - Ela finaliza afunção ou seja ela saida  função
#Exe1 -
def exe1():
    return 'OI'
    print("Esse trecho não vai ser excecutado")
print(exe1())

#2 - Podemos ter mais de um tipo de dado no return
def exe2(a):
    if a ==1:
        return 'Você digitou o número 1'
    elif a == 2:
        return 2
    elif a == 3:
        return 3.2
    else:
        return True

print(exe2(3))

# Um return pode devolver mais de um valor ao mesmo tempo

def varios_valores():
    return 1,3,4,5

print(varios_valores())