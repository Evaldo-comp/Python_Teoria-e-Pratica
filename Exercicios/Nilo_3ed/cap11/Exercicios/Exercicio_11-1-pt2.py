# inserindo dados na tabela

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                insert into precos(nome, preco)
                    values(?, ? )
                    ''', ("Carne", 23.00) )