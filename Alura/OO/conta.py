class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"construinfo objeto..{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo do {self.titular}: R$ { self.saldo} Reais")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor