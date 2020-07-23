"""
Pedro mora no em fazenda, cortada por um rio, na noite passada choveu muito, houve boatos de enchente
e Pedro precisa ir na cidade mas para isso ele precisa verificar se a ponte sobre o rio da fazenda está intacta

Dica: a ponte intacta "########", a ponte quebrada ("## ## ##")
"""

def status_ponte(s):
    if " " in s:
        return False
    return True

print(status_ponte("#########"))