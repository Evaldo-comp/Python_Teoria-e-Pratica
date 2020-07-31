
# len () retorna o tamanho de um iterável

print(len('Nome'))
print(len(list(range(120))))

for i in len(list(range(10))):
    print(i, end='')



# abs () retorna o valor absoluto de um inteiro ou real

print(abs(-2))
print(abs(-2.3))


# sum () retorna a soma total de um iterável

lst1 = list(range(8))
lst2 = list(range(18))
print(sum(list(range(10))))
print(sum(lst1, len(lst2)))
print(sum({'q': 2,'a': 6,'r': 7 ,'y': 24 ,'w':21 ,}.values()))
#OBS: sum não funcionará com strings, para isso utilize .join()



# round() retorna um número arredondado para uma determinada quantidade de digitos de precisão
# no caso da precisão nao ser informada ele retornará o inteiro mais próximo do número que foi
# fornecido como entrada

print(round(2.6))
print(round(5.6323232, 3))
print(round(2.61112, 2))
print(round(2.61111212111212, 4))