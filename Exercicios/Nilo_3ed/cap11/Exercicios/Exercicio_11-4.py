"""
    Modifique o programa do Exercicio 11.3 de forma a perguntar dosi valores e listar os produtos com
    preços entre esses dois valores
"""

import sqlite3
from contextlib import closing

valor1 = input("Informe o primeiro valor: ")
valor2 = input("Informe o segundo valor: ")
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f'select * from precos where preco >= ? ' , (valor1,))
        cursor.execute(f'select * from precos where  preco < ?' , (valor2,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada Encontrado.")
           
                
                break
            print(f"Preço do {resultado[0]} R$: {resultado[1]}")   
            x +=1
