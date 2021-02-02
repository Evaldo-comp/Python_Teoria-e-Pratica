"""
Altere o programa 6.7 de forma a poder trabalhar com vários comandos
digitados de uma só vez. Atualmente, apenas um comando pode ser inserido
por vez. Altere-o de forma a considerar operação como uma string
"""

ultimo = 10
fila = list(range(1, ultimo+1))
listop =[]
i = None
while True:
    print(f"\n Existem{len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("ou A para realizar o atendimento. S para sair")
    operacao = input("Digite a sequência de comandos desejados (F, A, S)\n")
    listop = list(operacao)

    for i in listop:

        if i == "A":
            if len(fila)>0:
                atendido = fila.pop()
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif i == "F":
            ultimo += 1
            fila.append(ultimo)
        elif i == "S":
            break
        else:
            print("operação inválida! Digite apenas F, A ou S")

