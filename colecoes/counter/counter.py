# Recebe um iteravel como parâmetro e cria um objeto do tipo Collections Counter, parecido com
# um dicionário contendo como chave o o elemento da lista passada como parâmetro e  como valor a quantidade
# de ocorrências desse elemento
'''
from collections import Counter


lista =[1,1, 2 , 3, 4, 5, 5, 5, 4,4, 3, 3,54,6,76,8 ,8 ,6,4]

res = Counter(lista)
print(res)

# Imprimindo o Counter a a partir de uma string
from collections import Counter

print(Counter('Francisco Evaldo Pereira Mariano'))
'''

texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam convallis 
facilisis metus, et ornare tellus malesuada nec. Curabitur rhoncus augue turpis,
vitae placerat ligula aliquet id. Vestibulum tincidunt porta mi. Maecenas a arcu
eget nisi varius lobortis quis ac erat. Nunc metus eros, dictum ultricies suscipit
ut, tristique et mi. Nunc pulvinar felis nibh, in placerat nulla rhoncus non. 
Vestibulum vel orci placerat, accumsan eros at, imperdiet risus. Ut lacinia sem in 
elit blandit, ut egestas arcu molestie. Praesent pretium sed ex aliquam dictum. Nam 
varius elit vel nisi elementum, a tempus felis semper. Morbi vel metus massa. 
Nulla mattis vitae est non finibus. Morbi a placerat nibh, fringilla mattis mi. 
Nunc et suscipit mi, id imperdiet est. 
"""

from collections import Counter
palavra = texto.split()
#print(palavra)

res1 = Counter(palavra)
print(res1)

print(res1.most_common(3))  #Imprime as 3 maiores ocorências