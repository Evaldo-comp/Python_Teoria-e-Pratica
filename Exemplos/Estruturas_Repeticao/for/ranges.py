#diferentes formas de utiliza o range

#Método 01 = Passando apenas um valor, Começa com o valor default 0

for i in range(10):
    print(i, end = ' ')
print(' ')
# Método 02 = Passando o valor de inicio e fim do range
for i in range(1, 10):
    print(i, end = ' ')
print(' ')
# Método 03 = Passando o valor de inicio de fim e intervalo do range
for i in range(1, 10, 2):
    print(i, end = ' ')
print(' ')
# Método 04 = Passando o valor de inicio de fim e intervalo do range(Regressivo)
for i in range(10, 1, -2):
    print(i, end = ' ')