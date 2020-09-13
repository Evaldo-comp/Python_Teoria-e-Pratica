"""
Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida.
Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa
em estoque
"""

estoque = {
            "tomate": [100, 2.30],
            "alface": [100, 2.30],
            "batata": [100, 2.30],
            "feijão": [100, 2.30],
}
print(estoque)
venda = []
# Trecho que coleta a lista de produtos do usuário e verifica a existência no estoque
while True:
    produto = input("Digite o nome do produto ou exit para sair")
    if produto.lower()=='exit':
        break
    if produto in estoque.keys():
        quantidade = int(input("Digite a quantidade que deseja "))
        venda.append([produto, quantidade])
    else:
        print("Produto indisponível no estoque")

print(venda)
#venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas\n")

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: {total:21.2f}\n')
print("Estoque: \n")
for chave, dados in estoque.items():
    print(f"Descrição: ", chave)
    print(f"Quantidade: ", dados[0])
    print(f"Preço: , {dados[1]:6.2f}\n")
