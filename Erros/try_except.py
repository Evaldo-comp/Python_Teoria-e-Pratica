"""
O bloco try/except serve para tratar erros, impedindo que o usuário receba mensagens de erros
inesperadas.

Estrutura

try:
    // Execução de trecho com erro
except:
    // Comportamento do software em caso de problema
"""
# Exemplo01 - Tratamento genérico (Não aconcelhável)
try:
    print(f'a idade do usuário é {idade}')
except:
    print('Idade não declarada')

# Exempl02 - Tratamento Específico
try:
    print(f'a idade do usuário é {idade}')
except NameError:
    print('Idade não declarada')

# Exemplo03 - Tratando várias exceções de uma só vez

try:
    print(f'a idade do usuário é {idade}')
except NameError:
    print('Ocorreu um NameError')
except TypeError:
    print('Ocorreu um TypeError')
except ValueError:
    print('Ocorreu um ValueError')