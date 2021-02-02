# Esses operadores lçógicos podem ser separados em dois tipos
#Unarios not e
#binário  not and is

sexo = input("insira seu sexo")
idade = int(input("insisra sua idade"))

if (sexo == "masculino" and idade >=18):
    print("você está apto a se inscriver para as formças armadas")
elif(sexo == "masculino" and idade <18):
    print("Você ainda não se alistar, volte quando tiver mais 18 anos")
elif(sexo == "feminino" and idade>=18):
    print("Apenas homens podem se alistar para o serviço militar obrigatorio")
else:
    print("Resposta inesperada, digite masculino para sexo masculino e feminino apra sexo feminino")

print(not True)
print(not False)