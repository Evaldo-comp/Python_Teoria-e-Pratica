"""
O raise é u aplavra resevada utilizada para ajudar ac riar nossas próprias exceções
e mensagens de erros:

raise TipoDoErro('Mensagem de Erro)
"""
# Exemplo
def cadastro(nome, idade):
    nomes = ['Evaldo', 'Ana', 'Pedro', 'Carla']
    if type(nome) is not str:
        raise TypeError('O nome precisa ser uma string')
    if type(idade) is not int:
        raise TypeError('A idade precisa ser um número inteiro')
    if nome not in nomes:
        raise ValueError(f'O nome pecisa ser um entre {nomes}')
    print(f'{nome} você tem {idade} anos')

cadastro('beo', 22)