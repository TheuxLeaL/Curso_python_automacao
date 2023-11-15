class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian','Robert','Rossana,','Ana']
    
    def Iniciar(self):
        print('Olá bem vindo a este site!')
        emails_apresentação = self.MontarCredencial(self.pessoas)
        for email in emails_apresentação:
            print(email)
    
    def MontarCredencial(self,pessoas):
        credenciais = []
        for pessoa in pessoas:
            credenciais.append(f'A empresa gostaria de dar as boas vindas para o(a) {pessoa}')
        return credenciais

email = EmailDeBoasVindas()
email.Iniciar()
# 'F5' Começar a debuggar seu código
# 'F10' Analisar linha sem entrar no código interno
# 'F11' Analistar linha e entrar no código interno
# 'SHIFT-F11' Sair do bloco de código atua le continuar a execução