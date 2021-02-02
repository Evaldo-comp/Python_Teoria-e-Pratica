"""
    Modifique o programa 9.8 para gerar uma lista html, usando os elementos ul e il
"""

# dicionários para organizar os itens
compras = {"Limpesa": ["Sabão em pó",  "Detergente", "Amaciante"],
           "Carnes": ["Frango", "Bisteca", "Fígado"],
           "Bebidas": ["Suco", "Cerveja", "Vinho"]
           }


# Cria a estrutura básica da página web
with open("compras.html", "w", encoding="utf-8") as listacompras:
    listacompras.write
    ("""
    <DOCTYPE html>
    <html lang ="pt-br">
        <head>
            <meta charset = "utf-8">
            <title>Lista de Compras</title>
        </head>
        <body>
        <h1>lista de Compras</h1>   
    </html>
    """)

    # for para dicionar os itens percorrendo o dicionário
    for c, v in compras.items():
        listacompras.write(f"<ul>{c}</ul>\n")
        for e in v:
            listacompras.write(f"<li> {e}</li>\n")
    listacompras.write("</body></html>")
