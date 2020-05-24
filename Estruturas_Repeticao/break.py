#O break serve para parar a executar determinada instrução quando se atinge uma situação pre-determinada

#Break com for

a = 0;
for i in range(1, 100):
    if (i == 50):
        break
    else:
        print(i)
 #Break com while
while(a <=50):
    if (a == 30):
        break
    else:
        print(a)
    a=a+1
