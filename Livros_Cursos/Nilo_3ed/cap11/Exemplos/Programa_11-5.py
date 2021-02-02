# Consulta utilizando parâmetros

import sqlite3
from contextlib import closing


nome = input("Nome  a buscar: ")
with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f'select * from agenda where nome = ?' , (nome,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada Encontrado.")
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            x +=1
