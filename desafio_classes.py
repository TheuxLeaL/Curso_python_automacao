# DESAFIO
'''
Você irá criar a class Carro e eu quero no mínimo 3 propriedades para a classe carro e no mínimo 3 métodos para ela.
'''
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def Ligar(self):
        print('Ligando carro')
    
    def AbrirVidro(self):
        print('Abrindo vidro')

    def Desligar(self):
        print('Desligando carro')

    def ExibirInfosDoCarro(self):
        print(self.marca, self.modelo, self.ano)
    

carro1 = Carro('Volvo','XC40','2023')
carro2 = Carro('Renault','Sandero','2020')
carro3 = Carro('Porsche','Boxer','2022')

carro1.ExibirInfosDoCarro()
carro2.ExibirInfosDoCarro()
carro3.ExibirInfosDoCarro()
carro1.Ligar()
carro1.Desligar()
carro1.AbrirVidro()

