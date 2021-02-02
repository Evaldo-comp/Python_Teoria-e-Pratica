# A função filter() serve para filtrar dados de uma determinada  coleção
import statistics

dados = [1, 2, 3, 4.6, 4.1, 6, 8]

 # Calcula a média utilizando a função ,meam() da biblioteca statistics
media= statistics.mean(dados)

 # A função filter recebe dois parâmetros, sendo um uma função e o outro interáveis

res = filter(lambda x: x> media, dados)
print(list(res))

# Utilizando a função filter para retirar dados faltantes de uma coleção

mult_2 = [2, 4, 6, '', 8, '',10 ]

res = filter(None, mult_2)
print(list(res))

res=  filter(lambda x: x != '',  mult_2)
print(list(res))

#OBS: A função map() retorna apenas valores inteiros enquanto a função filter também retorna valores boleanos


# Retornando um nome menor que 5 caracteres
nomes = ['Vanessa', 'Ana', 'Maria']                 

instrutora = filter(lambda nome: len(nome) < 5, nomes)
print(f'A sua instrutora é {list(instrutora)}')

# Exemplo combinando map com filter

inst = list(map(lambda nome: f'O nome da sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)) )
print(inst)