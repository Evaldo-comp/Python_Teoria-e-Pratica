import forca
import advinhacao


def escolha_jogo():
    print("**********************************")
    print("       Escolha o seu Jogo         ")
    print("**********************************")

    print("(1) Forca  (2) Advinhação")

    jogo = int(input("Qual o jogo?"))

    if (jogo == 1):
        print("Forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("advinhação")
        advinhacao.jogar_advinhacao()


if (__name__ == "__main__"):
    escolha_jogo()
