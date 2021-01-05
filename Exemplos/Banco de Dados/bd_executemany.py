import sqlite3
dados = [("Pedro", "1111-2222"),
         ("Ana", "3333-3333"),
         ("José", "4444-5555")]
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.executemany('''
        insert into agenda(nome, telefone)
        values(?, ?)
        ''', dados)
conexao.commit()
cursor.close()
conexao.close()