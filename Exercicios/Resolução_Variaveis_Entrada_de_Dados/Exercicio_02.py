"""
Escreva uma expressão que será utilizada para decidir se uma aluno foi ou não aprovado.
Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
Considere que o aluno cursa apenas três matérias, e a quarta nota de cada uma está
armazenada nas seguintes variáveis:materia1, materia2, materia3
"""
materia1 = 4.7
materia2 = 5.8
materia3 = 1.5

media1 = (5.2 + 7.8 + 3.5 + materia1) / 4
media2 = (7.2 + 8.8 + 9.5 + materia2) / 4
media3 = (1.2 + 4.8 + 6.5 + materia3) / 4

print((media1 and media2 and media3) > 7)

#Fonte: Introdução à Programação com Python - Nilo Ney Coutinho- 3º ed
