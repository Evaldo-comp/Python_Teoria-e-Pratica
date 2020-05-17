#Recebendo dados do usuario

#entrada de dados
print("Qual o seu nome")
nome = input() #Entrada


#Exemplo de print antigo
#print("Seja bem vindo %s" %nome)

#formato moderno
#print('Seja bem vindo {0}'.format(nome))

#Formato mais atual
#print(f'Seja bem vindo{nome}')

print("qual a sua idade")
idade = int(input())



#Processamento
#int(idade) é um cast
#Cast é uma conversão de dados



#Saida de Dados
print("%s você tem %d anos" %(nome, idade))