"""
Escreva uma função que receba uma string com as opções válidas a aceitar
(cada opção é uma letra). Converta as opções válidas para letras minúsculas.
Utilize input para ler uma opção, converter o valor para letras minúsculas
e verificar se a opção é válida. em caso de opção inválida,a função deve
pedir ao usuário que digite novamente a opção.
"""
def genero(pergunta):
    while True:
        p = input(pergunta)
        if p.lower() == "m" or p.lower() == "f":
            print("Opção Válida")
            break
        print("Opção inválida, digite novamente")

genero("Qual seu genero M - Masculino ou F - Feminino")