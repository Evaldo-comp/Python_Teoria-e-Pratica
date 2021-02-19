class Carro:
    def __init__(self, vmaxima):
        self.vmaxima = vmaxima
        self.velocidade = 0

    def acelerar(self, delta=5):
        maxima = self.vmaxima
        nova = self.velocidade + delta
        self.velocidade = nova if nova <= maxima else maxima
        return self.velocidade

    def frear(self, delta=5):
        nova = self.velocidade - delta
        self.velocidade = nova if nova >= 0 else 0
        return self.velocidade


c1 = Carro(180)

for i in range(25):
    print(c1.acelerar(8))

for i in range(10):
    print(c1.frear(delta=20))
