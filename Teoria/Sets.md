### Conjuntos

Os conjuntos em python realizam operações de união, intersecção e diferença, entre outras, igualmente os conjuntos em matemática, em python eles não aceitam repetições e não matem a ordem de seus elementos.

##### Exemplo de adição de itens em um conjunto:
```python
a = set()
a.add(Banana)
a.add(Jaca)
a.add(Banana)
saída {Banana, Jaca}
```
Um conjunto pode ser criado a partir de uma lista como pdemos observar abaixo:
```python
a = set([1, 2, 3])
{1, 2, 3}
```
#### Vamos emeteder como realizar operações báśicas com Conjuntos:

##### Diferença entre Conjuntos
```python
set1={0,1, 2, 3, 4}
set2= {2, 3, 4,5}
print(set1  - set2) # imprime os ementos que estão em set1 e não estão em set2
{1} # saída
```


##### União entre conjuntos:
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1| set2) # Iprime os intens que estão em set1 e em set2
{1, 2, 3, 4, 5,6} # saída
```
##### A união também pode ser realizada através do método union():
```python
set1 = {1, 2 3,4}
set2{5, 6, 7}
set3 = set1.union(set2)
```
##### Utilizando o método upade para juntas dois conjuntos
```python
set1 = {1, 2 3,4}
set2{5, 6, 7}
set1.update(set2) # Observe que aqui não é retornada a unição dos dois conjuntos, mas um conjunto é inserido em outro
```

______

:gift: Conteúdo adicional:
[W3schools](https://www.w3schools.com/python/python_sets.asp)


:house: [Home](https://github.com/Evaldo-comp/Python_Teoria-e-Pratica)
