"""
Leitura de Arquivos:

Para ler um arquivos utiliza-se a função open()
"""

# Exemplo:
arquivo = open('texto.txt')

# A função read(), lê todo o arquivo
print(arquivo.read())

# Abrindo um texto apenas com permissão de leitura
arquivo = open('texto.txt','r')
print(arquivo.read())

# Abrindo um arquivo do texto com permissão de escrita
arquivo = open('texto.txt','w')
print(arquivo.read())
