# O elif é a junção do else + if

#Exemplo01
numero = int(input("Insira um número\n"))

if numero % 2 == 0: #teste
    print("o número que você inseriu é par")
elif numero % 2 != 0:
    print("O numero inserido é impar")


#Exemplo02
idade = int(input("Insira sua idade\n"))
if idade >= 18:
        print("você é maior de idade")
elif idade <=10:
    print("você é uma criança")
elif(idade <=18):
    print("Você é adolecente")
elif(idade >18 and idade < 50):
    print("Você é adulto")
else:
    print("Você é idoso")