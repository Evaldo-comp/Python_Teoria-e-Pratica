### LISTAS

A lista é um tipo de variável que permite o armazenamento de vários valores em uma única estrutura , os dados armazenados em uma lista podem 
ser de tipos diversos, ou seja ela suporta *inteiros , strings, floats* e etc.

#### Declaração de uma lista vazia
```python
l = [ ]  #Os elementos de uma lista ficam armazenados entre colchetes separados por vírgula
```

#### Declaração de uma lista com três inteiros
```python
lista = [1, 2, 3]
```

:pencil2: *Os elementos de uma lista são organizados e buscados dentro de um programa levando em consideração o seu índice, que começa por 0, caso queira trocar determinado valor dentro da lista, ou invocá-lo, basta utilizar o índice ao qual você deseja realizar a instrução*

#### Trocando o valor do índice 3 de uma lista
```python
lista[2]= 5   #O índice 2 irá valer  5
```

#### Fatiamento de lista:

Pode ser necessário que em algum momento, você não precise utilizar a lista inteira, mas apenas algum trecho dela, 
um intervalo específico, para utilizarmos apenas um determinado intervalo dentro de uma lista, nós podemos fatiá-la, 
indicando o índice de corte inicial e índice de corte final

##### Exemplo: 
```python
print(lista10[1:])    # Imprime do índice 1 até o final
print(lista10[::])    # Imprime todos os elementos
print(lista10[-1:])   # Imprime apenas o último elemento
print(lista10[:4])    # Imprime do índice 0 ao índice 4
print(lista10[2 :4])  # Imprime do índice 2 ao índice 4
print(lista10[1::2])  # Imprime todos os elementos do índice 1 de dois em dois
print(lista10[::2])   # Imprime todos os elementos do início ao fim de dois em dois
```
#### Tamanho de Uma Lista

Para sabermos qual o tamanho da lista basta utilizarmos a função ```len()```.

##### Exemplo:
```python
semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta','Sábado', 'Domingo']
print(len(semana))  #imprime o tamanho da lista
```
#### Adicionando elementos à lista:

Para adicionarmos elementos em uma lista utilizamos um método. Importante notarmos a diferença de função e método. </br>

**função** é chamada e leva como parâmetro o objeto ao qual queremos aplicar alguma instrução. </br>
```
len(objeto)
```
**Métodos** são escritos após o nome do objeto separados por ponto.</br>
 ```
 objeto.append(elemento)
```
##### Exemplo de Adição:
```python
lista =[]
lista.append("A")  # Adiciona a letra A à lista
```
:pencil2: *Outra forma de adicionar elementos em uma lista, é acrescentando listas na lista através do operando +*

#### Exemplo de adição com operando 
```python
lista = []
lista = lista + [1, 2] #adiciona 1 e 2 a lista
# podemos utilizar outra estrutura mais simples
lista += [1, 2]
```
:pencil2: *OBS: Se você utilizar uma lista como parâmetro do método **append**, ele irá adicionar uma lista dentro da outra, por isso é indicado utilizar o exemplo anterior **+ =** pois esta forma invoca o método **extend()** este método inclui uma lista dentro de outra mas como elementos independentes.*

#### Remoção de Elementos:
Assim como é possível adicionar elementos em lista, também conseguimos removê-los, para isso utilizamos a instrução **del**.

##### Exemplo: 
```python
lista = [1, 2, 3, 4, 5]
del lista [índice que deseja remover]
#também é possível utilizar o del como fatias de lista : 
del lista [1: 10]
```
#### Utilizando listas como fila:
Em uma fila a inclusão é feita no fim e a exclusão é feita no início **(FIFO- First in first Out)**.
```
lista.apend(último)  # Insere um elemento no fim da fila
lista.pop(0)  # O método pop(0)não só retira um elemento de uma lista como também retorna o mesmo.
```
##### Exemplo:
```python
ultimo = 10
fila = list(range(1, ultimo+1))
listop =[]
i = None
while True:
   print(f"\n Existem{len(fila)} clientes na fila")
   print(f"Fila atual: {fila}")
   print("Digite F para adicionar um cliente ao fim da fila")
   print("ou A para realizar o atendimento. S para sair")
   operacao = input("Digite a sequência de comandos desejados (F, A, S)\n")
   listop = list(operacao)

   for i in listop:

       if i == "A":
           if len(fila)>0:
               atendido = fila.pop()
               print(f"Cliente {atendido} atendido")
           else:
               print("Fila vazia! Ninguém para atender.")
       elif i == "F":
           ultimo += 1
           fila.append(ultimo)
       elif i == "S":
           break
       else:
           print("operação inválida! Digite apenas F, A ou S")
  ```
#### Utilizando listas como pilhas:
A estrutura é bem parecida de quando trabalhamos com filas, a diferença é o elemento que é passado para o método ```pop()```. Na fila o primeiro a entrar é o último a sair, já na pilha o último a entrar é o primeiro a sair, sendo assim o método ```pop()``` leva o parâmetro -1, para indicar  o elemento que vai ser excluído é o último elemento a entrar.

#### Pesquisando itens em uma lista.
Podemos percorrer uma lista para tentar encontrar um elemento determinado pelo programador, ou pelo próprio usuário, para isso utilizamos o laço while.

##### Exemplo de busca:
```python

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
 ```
#### Pesquisando uma lista com ```FOR```.
A pesquisa acima foi realizada utilizando um ```while```, mas o Python oferece uma estrutura especial para percorrer listas, o ```for```, a diferença é que  o ```for``` é indicado quando se sabe a quantidade que se deseja percorrer. O ```while``` é indicado quando o tamanho da lista é incerto e o índice a ser manipulado ainda é desconhecido, segue abaixo o exemplo de uma pesquisa utilizando um ```for```.

##### Exemplo:
```python
L = [7, 9, 10, 12]
p = int(input("Digite um número para pesquisar"))

for e in L:
   if e == p:
       print('Elemento encontrado')
       break
   else:
       print("elemento não encontrado")
       
  ```
#### Range()
A função range permite que possamos criar uma sequência de números dentro de um intervalo pré-determinado, esta função pode levar 1, 2 ou 3 parâmetros.

- **range(10):** Gera uma sequência de 0 a 9, o fim do intervalo é excluído
- **range(2, 12):** Gera uma sequência de 2 a 11
- **range(2, 12, 2):** Gera uma sequência de 2 a 11 de dois em dois

:pencil2: *É importante lembrar que a sequência gerada pelo range não é uma lista, e sim um objeto. Para transformar esta sequência em uma lista precisamos utilizar a função ```list```*

##### Convertendo um range em uma lista:
```python
l = list(range(100, 1000, 10))
print(l)
```
#### Enumerate:
A função ```enumerate``` gera uma tupla de dois elementos, onde o primeiro  é o índice de uma lista e o segundo é o valor deste índice. A eficiência desta função é melhor aproveitada quando utilizado junto ao ```for```, a cada giro do ```for```, os elementos da tupla gerada são modificados pelos índices e valores subsequentes.

##### Exemplo:
```python
L = [5, 9, 13]
for x, e in enumerate(L):
    print(f'[{x}] {e}')
 ```
#### Ordenação utilizando Método Bolha:

Existem vários algoritmos para ordenar listas, um dos mais simples é o método bolha, não indicado para listas muito grandes, ele consiste basicamente em comparar dois elementos por vez, se o valor do primeiro for maior do que o valor do segundo eles trocam de posição dentro da lista e assim sucessivamente até que a lista esteja ordenada.

##### Exemplo:
```python
L = [7, 4, 3, 12, 8]
fim = len(L) # indica a quantidade de elementos da lista
while fim > 1:
   trocou = False
   x = 0
   while x <(fim-1):
       if L[x] > L[x + 1]:
           trocou = True
           temp = L[x]
           L[x] = L[x+1]
           L[x + 1] = temp
       x+=1
   if not trocou:
       break
   fim -=1
for e in L:
   print(e)
```

:pencil2: *O Python possui dois métodos que fazem essa ordenação de forma instantânea mas com algumas particularidades.*</br>
- **sort():** Ordena um alista modificando sua estrutura
- **sorted():** Ordena sem alterar a lista original

:house: [HOME]()










