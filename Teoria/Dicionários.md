
### Dicionários:
O dicionário consiste em uma combinação de chave e valor, cada elemento de um dicionário segue esta combinação e são organizados dentro de chaves diferente das listas que utilizam colchetes.

#### Estrutura = ```{“Chave”: valor, “Chave”: valor}```

Ao associar um valor a uma chave, se essa chave já existir o valor será substituído, se a chave não existir uma nova chave será criada.</br>
```python
dicionário[“chave existente”] = novo valor
dicionário [chave não existente] = novo valor ] # uma nova chave se
```

É possível extrair de discionários apenas chaves ou apenas valores, ambos em forma de listas.
```python
dic.keys() # obtém uma lista com as chaves do dicionário

dic.values() # obtém uma lista com os valores do dicionário
```
Uma chave do dicionário pode ser apagada utilizando o comando ```dell```.
```python
del dic [“chave”]
```
:pencil2: *OBS: Ao utilizar f’strings as aspas “ duplas internas das chaves são substituídas por aspas simples.*

#### Dicionário com lista:
uma chave de um dicionário pode ser associado a uma lista ou mesmo a outro dicionário.

##### Exemplo:
```python
Ingrediente = {
        “Suco”: [“Fruta”, “Açúcar”, “Água”]
        “Arroz”:[“Arroz”, “Água”, “Sal”]
        “Feijão”: [“Feijão”, “Sal”, “Água”]
}.
```

:house:[HOME]()









