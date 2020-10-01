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
______

#### Contagem:

Além de verificar a ocorrência de um item dentro de uma string, pode ser necessaŕio que você precise obter o número de vezes que este item ocorre, para isso temos o método count():
```python

s= "O rato roeu a roupa do rei de Roma"
s.count("r") # retorna um inteiro que representa a quantidade de vezes que r ocorre dentro da string
```

______


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

______

#### Posicionamento de strings:

Existe um método que centraliza  a string dentro de um número de posições passados como parâmetro neste método, veja como funciona;
```python
s = "Palmeiras"
s.center(10) # posiciona a string dentro de uma total de 0 espaços
s.center(10, ".") # Aqui é passado um argumento a mais, esse argumento irá substituir os espaços em branco 
s.ljust(5, ".") # o ljust não centraliza, mas completa à esquerda com o caractere passado como parâmetro
s.rjust(5, "#") # Funciona igual ao ljust, mas completa à direita
```

______

#### Quebra ou separação de string:

Uma string pode ser quebrada, na ocorrência de determinado item, depende do parâmetro passado para o método ```split()``` que por padrão quebra a string nos espaços

<b>Importante:</b> O caractere utilizado para dividir a string não é retornado, ou seja ele é perdido na divisão.
```python
s = “Não gosto muito de me separar”
s.split()
saida: [‘nao’, ‘gosto’,’muito’, ‘de’, ‘me’, ‘separar’]
```

______

#### Substituição de Strings:

Podemos substituir determinada ocorrência de uma string por outra, para isso devemos utilizar o método ```replace()```, que leva dois parâmetros, o primeiro é o elemento da string a ser substituído e o segundo o elemento que substituirá o primeiro.
```python
clubes = “Palmeiras, São paulo, Palmeiras, Flamengo, Cruzeiro”
clubes.replace(“Palmeiras”, “Campeão”)
o elemento “Palmeiras” será substituído dentro da strong pela palavra “Campeão”
```
Ainda é possível adicionar um terceiro parâmetro que indicará a quantidade de vezes que desejamos realizar a repetição.


______

#### Remoção de Espaços em Branco:

Algumas vezes podem sobrar espaços em strings inseridas pelo usuário ou até mesmo pelo programador, esses espaços podem não significar nada,  mas na comparação de uma chave de acesso por exemplo, pode causar algum conflito, por isso é importante deixarmos a string limpa sem espaços além do previsto, este caso utilizamos o método ```strip()``` e suas variações ```lstrip()``` e ```rstrip()```.

```python
t = “   olá   “
t.strip() # remove espaços extras do início e fim da string
“olá” #saída
t.lstrip() # remove espaços apenas da esquerda
“olá    “ #saida
t.rstrip()# remove espaços apenas da direita
“   olá”  saída
```

<b>Importante:</b> Se algum parâmetro for passado para strip e suas variações, o método entenderá que esse parâmetro será o caractere a remover e não os espaços.

_______

#### Validação de string por tipo de conteúdo:

Alguns métodos servem para fazer validação de strings, verificar o tipo de conteúdo inserido nessa string, algo bastante útil na validação de senhas.</br>

<b>isalnum():</b><br/>
Esse Método retorna verdadeiro se a string não estiver vazia e os seus caracteres forem letras e/ou números, no caso da string conter  espaços, vírgula, exclamação e etc, ele retornará false.
```python
s= “aí dento!”
s.isalnum() # irá retornar false
p = “arriegra”
p.isalnum() # irá retornar true 
```

<b>isalpha():</b><br/> 
É um método de validação mais restritivo , ele irá retornar true apenas se a string não estiver vazia e se todos os caracteres forem letras, caso contenha qualquer outro tipo , irá retornar false.
```python
s = “R2D2”
s.isalpha() # irá retornar false pois contêm números
p = “pegubeco”
p.isalpha() # irá retornar true
```

<b>isdigit():</b><br/> 
Retorna true se a string nao estiver vazia e todo os caracteres forem números, caso contrário retorna false.
```python
s = “2020”
s.isdigit() # retorna true
p = “+12”
p.isdigit() # retorna false
```

<b>isupper() - islower():</b><br/>
Verificam se todos os caracteres são maiusculos ou minusculos, respectivamente.
```python
s = “sossega”
s.islower() # retorna true
s.isupper() # retorna false
```
<b>isspace():</b><br/>
Verifica se a string contém apenas caracteres em branco como espaço, tab e etc.
```python
a = “\t\n\r    “
a.isspace() # retorna true
```
<b>isprintable():</b><br/>
Verifica se alguma string irá causar algum erro ou conflito ao ser mostrada no terminal,  retorna true caso tudo seja printado sem problemas, ou false caso haja algum conflito.
```python
“\t\n\t”.isprintable() # retorna false
“Olá Mundo”.isprintable() # retorna True
```

______


#### Formatação de strings:

##### O método format:

Neste método podemos substituir os valores por números dentro de chaves, os números são equivalentes a ordem em que os parâmetros que eles representam são invocados dentro do método.
```python
“{0} {1} {2}”.format(“Alô”, “Mundo”, “!”)
```
É possível especificar a largura de um valor:
```python
“{0:10} {1}”.format(“123”, “234”) # o primeiro número antes dos dois pontos é a posição do parâmetro, o segundo número é o tamanho que esse valor irá ocular na #impressão
‘123          234’  # saída
```
É possível especificar se queremos espaços adicionais a esquerda ou a direita do valor bastando para isso a inclusão dos símbolos > e < depois dos dois pontos.
```python
“{0:<10}”.format(“000”)
“000    “ # adicionou espaços extras a direita

“{0:>10}”.format(“000”)
“       000 “ # adicionou espaços extras a esquerda
```

Para centralizarmos o valor entre os espaços devemos utilizar<b>^</b>:

```python
“{0:^10}”.format(“000”)
“    000    “ # centralizado
```

Se ao invés de espaços, quisermos preencher com outro caractere, basta especificarmos depois dos dois pontos.
```python
“{0:$<10}”.format(“000”)
“000$$$$  “ # adicionou $  à direita
```

#### Formatação de números:

Se especificarmos a direita dos dois pontos de  um número, ele será interpretado como a quantidade de algarismos. O número a esquerda será o algarismo utilizado para preencher caso o valor em si não ocupe a quantidade de algarismo solicitado.
```python
“{0:03}”.format(2) #número com 3 algarismos preenchidos com 0
‘002’ #saída
```

Podemos ao invés de preencher com 0, utilizar outros caracteres, mas para isso devemos colocá-lo à esquerda do símbolo de igualdade. 
```python
“{0:*=8}”.format(12) # preenche 6 espaços com *
‘******12’ #saída
```

O alinhamento dos números também pode ser espeocificado utilizando <b>< ></b>  e <b>^</b>.

```python
# Centralizado
“{0:*^8}”.format(12) # preenche 6 espaços com 
‘****12****’ # saída
  
# À esquerda
“{0:*<8}”.format(12) # preenche 6 espaços com 
‘12********’ # saída

# À direita
“{0:*>8}”.format(12) # preenche 6 espaços com 
‘12********’ #saída

```

Podemos solicitar a vírgula para conseguir um agrupamento por milhar:
```python
“{0:10}”.format(1234)
“      1,234’ #saida
```

ou ainda o ponto para controlar a precisão de casas decimais:
```python
“{0:10.5f}”.format(1500.31)
‘1500.310001 #saída
```

Por último se fizermos as devidas substituições, é possível imprimir um determinado número em sistemas de numeração diferente
```python
“{:b}”.format(10)# imprime o número 10 em binários ou seja na base 2
“{:c}”.format(10)# imprime o número 10 em seu equivalente ‘char’ de acordo com a tabela ASCII
“{:o}”.format(10)# imprime o número 10 octal
```
______

:house:[HOME](https://github.com/Evaldo-comp/Python_Teoria-e-Pratica)







