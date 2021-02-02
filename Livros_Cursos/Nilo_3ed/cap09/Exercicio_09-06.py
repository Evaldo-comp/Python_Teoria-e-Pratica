
LARGURA = 79
i = 0

with open("entrada.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0] == "=":
            while(i <= 40):
                print(f"{i}{linha}")
                i += 1
