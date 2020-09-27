### STRINGS: <br/>
Em Python as strings são imutáveis, dessa forma se quisermos acessar, manipular itens individuais dentro de uma string, antes teremos que convertê-la em uma lista, essa conversão pode ser feita facilmente como mostrado abaixo:<br/>

```L = list(“Isso é uma string”) # a string foi convertida para lista atravésa da função list()```
Para fazer o caminho inverso, ou seja transformar uma lista em uma string basta utilizar o método ```.join()```.

```python

L = ['I', 's', 's', 'o', ' ' , 'é', ' ',  'u', 'm', ' a', ' ','s', 't', 'r', 'i', 'n', 'g']
s = " ".join(L)
```
#### Verificação parcial de uma string:

Podemos verificar com qual caractere começa ou termina uma string, utilizando os métodos ```startswith()``` e ```endswith()```:
```python
S = “Alô Mundo”
S.startswith(“Alô”) # Retorna true se a string começa com o argumento passado
S.endswith(“Mundo”) # Retorna true se a string termina com o argumento passado e False se a string terminar de forma diferente
```
<b>Importante:</b> *Os métodos startswith e endswith consideram letras maiusculas e minusculas para isso é interessante utilizar os métodos lower e upper*

```python
string.lower() # retorna uma string com todas as letras minúsculas
string.upper() # retorna uma string com todas letras maiúsculas
```
Outra forma de verificar a ocorrência de determinado elemento dentro de uma string é utilizando operador ```in```, para comparar duas strings, se o objeto da esquerda estiver na string da direita, então será retornado true, caso contrário será retornado false.
```python
s = " Meu nome é Evaldo"
"Evaldo" in s # retorna true
```
A mesma lógica do operador anterior pode ser utilizada para verificar a não existência de um elemento em uma string, neste caso utiliza-se ```not in```.

#### Contagem:

Além de verificar a ocorrência de um item dentro de uma string, pode ser necessaŕio que você precise obter o número de vezes que este item ocorre, para isso temos o método count():
```python

s= "O rato roeu a roupa do rei de Roma"
s.count("r") # retorna um inteiro que representa a quantidade de vezes que r ocorre dentro da string
```
#### Pesquisa:

A pesquisa procura um caractere ou um trecho dentro de uma string e retorna o índice onde  ele se localiza, essa busca é feita com o método ```find()```:
```python

s= "Maranguape"
s.find("ran") # Retorna o número 2, pois é no índice 2 que inicia o trecho passado como argumento
```
<b>Importante:</b> *No caso do argumento não ser encontrado o valor retornado será -1*.

O método ```find()``` possui uma variação, o método ```rfind()``` que faz uma busca por uma ocorrência mais a direita.
```python

s = " eu sou seu pai"
s.rfind("s") # retorna  7
s.find("s") # retorna 3

```
Os métodos ```find()``` e ```rfind()```, suportam dois argumentos adicionais além do valor a ser buscado, o segundo argumento é o índice onde a busca deve iniciar e o terceiro é o incie onde a busca deve terminar.
```python

s = "Me dê sua força pegazuuuuuu"
s.find("u", 3, 8) #busca o caractere u entre os índices 3 e 8

```

<b>Importante</b>: No caso de não ser passado o  valor de início e o valor de fim, o único valor passado será considerado como o início do corte e a linguagem irá considerar o fim como o último índice da string.

A linguagem Python possui dois métodos semelhantes ao dois que foram trabalhados anteriormentes, é ```index``` e ```rindex```, a diferença que estes quando não encontram o item buscando retornam um erro.






