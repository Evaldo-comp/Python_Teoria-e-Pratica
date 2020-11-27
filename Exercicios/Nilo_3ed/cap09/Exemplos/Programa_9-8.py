# Geração de uma página web a partir de um dicionário

# dicionários para organizar os filmes
filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Dificil de Matar"],
    "guerra": ["Rambo", "Platoon", "O Resgate do soldado Ryan"]
}

# Cria a estrutura básica da página web
with open("filmes.html", "w", encoding="utf-8") as pagina2:
    pagina2.write
    ("""
    <DOCTYPE html>
    <html lang ="pt-br">
        <head>
            <meta charset = "utf-8">
            <title>Filmes</title>
        </head>
        <body>
    </html>
    """)

    # for para adicionar os filmes percorrendo o dicionário
    for c, v in filmes.items():
        pagina2.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina2.write(f"<h2>{e}</h2>\n")
    pagina2.write("</body></html>")
