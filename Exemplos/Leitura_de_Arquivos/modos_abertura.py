"""
Modos de abertura:

r : Abre apenas para leitura
w : Abre para escrita -  sobrescreve se o arquivo já existir
x : Abre para escrita somente se o arquivo não existir
a : Abre para escrita e adiciona o novo conteúdo no final do já existente,
se não existir nenhum, esse modo irá criar um novo arquivo
+ : Abre aatualizaçao seja de leitura ou escrita
"""
'''
# modo x
with open('teste.txt','x') as arquivo:
    arquivo.write('teste')
'''
# modo a
with open('teste3.txt','a') as arquivo:
    arquivo.write('teste')