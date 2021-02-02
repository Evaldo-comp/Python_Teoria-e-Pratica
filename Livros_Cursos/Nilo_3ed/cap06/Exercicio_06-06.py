"""
Modifique o programa 6.7 para trabalhar com duas filas. Para facilitar
seu trabalho, considere o comando A para atendimento da fila 1; e B
, para atendimento da fila 2. O mesmo para a chegada de clientes
: F para a fila 1; e G, para fila 2
"""


ultimo = 10
fila1 = list(range(1, ultimo+1))
fila2 = list(range(1, ultimo+1))
listop =[]
i = None
while True:
    print(f"\n Existem{len(fila1)} clientes na fila 1")
    print(f"\n Existem{len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("ou A para realizar o atendimento. S para sair")
    operacao = input("Digite a sequência de comandos desejados (F, A, S)\n")
    listop = list(operacao)

    for i in listop:

        if i == "A":
            if len(fila1)>0:
                atendido = fila1.pop()
                print(f"Cliente {atendido} da fila 01 atendido")
            else:
                print("Fila 1 vazia! Ninguém para atender.")
        elif i == "B":
            if len(fila2)>0:
                atendido = fila2.pop()
                print(f"Cliente {atendido} da fila 02 atendido")
            else:
                print("Fila 2 vazia! Ninguém para atender.")
        elif i == "F":
            ultimo += 1
            fila1.append(ultimo)
        elif i == "G":
            ultimo += 1
            fila2.append(ultimo)
        elif i == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S")

