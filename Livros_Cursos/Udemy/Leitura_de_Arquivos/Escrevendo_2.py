"""
Escrevendo em um arquivo utilizando um for

Fonte: Nilo 3 ed
"""

arquivo = open("números.txt", "w")
for linha in range(1, 101):
    arquivo.write(f"{linha}\n")
arquivo.close()-
