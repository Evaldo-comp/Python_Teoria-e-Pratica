"""
A função seek() é utilizada para movimentar o cursor pelo arquivo
"""
arquivo = open('texto.txt')
print(arquivo.read())

# Coloca o cursor no caractere 30
arquivo.seek(30)

# Lê o arquivo a partir do caractere 30
print(arquivo.read())

# readline() : função utilizada para Ler o arquivo linha a linha
arquivo = open('texto.txt')
print(arquivo.readline())

#OBS: ao trabalhar com arquivos é importante fechá-los quando acabarmos de utilizá-lo
# Abrir arquivo
arquivo = open('texto.txt')

# Utilizar o Arquivo
print(arquivo.read())

# Fechar o Arquivo
arquivo.close()

# Para verificar a situação atual do arquivo, utiliza-se a função closed
arquivo = open('texto.txt')
print(arquivo.closed)