# Tags  Condicionais

"""Um barman está escrevendo um programa simples, para determinar se
 ele deve servir bebidas a alguém. Ele serve apenas
bebidas para pessoas com 18 anos ou mais e quando não está de férias.
O progrmaa que ele está escrevendo deve fgazer duas verificaoes:
1 -  Se o cleinte é maior de idade
2- Se ele não está de férias
"""

# Resolução mais extensa
def  servir_bebidas(idade, ferias):

    if idade <18 and ferias == True:
        return False
    elif idade <18 and ferias == False:
        return False
    elif idade >=18 and ferias ==True:
        return False
    elif idade >=18 and ferias ==  False:
        return True
    else:
        return 'Você digitou alguma opção inválida'



# Resolução compacta

def  servir_bebidas(idade, ferias):
    if idade >=18 and ferias ==False:
        return True
    return False

print(servir_bebidas(17, False))





