class Data:
    pass


d1 = Data()  # instanciação de um objeto
d1.dia = 5
d1.mes = 12
d1.ano = 2020

# Pelo fato do Python ser uma linguagem dinâmica, é possivel fazer a inicialização atributos diretamente no
# objeto mesmo sem tê-lo feito antes na própria classe.

print(f"{d1.dia}/{d1.mes}/{d1.ano}")
