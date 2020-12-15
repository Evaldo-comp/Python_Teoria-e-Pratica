
from cliente import Cliente
from conta import Conta, ContaEspecial

Edson = Cliente("João da Silva", "777-1234")
Maria = Cliente("Maria da Silva", "555-4321")
conta1 = Conta([Edson], 1, 1000)
conta2 = ContaEspecial([Maria, Edson], 2, 500, 100)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()


print(f"{conta1.saldo}")
