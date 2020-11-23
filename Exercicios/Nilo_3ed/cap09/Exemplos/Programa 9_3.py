# Gravação de números pares e ímpares em arquivos diferentes

with open("impares.txt", "w") as impares:  # cria arquivo impares
    with open("pares", "w") as pares:  # cria o arquivo pares
        for n in range(0, 1000):  # gera uma lista de numeros de 0 a 1000
            if n % 2 == 0:
                pares.write(f"{n}\n")  # escreve os pares no arquivo pares
            else:
                # escreve os impares no arquivo impares
                impares.write(f"{n}\n")
