
from conta import Conta
from cliente import Cliente
joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")
conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)

conta1.saque(190)
conta2.deposito(300)


Joao = Conta("João da Silva", "777-1234")
Maria = Conta("Maria da Silva", "555-4321")

print(f"{conta1.saldo}")
