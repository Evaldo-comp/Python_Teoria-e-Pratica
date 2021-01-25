# Pratique o uso do interpretador do Python como uma calculadora

""" 2. Suponha que o preço de capa de um livro seja R$ 24.95, mas as livrarias
recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro
exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total
de atacado para 60 copias?"""

preco_com_desconto = 24.95 - (24.95 * 0.4)
frete = (59 * 0.75) + 3.00
custo_total = (preco_com_desconto * 60) + frete 
print(f"O preço total para 60 cópias é de R$ {custo_total:.2f} Reais")
