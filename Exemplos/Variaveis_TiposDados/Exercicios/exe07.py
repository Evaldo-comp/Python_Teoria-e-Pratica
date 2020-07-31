"""
Faça a comparação entre duas strings retornado True se forem iguais e
False se forem diferentes.
dica: "Bola" == "BOla"
"""
def iguais(s1,s2):
    if s1.lower() == s2.lower():
        return True
    return False

#Função aprimorada
def iguais(s1,s2):
    return s1.lower() == s2.lower()

print(iguais("Evaldo", "EVALDO"))