print("**********************************")
print(" Bem Vindo ao jogo de Advinhação ")
print("**********************************")

numero_secreto = 42
count = 3
# rodada = 1  // variáel com valor declaravel utilizada apenas no whilr

""""
 -----------------Verificação utilizando While----------------------

while(rodada <= count):

    chute = int(input("Digite o número: "))
    menor = chute < numero_secreto

    print(f"Você chutou o núméro {chute}")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!!")
    elif (menor):
        print("Você Errou")
        print("O chute é MENOR do que o Número Secreto")
    else:
        print("Você Errou")
        print("O chute é MAIOR do que o Número Secreto")

    print(f'tentativa {rodada} de {count}')
    rodada += 1

---------------------------------------------------------------------------------------
"""

# Verificaçaõ utilizando for

for rodada in range(1, count+1):
    chute = int(input("Digite um  número entre 1 e 100: "))
    menor = chute < numero_secreto

    print(f"Você chutou o núméro {chute}")

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print(f"Você Acertou na {rodada} tentativa!!")
        break
    elif (menor):
        print("Você Errou")
        print("O chute é MENOR do que o Número Secreto")
    else:
        print("Você Errou")
        print("O chute é MAIOR do que o Número Secreto")

    print(f'tentativa {rodada} de {count}')
