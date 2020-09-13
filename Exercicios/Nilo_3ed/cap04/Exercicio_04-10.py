"""
Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo
de instalção: R para residências , I para indústrias e C para comércios.
Calcule o preço  a pagar de acordo com a tabela a seguir.

                -------------------------------------------------
                |      Preço por tipo e faixa de consumo        |
                -------------------------------------------------
                |    Tipo     |   Faixa (kWh) |       Preço     |
                | Residencial | Até 500       |      R$ 0,40    |
                |             | Acima de 500  |      R$ 0,65    |
                | Comercial   | Até 1000      |      R$ 0,55    |
                |             | Acima de 1000 |      R$ 0,60    |
                | Industrial  | Até 50000     |      R$ 0,55    |
                |             | Acima de 5000 |      R$ 0,60    |
                -------------------------------------------------
"""

# Solução

tipoInsta = input('''
Qual o tipo de instalação:
Digite R ou r : Para Residencial
Digite I ou i : Para Industrial
Digite C ou c : Para Comercial\n
''')
consumo = int(input("Insira a quantidade de kWh consumida"))
conta = None

if tipoInsta == 'R' or tipoInsta == 'r':
    if consumo <= 500:
        conta = consumo * 0.40
        print(f'O valor da sua conta de luz é R$ {conta:.2f} Reais')
    else:
        conta = consumo * 0.65
        print(f'O valor da sua conta de luz é R$ {conta:.2f} Reais')
elif tipoInsta == 'I' or tipoInsta == 'i':
    if consumo <= 1000:
        conta = consumo * 0.55
        print(f'O valor da sua conta de luz é R$ {conta:.2f} Reais')
    else:
        conta = consumo * 0.60
        print(f'O valor da sua conta de luz é R$ {conta:.2f} Reais')
elif tipoInsta == 'C' or tipoInsta == 'c':
    if consumo <= 5000:
        conta = consumo * 0.55
        print(f'O valor da sua conta de luz é R$ {conta:.2f} Reais')
    else:
        conta = consumo * 0.60
        print(f'O valor da sua conta de luz é R$ {conta:.2f} Reais')
else:
    print(" Inserção errada, por favor insira um tipo de instalação válido.")
