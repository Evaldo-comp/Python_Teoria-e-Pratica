#Uma variavel pode ser retoernada em em em alguma parte do programa dependendo de onde ela foi declarada
#sendo assim, ela pode assumir basicamente dois tipos de amplitude
#Variável Global: Pode ser chamada em TODO o programa
#Variável local: Só pode ser utilizada dentro do bloco onde foi declarada

v1 = 2
for i in range(10):
    vinterna =+ i
    print(vinterna)


print("Varivel declarada antes do bloco for", v1)
print(vinterna)