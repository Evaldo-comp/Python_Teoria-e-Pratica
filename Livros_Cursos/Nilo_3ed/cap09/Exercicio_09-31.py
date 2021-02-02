# Verificação se um diretório ou arquivo existe
import os.path

print(os.getcwd())
for z in os.listdir("."):
    if os.path.isdir(z):
        print("z existe e é um diretório")
    else:
        print("O diretório z não existe")
