"""
Apesar de visualmente se assemelhar com uma list comprehensions, o generator
possui algumas especifidades

Links úteis:
http://pythonclub.com.br/python-generators.html
https://pythonacademy.com.br/blog/iterators-e-generators-em-python
https://www.learnpython.org/en/Generators

"""
nomes = ['José', 'Carlos', 'Ana', 'Joana', 'Costa']

print(any(nome[0] == 'C' for nome in nomes))

#List comprehension
res = [nome[0]=="C" for nome in nomes]
print(res)

#Generator
res = (nome[0] == 'C' for nome in nomes)
print(res)

#Teste de desenpenho do generator

# Essa biblioteca permite utilizar um método que pega a quantidade de bytes de determinado parâmentro
from sys import getsizeof

# Gerando uma lista com list Comprehension
list_com = getsizeof([x ** 2 for x in range(10)])

# Gerando uma lista com Set Comprehension
set_com = getsizeof({x ** 2 for x in range(10)})

# Gerando uma lista com Dictionary Comprehension
dic_com = getsizeof({x: x ** 2 for x in range(10)})

# Gerando uma lista com Generator
gen = getsizeof(x ** 2 for x in range(10))

print('Para realizar a mesma tarefa é gasto de memória :')
print(f'List Comprehension: {list_com} bytes')
print(f'Set Comprehension: {set_com} bytes')
print(f'Dictionary Comprehension: {dic_com} bytes')
print(f'Generator: {gen} bytes')
