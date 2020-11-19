"""
Acessando parâmentros via linha de comando

Fonte: Nilo 3 ed
"""


import sys
print(f"Número de parâmentros:{len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"parâmentros{n} = {p}")
