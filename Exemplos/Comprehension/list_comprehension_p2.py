# Utilizando condicionais lógicas

numeros = [1,2,3,4,5,6,7,8,9,0]

pares = [numero for numero in numeros if numero %2 ==0]
print(pares)

impares = [numero for numero in numeros if numero %2 !=0]
print(impares)

# Outra forma
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if  numero % 2]

print(pares)
print(impares)
