import random


def jogar_advinhacao():

    print("**********************************")
    print(" Bem Vindo ao jogo de Advinhação ")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil  (2) Médio (3) Difícil")

    nivel = int(input("Define o nível"))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print(numero_secreto)
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

    for rodada in range(1, total_tentativas+1):
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
            print(f"Você fez {pontos} pontos!!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("O chute é MAIOR do que o Número Secreto")
                if (rodada == total_tentativas):
                    print(f"O número secreto era {numero_secreto}")
                    print(f"Você fez um total de {pontos} pontos")
            elif(menor):
                print("Você Errou, O seu chute foi MENOR do que o número secreto")
                if (rodada == total_tentativas):
                    print(f"O número secreto era {numero_secreto}")
                    print(f"Você fez um total de {pontos} pontos")
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar_advinhacao()
