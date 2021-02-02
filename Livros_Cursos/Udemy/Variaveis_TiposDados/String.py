#Strings podem ser representadas entre aspas simples ou aspas duplas
nome1 = "Edson"
nome2 = 'Pedro'
print(nome1,nome2)

#Pulando linha método 01 -  \n
texto = "Ele realmente não sabia o que fazer\n naqeula situação"
print(texto)

#Pulando linha método 02 - Tripla aspas duplas
texto = """Ele realmente não sabia o que fazer
 naqeula situação"""
print(texto)

#upper - Colocando toda a string em caixa alta
print(nome1.upper())

#lower - Colocando toda a string em caixa baixa
print(nome1.lower())
#Transformando um string composto em lista
frase = "Essa é uma string"
print(frase.split())        #por definição ela quebra astring nos espaços
frase2 = "O rato roeu a roupa do rei de Roma"
print(frase2.split('r'))    #Corta a string onde ocoorre o r

#Invertendo uma string
print(frase)
print("Frase invertida")
print(frase[::-1])  #começa do primeiro elemento, vai até o último e inverte

#trocando caracteres dentro de uma strinh
str = "Ele é alto"
print(str.replace('e', 'a'))
