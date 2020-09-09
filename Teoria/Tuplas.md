### TUPLAS
As tuplas são imutáveis, por isso são indicadas para trabalhar com valores constantes, como por exemplo, dias da semana, meses do ano e etc.
Para criar uma tupla utilizamos parênteses, apesar dos parênteses serem opcionais,sua utilização é indicada para facilitar a leitura.
```python
Cavaleiros = (Seya, Yoga, Shun, Shiriu, Ikki)
```
As tuplas são imutáveis, ou seja, não podem ter seus elementos alterados, não cabendo então na tupla ```Cavaleiros de Bronze``` trocar o *Seiya* por *Aldebaran*.</br> 
:pencil2: *OBS: Se a tupla tiver apenas um elemento, a sua estrutura deve ser a a seguinte:*
```python
Presidente odiado pelas Emas =(Bolsonaro,) # elemento único, dentro de parênteses e uma vírgula
```
Podemos transformar uma lista em tupla através do comando ```tuple```.
```python
Lista = [1, 2, 3, 4]
Tupla = tuple(Lista) # uma tupla é criada a partir de uma lista
```
Tuplas permitem concatenação, ou seja a junção de uma mais tuplas .
```python
t1= (Seya)
t2=(Saori)
seyore = t1 + t2 # desculpem por isso :)
```
#### Utilizando tupla para desempacotar

Quando vamos desempacotar vários elementos em uma lista, o asterisco na primeira variável vai receber todos os elementos menos o último.
```python

# neste caso o primeiro item com asterisco recebe os 5 primeiros elementos da lista, deixando o último para o item sem asterisco
*Cavaleiros de Bronze, Cavaleiro de Ouro = [Seya, Hyoga, Ikki, Shun, Shiryu, Mu]
Cavaleiros de Bronze =  [Seya, Hyoga, Ikki, Shun, Shiryu]
Cavaleiros de Ouro = [Mu]

# Aqui acontece a mesma coisa do código anterior
Cavaleiros de Bronze, Cavaleiros de Ouro* = [Seya, Mu, Saga, Camus]
Cavaleiros de Bronze = [Seiya]
Cavaleiros de Ouro = [Seya, Mu, Saga, Camus]
```

A variável sem o asterisco * recebe apenas um valor, já a variável com asterisco recebe todos os demais, se existirem duas variáveis sem asteriscos, elas recebem cada qual um valor nas suas posições, o restante sobra para a variável com asterisco. Vamos entender como funciona com os cavaleiros
```python
Ouro, Bronze*, Prata = [Camus, Seiya, Hyoga, Mouses de Baleia]
Ouro = [Camus]
Bronze = [Seiya, Hyoga]
Prata = [Mouses de Baleia]
```

:house:[HOUSE](https://github.com/Evaldo-comp/Python_Teoria-e-Pratica/blob/master/README.md)







