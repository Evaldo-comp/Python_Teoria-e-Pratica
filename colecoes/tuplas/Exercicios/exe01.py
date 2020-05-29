"""Exercício01 - Crie uma tupla e imprima o que se pede :"""
tupla = (1, 3, 4, 5, 6, 7)
# 1- Apenas o primeiro item
print(f'O primeiro item da tupla é: {tupla[0]}')

# 2- O número de ítens da tupla
print(f'A tupla tem {len(tupla)} itens')

# 3 - Utilize o slice negativo para imprimir o último intem da tupla
print(f'O último item da tupla é  {(tupla[-1:])} ')

# 3 - Utilize o slice para imprimir do 2 ao ultimo item
print(f'O intervalo que corresponde do segundo ao último item é   {(tupla[1:])} ')



