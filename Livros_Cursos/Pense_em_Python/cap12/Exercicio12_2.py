import random

t = []
for i in range(100):
    x = random.random()
    y = random.randint(1, 100)
    t.append(i)
    print(x)
    print(y)
print(random.choice(t))
