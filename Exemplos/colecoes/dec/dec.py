# É uma lista de alta performance

from collections import deque

deq = deque('Evaldo')
print(deq)

# Adicionar elementos no deque
deq.append('p')
print(deq)

deq.appendleft('F') # Adiciona o elemnto à esquerda
print(deq)

# removendo elementos

print(deq.pop())
print(deq.popleft()) # Remove o primeiro elemento mais à esquerda