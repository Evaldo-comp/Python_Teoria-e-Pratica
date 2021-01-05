# Consulta, registro por registro
import sqlite3
conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute("select * from precos")
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    print(f"Nome do produto: {resultado[0]}\nPreço:R$ {resultado[1]}")
cursor.close()
conexao.close()