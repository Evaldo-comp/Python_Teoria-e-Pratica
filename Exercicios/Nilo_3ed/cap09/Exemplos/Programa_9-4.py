# with em uma só linha

with open("impares.txt", "w") as impares, open("pares", "w") as pares:
    for n in range(0, 1000):  # gera uma lista de numeros de 0 a 1000
        if n % 2 == 0:
            pares.write(f"{n}\n")  # escreve os pares no arquivo pares
        else:
            # escreve os impares no arquivo impares
            impares.write(f"{n}\n")
