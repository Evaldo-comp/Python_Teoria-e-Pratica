"""
Modifique o jogo da forca (Programa 7.2) de forma a escrever a palavra secreta
cso o jogador perca.
"""
"""
Programa 7.2
"""

palavra = input("Digite a Palavra secreta:").lower().strip()
for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você Acertou")
        break
    tentativa =  input("\nDigite uma letra").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros +=1
            print("Você Errou")
        print("X==:==\nX : ")
        print("X 0 " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = " | "
        elif erros == 3:
            linha2 = "\| "
        elif erros >= 4:
            linha2 = "\|/"
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 += " / "
        elif erros >= 6:
            linha3 += " /\ "
        print(f"X{linha3}")
        print("X\n========")
        if erros == 6:
            print(f"Enforcado, a palavra secreta é {palavra}")
            break