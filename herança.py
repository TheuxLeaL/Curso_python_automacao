# A herança é um conceito da orientação de objetos que é usado na programação para nos ajudar a evitar ficar nos repetindo e re'escrevendo funcionalidades repetidamente, quando elas ja existem em outras classes. Ou seja através da herança nós podemos herdar e reutilizar os métodos e propriedades de outra classe.
class computador:
    def __init__(self, marca, memoria_ram, placa_de_video): #show just the first example property then show the others
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def Ligar(self):
        print('estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformacoesDesseComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

class ComputadorGamer(computador): #puxando tudo da primeira classe
    def __init__(self, marca, memoria_ram, placa_de_video, tamanho_da_torre): #Override/subscrever a classe que serviu de herança com mais propriedades
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        self.tamanho_da_torre = tamanho_da_torre
    def trocar_cor_led(self,cor):
        print(f'Trocando cor dos led para {cor}')
    def ligar_ventoinha(self):
        print('Ligando a ventoinha')
    def desligar_ventoinha(self):
        print('Desligando ventoinha')
    
    def ExibirInformacoesDesseComputador(self): #subscrevendo o método para exibir a nova propriedade "tamanho_da_torre"
        print(self.marca, self.memoria_ram, 
              self.placa_de_video, self.tamanho_da_torre)
    
pc_gamer = ComputadorGamer('Asus', '16gb', 'RTX 3080TI','Médio')
pc_gamer.Ligar()
pc_gamer.ExibirInformacoesDesseComputador()
pc_gamer.trocar_cor_led('Azul')
pc_gamer.ligar_ventoinha()
pc_gamer.desligar_ventoinha()
