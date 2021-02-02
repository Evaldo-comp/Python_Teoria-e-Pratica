estoque = {
            "tomate": [100, 2.30],
            "alface": [100, 2.30],
            "batata": [100, 2.30],
            "feijão": [100, 2.30],
}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
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
