class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Nº{self.numero} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append("Depósito", valor)

    def extrato(self):
        for i in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n  Saldo: {self.saldo:10.2f}\n")
