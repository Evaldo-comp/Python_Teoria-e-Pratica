"""
Atualmente a classe Televisão inicializa o canal com 2. Modifique a classetelevisão de forma areceber
o canal incial em seu contrutor
"""


class Televisão:
    def __init__(self, canal_ini, min, max):
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


tv = Televisão(1,  4,  99)

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for x in range(0, 4,  120):
    tv.muda_canal_para_baixo()
print(tv.canal)
