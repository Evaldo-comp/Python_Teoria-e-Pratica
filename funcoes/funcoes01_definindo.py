# Definindo funções

# Def - nome_da_função (parametros):

def noob():
    print('oi')


noob()


def patativa() :
    print('''
    POEMA 1
    
    Sertão, argúem te cantô,
    Eu sempre tenho cantado
    E ainda cantando tô,
    Pruquê, meu torrão amado,
    Munto te prezo, te quero
    E vejo qui os teus mistéro
    Ninguém sabe decifrá.
    A tua beleza é tanta,
    Qui o poeta canta, canta,
    E inda fica o qui cantá.''')


def goulart():
    print('''
    POEMA 21
    
    Uma parte de mim
    é todo mundo;
    outra parte é ninguém:
    fundo sem fundo.

    Uma parte de mim
    é multidão:
    outra parte estranheza
    e solidão.''')


def f_pessoa() :
    print('''
    POEMA 3   
   
    O poeta é um fingidor.
    Finge tão completamente
    Que chega a fingir que é dor
    A dor que deveras sente.''')


patativa()
goulart()
f_pessoa()


# Ao chamar o nome do poeta as funções retornaram o nome do poema

def nome_poema(p):
    if p == 1:
        print("O poema é : EU E O SERTÃO de Patativa do Assará")
    elif p == 2:
        print("O Poema é : TRADUZIR-SE de Ferreira Goulart")
    elif p == 3:
        print("O Poema é : AUTOPSICOGRAFIA de Fernando Pessoa")
    else:
        print("Valor inválido")

p = int(input("Qual poema você deseja sabeo o nome? digite a opção 1, 2 ou 3"))
nome_poema(p)

nomes = nome_poema  # Deve-se associar a variável sem o parênteses
nomes(p)

# Obs: Não é uma prática muito utilizada nem aconcelhável.