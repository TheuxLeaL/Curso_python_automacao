import random
class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas=['Cristian','Robert','Rossana','Ana']
    
    def Iniciar(self):
        print('Olá bem vindo a este site!') # Inicie o debug aqui (coloque um breakpoint)
        self.ChutarIdade(self.pessoas) #Pule essa linha
        self.ChutarNome() # Entre dentro do método dessa linha
        self.ChutarCor() # Entre neste método
        print('Programa finalizado')
    
    def ChutarCor(self):
        cores = ['Azul','rosa','verde']
        for cor in cores:
            print(f'as opções de cores são {cor}')

        print('Sua cor favorita é...') # não continue a execução aqui, volte para onde estava antes
        cor_preferida = random.choice(cores)
        print(cor_preferida)

    def ChutarNome(self):
        nome = f'bem vindo ' (random.choice(self.pessoas))
        print(nome)
    
    def ChutarIdade(self,pessoas):
        # ENtre aqui
        idade = random.radint(18,50)
        print(idade)
    
email = EmailDeBoasVindas()
email.Iniciar()