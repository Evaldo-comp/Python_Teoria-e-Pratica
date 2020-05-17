nome = ''
idade = 0
altura = 0.0
print("Insira o que se pede")
nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))

#==============================IMPRIMIDOS DADOS====================>
# Exemplo de print antigo
print("Impressão do primeiro método")
print("Seja bem vindo %s, sua idade é %d e você mede %0.1f\n"%(nome, idade, altura))

# Exemplo de print utilizando método format
print("Impressão do segundo método")
print("Seja bem vindo {0}, sua idade é {1} e você mede {2}\n".format(nome, idade, altura))

# Exemplo de print utilizando f string
print("Impressão do terceiro método")
print (f'Seja bem vindo {nome}, sua idade é {idade} e você mede {altura}')






