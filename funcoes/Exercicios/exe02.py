"""
Uma função pode receber mais de uma argumento, os parâmetros  podem ser classificados em
default, nomeados e etc. segue neste programa uma função com 3 parâmetros
"""

#Prática: cirie uma função que receba o numeros de vitórias, emaptes e derrotas de um time
# sendo que
# 1 - Vitória = 3 pts
# 2 - Empate =  1 pts
# 1 - Derrota = 0 pts

def pontos(wins, draws, losses):
	return wins*3 + draws

print(pontos(3,2,4))