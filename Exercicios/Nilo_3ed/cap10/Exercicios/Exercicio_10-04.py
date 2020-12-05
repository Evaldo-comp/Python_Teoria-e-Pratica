"""
Modifique o construtor da classe televisão de forma que min e max sejam parâmetros
opcionais, em que min vale 2 e max vale 14, caso outro valor não seja passado
"""


class Televisão:
    def __init__(self, canal_ini, min=2, max=14):
        self.ligada = False
        self.canal = canal_ini
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1


tv = Televisão(3)

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for x in range(0, 4,  120):
    tv.muda_canal_para_baixo()
print(tv.canal)
