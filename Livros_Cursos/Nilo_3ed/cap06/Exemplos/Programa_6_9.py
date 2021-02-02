
nome = ['Evaldo', 'Ana', 'Pedro', 'José', 'Maria']

p = input('Digite seu nome')
achou = False
x = 0
while x < len(nome): # Percorre a lista
    if nome[x] == p:  # verifica se o elemento da lista é igual ao nome inserido
        achou = True  # Retorna true caso verdade
        break
    x+=1
if achou: # Trecho que imprime os resultados
    print(f'{p} encontrado na posição {x}')
else:
    print(f'{p} não encontrado')