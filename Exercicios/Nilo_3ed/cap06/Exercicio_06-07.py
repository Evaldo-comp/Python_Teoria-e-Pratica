expressao = input("Insira a expressão apenas com parẽnteses")
contador = 0
pilha =[]
while contador < len(expressao): #Cria um laço para percorrer a expressão
    if expressao[contador] == "(":
        pilha.append('(') # Adiciona ( a pilha
    if expressao[contador] == ")":
        if len(pilha) > 0:  # Verifica se a pilha está vazia
            pilha.pop(-1)   # pilha não está vazia, sendo assim retira-se o elemento do topo
        else:
            pilha.append(")") # pilha vazia, então occorrreu um erro pois o elemento ) veio sem um (
            break
    contador+=1

if len(pilha) == 0:
    print('OK')
else:
    print('Erro')


