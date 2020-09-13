"""
Um arquivo aberto para leitura nao suporta escrita e vice-versa

OBS: Ao abrir um arquivo em modo escrita, se ele não existir, um arquivo novo
será criado, se esse arquivo já existir ele será substituido pelo novo, ou seja
o arquivo existente irá se perder.
"""

# Exemplo de abertura para escrita

with open('text.txt', 'w') as arquivo: # o argumento w, indica que é um arquivo de escrita
    arquivo.write("Inserindo uma nova linha de conteúdo para teste\n")
    arquivo.write("Apenas mais uma linha para teste\n")

# Abertura e escrita em arquivo não pythônica

arquivo = open('texto.txt', 'w')
arquivo.write('Nova linha')
arquivo.close()

# Recebendo dados do usuário e escrevendo em um arquivo

with open('Linguagens.txt', 'w') as linguagens:
    while(True):
        ling = input("Digite o nome de uma linguagem de programação")
        if ling != 'sair':
            linguagens.write(ling)
            linguagens.write("\n")
        else:
            break