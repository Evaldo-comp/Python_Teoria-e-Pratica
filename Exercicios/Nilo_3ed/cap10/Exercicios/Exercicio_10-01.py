
"""
Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos 
Televisão e atribua tamanhos e marcas diferentes. Depois imprima o valor 
desses atributos de forma a confirmar a independência dos valores de cada 
instância
"""


class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = "50 pol"
        self.marca = "Samsung"


tv = Televisão()
tv_quarto = Televisão()
tv_sala = Televisão()

tv_quarto.tamanho = "40 pol"
tv_quarto.marca = "LG"

tv_sala.tamanho = "32 pol"
tv_sala.marca = "Sony"

print(f" Tamanho da TV do quarto {tv_quarto.tamanho}\n")
print(f" Marca da Tv do quarto {tv_quarto.marca}\n")

print(f" Tamanho da TV da sala {tv_sala.tamanho}\n")
print(f" Marca da TV da sala {tv_sala.marca}\n")
