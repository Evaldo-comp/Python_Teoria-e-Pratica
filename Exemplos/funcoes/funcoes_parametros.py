# Algumas funções precisam de dados para executar as operações presentes no seu corpo
# Esses dados são fornecidos pelo usuário quando chamamos essa função e  são chamados de argumentos

#Exemplo de função com processamento fixo

def impar_par():
    for i in range (1, 11):
        if i %2 == 0 :
            print(f' O número {i} é par')
        else:
            print(f' O número {i} é impar')
impar_par()

#Exemplo de função com processamento dinâmico com parâmetros enviados pelo usuário

def impar_par(n):
    if n % 2 == 0:
        print(f' O número {n} é par')
    else:
        print(f' O número {n} é impar')

num= int(input('Digite um número\n'))
impar_par(num)


# AS funções podem receber de 1 a n parâmetros, divididos por vírgula.
# O exemplo seguinte recebe três parâmetros para realizar uma operação escolhida pelo usuário

def calc(op,n1, n2):
    if op == 1:
        return n1 + n2
    else op == 2:
        return n1 -n2
    op = int(input("""
    Escolha a operação que deseja realizar'
    Digite:
    1:  SOMA
    2: SUBTRAÇÃO
   """))

    n1 = int(input('Digite o primeiro número '))
    n2 = int(input('Digite o segundo número '))

    print(f' O resultado da operação escolhida é {calc(op, n1, n2)}')

 #Prática:  Insira na função as operações de divisão e multiplicação além de outra opção para tratar
# a inserção de um caractere qualquer como erro.


def calc(op,n1, n2):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 -n2
    elif op == 3:
        return n1 * n2
    elif op == 4:
        return n1 // n2
    else:
        return 'entrada inválida'

op = int(input("""
Escolha a operação que deseja realizar'
Digite:
1:  SOMA
2: SUBTRAÇÃO
3: MULTIPLICAÇÃO
4: DIVISÃP"""))

n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o primeiro número '))

print(f' O resultado da operação escolhida é {calc(op,n1,n2)}')

# OBS: Há uma diferença entre parâmetros e Argumentos:
# Parâmetros são declarados na definição da função, já os argumentos
# são chamados durante a execução da mesma

# Argumentos nomeados:
# A ordem com que os argumentos são passados, pode alterar na execução da função,
# mas podemos nomear Argumentos, dessa forma , não importa a ordem em que os argumentos são passados

#Exemplo de uma função sem argumentos nomeados:

def ficha(nome, sobrenome, idade):
    print(f'Olá {nome}, {sobrenome}, você tem {idade} anos')

ficha(12, 'Pereira', 'Evaldo')

# Execução da mesma função com argumentos nomeados:

def ficha(nome, sobrenome, idade):
    print(f'Olá {nome} {sobrenome}, você tem {idade} anos')

ficha(idade = 12, sobrenome = 'Pereira', nome = 'Evaldo')


# Você pode escolher colocar um parâmetro default que torna a passagem de
# argumento para esse parâmetro como opcinal;

def exponencial(num, pot = 2): # Se nenhum número for enviado para o segundo parâmetro ele assumira o vaor dois
    return num ** pot

print(exponencial(3,3))

#OBS: Esses parâmetros default devem sempre estar no final da declaração
#def exponencial(pot=2, num)  -- errado

