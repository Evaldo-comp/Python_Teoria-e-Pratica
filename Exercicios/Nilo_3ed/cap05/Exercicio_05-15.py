"""
Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a
quantidade comprada. Utilize os códigos a seguir para obter o preço de cada produto.

CÓDIGO = 1    PREÇO = 0.50
CÓDIGO = 2    PREÇO = 1.00
CÓDIGO = 3    PREÇO = 4.00
CÓDIGO = 5    PREÇO = 7.00
CÓDIGO = 9    PREÇO = 8.00

Seu programa deve exibir o total das compras depois depois que o usuário
digitar 0. Qualquer outro código deve gerar a mensagem de erro " Código Inválido"
"""
soma  =0
cod = None
qtd = 0
while True:
    cod = int(input("Digite o código do produto"))


    if cod == 1:
        qtd = int(input("Insira a quantidade que deseja comprar"))
        total = qtd * 0.50

    elif cod == 2:
        qtd = int(input("Insira a quantidade que deseja comprar"))
        total = qtd * 1.00

    elif cod == 3:
        qtd = int(input("Insira a quantidade que deseja comprar"))
        total = qtd * 4.00

    elif cod == 5:
        qtd = int(input("Insira a quantidade que deseja comprar"))
        total = qtd * 7.00

    elif cod == 9:
        qtd = int(input("Insira a quantidade que deseja comprar"))
        total = qtd * 8.00


    elif cod == 0:
        break
    else:
        print("Código Inválido")
    soma += total

print(f'O total das compras é R${soma} Reais')

