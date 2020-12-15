
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


Edson = Cliente("Edson", "123.123")
Maria = Cliente("Maria", "222.222")

print(Edson.telefone)
print(Edson.nome)

print(Maria.nome)
print(Maria.telefone)
