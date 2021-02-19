# Escreva uma função is_alfabetico que retorne True se as letras numa palavra aparecem na ordem
# alfabética

def is_alfabetica(word):
    t = 0
    a = 0
    for i in word:
        num = ord(i)
        if num >= a:
            a = num
            print(a)
            t += 1
        else:
            return False
    if t == len((word)):
        return True


print(is_alfabetica("aei"))
