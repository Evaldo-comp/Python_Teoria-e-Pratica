"""
Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h

"""
# Solução

velocidade = int(input("Qual a velocidade do carro?"))

if velocidade > 80:
    print("Você foi multado no valor de R$ ", (velocidade - 80) * 5, "Reais")


