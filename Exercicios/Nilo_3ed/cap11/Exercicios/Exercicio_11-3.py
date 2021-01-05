# Consulta utilizando parâmetros

import sqlite3
from contextlib import closing


"""
    Escreva um programa que realize consultas no banco de dados preços. O programa deve perguntar o nome
    do produto  elistar seu preço
"""

nome = input("Qual o nome do produto: ")
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f'select * from precos where nome = ?' , (nome,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada Encontrado.")
                break
            print(f"Preço do {resultado[0]} R$: {resultado[1]}")
            x +=1
