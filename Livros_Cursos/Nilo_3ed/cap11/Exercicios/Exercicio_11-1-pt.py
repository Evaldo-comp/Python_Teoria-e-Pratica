# Criando a tabela

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                create table precos(
                    nome text,
                    preco double)
                ''')