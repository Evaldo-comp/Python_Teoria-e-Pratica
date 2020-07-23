"""
Essa função assim como a filter() e map(), pega dois parâmetros, sendoi um deles um iterável
Estrtura : reduce(x, y), onde x é o primeiro dado de uma coeção e o y é o segundo
            em seguida x recebe or esultado da opração de xy e o segundo parâmetro rece o 3 item da coleção
"""
from functools import reduce  # reduce precisa ser importada
#Exemplo:
dados =[1, 3, 4, 23, 100, 25, 45, 34 ]
# A função que vai ser passada para o reduce tem que ter dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)
