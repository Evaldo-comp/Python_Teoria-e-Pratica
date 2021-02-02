"""
    Modifique o programa do Exercicio 11.3 de forma a perguntar dosi valores e listar os produtos com
    preços entre esses dois valores
"""

# Consulta, registro por registro
import sqlite3
conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute("""update   precos
                    set  telefone = (telefone+ 0.2)""")

cursor.close()
conexao.close()
