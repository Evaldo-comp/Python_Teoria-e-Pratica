with open("listaNomes.txt") as nomes:
    for i in nomes.readlines():
        if i[0] != "*":
            print(i)
        else:
            break
