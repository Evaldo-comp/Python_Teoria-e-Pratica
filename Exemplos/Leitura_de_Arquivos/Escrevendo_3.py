"""
Abrindo, lendo e fechando um arquivo

Fonte: Nilo 3 ed
"""


arquivo = open("números.txt",  "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
