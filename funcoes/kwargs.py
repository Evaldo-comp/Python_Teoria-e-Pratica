""" O **kwargs é uma forma mais robusta do args, este ao contrário daquele permite que
trabalhemos com dicionários, para isso ele utiliza parâmentros nomeados

#obs:
Ordem correta da declaração de parâmentros em uma função
- Parâmentros Obrigatórios
- *args
- Parâmentros default
- **kwargs

#Exemplo1

def pets(**kwargs):
    for pessoa, pet in kwargs.items():
        print(f'O pet de {pessoa} é um {pet}')

#semana(1 = 'Domingo', 2 = 'Segunda', 3 ='Terça', 4 = 'Quarta', 5 ='Quinta', 6 ='Sexta', 7 ='Sábado')

pets(Pedro= 'Gato', Ana = 'Cachorro', Maria = 'Papagaio')

#Exemplo2
# O **kwargs é capaz de fazer uma verificação entre chave e valor dentro de uma dicionário
def pet_vicio(**kwargs):
    if 'Pedro' in kwargs and kwargs['Pedro'] == 'Gato':
        return 'Pedro é gatólatra'
    elif 'Pedro' in kwargs and kwargs ['Pedro'] == 'Cachorro':
        return 'Pedro é Cachorrólatra'
    return 'Pedro não gosta de animais'


print(pet_vicio(Pedro = 'fuinha'))

#Prática:
# Utilizando a estrtura do exemplo acima crie um código que faça a verifição entre usuário e senha
#e forneça acesso quando a senha correspinder ao usuário

#Resposta da Prática

def acesso(**kwargs):
    if 'usuario' in kwargs and kwargs['usuario'] == '1234':
        return 'Acesso Concedido'
    return 'Acesso Negado'

senha=input('Digite sua senha')
print(acesso(usuario= senha))
"""


# Desempacotar no kwargs
def mostra_nomes(**kwargs) :
    return f"{kwargs [ 'nome' ]} {kwargs [ 'sobrenome' ]}"


nomes = {'nome' : 'Evaldo', 'sobrenome' : 'Pereira'}

print(mostra_nomes(**nomes))  # desempacotando
#OBS: O nome das chaves do dicionário que serpa desempacotado
# devem ser os mesmos que foram passados nos parâmetros a função
