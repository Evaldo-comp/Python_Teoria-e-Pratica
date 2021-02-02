"""
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar

"""

# Solução
preco = float(input("Digite o valor da mercadoria"))
porce = float(input('Agora insira quanto é o desconto sobre essa mercadoria'))

precoAtual = preco - (preco * porce/100)
desc = preco - precoAtual

print(f'O valor do desconto aplicado foi de R${desc:.2f} Reais')
print(f'O preço a pagar é de: R${precoAtual} Reais')