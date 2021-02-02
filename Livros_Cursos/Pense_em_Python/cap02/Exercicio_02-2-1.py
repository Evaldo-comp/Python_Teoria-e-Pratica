# Pratique o uso do interpretador do Python como uma calculadora

# 1. O volume de uma esfera com raio r é de 4/3 pi r ^ 3. 
# Calcule o volume de uma esfera em que o raio é dado pelo usuário
# dica: 1 metro cúbico  = 1000 litros
raio = float(input("digite o valor do raio\n"))
volume = (4 * 3.14 * (raio ** 3))/3
print(f'{volume:.2f} metros cúbicos ou {volume * 1000:2.3f} litros')

# 2. 