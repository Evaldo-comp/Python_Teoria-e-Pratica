"""
Toda entrada deve ser tratada


try:
    idade = int(input("Digite sua idade"))
except:
    print("Valor incorreto")  # Mensagem de erro
else:
    print(f'Sua idade é {idade}')  # Execução caso não ocorra erro
finally:
    print("Executando o finally")  # Sempre é executado com ou sem erro

def divisao(x, y):
    return x/y


# Tratamento fora da função (ERRADO e DISPENDIOSO)
num1 = int(input("Informe o primeiro número"))
try:
    num2 = int(input("Informe o segundo número"))
except ValueError:
    print("O valor deve ser numérico")
try:
    print(divisao(num1, num2))
except NameError:
    print("Valor incorreto")
"""
# Tratamento dentro da função (CORRETO)

def div(a, b):
    try:
        return int(a)/ int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

a = input('Qual o valor do primeiro número?')
b = input('Qual o valor do segundo número?')
print(div(a, b))

