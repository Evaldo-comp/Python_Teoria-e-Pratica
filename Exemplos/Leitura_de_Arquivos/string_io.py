"""
Para ler ou escrever dados em arquivos do sistema operacional, o software precisa
ter permissão de leitura e escrita

stringIo utilizado para ler e criar arquivos em memoria
"""
# primeiramente faz-se o import
from io import StringIO

# cria-se uma string de modo normal
mensagem = "Essa e uma mensagem de teste"

# cria-se um arquivo, que pode já vir com a string escrita nele
arquivo = StringIO(mensagem)

# utilizando o arquivo
print(arquivo.read())

# Escrevendo outros textos
arquivo.write("  Outro teste")

arquivo.seek(10)

print(arquivo.read())