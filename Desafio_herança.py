'''

Vamos imaginar que você vai criar uma classe chamada NavegadorDeSites, essa classe terá 2 propriedades
* "site"
" "conteudo_a_buscar".
 A classe terá também um método chamado:
* acessar_site, esse método deverá simplesmente imprimir para qual site está navegando e qual informação será extraída, com base nas informações que foram passadas no construtor. Ex: "Navegando até o site devaprender.com para extrarir quantidade de postagens feitas até hoje"
'''
class NavegadorDeSites:
    def __init__(self, site, conteudo_a_buscar):
        self.site = site
        self.conteudo_a_buscar = conteudo_a_buscar
    
    def AcessarSite(self):
        print(f'Acessando site {self.site} para extrair {self.conteudo_a_buscar}')

class NavegadorDeSitesDeComparação(NavegadorDeSites):
    def buscador_de_preco(self,nome_do_produto, preco):
        print(f'Buscando informações sobre {nome_do_produto}, com o preço máximo de {preco}')

produto = NavegadorDeSitesDeComparação('https://www.olx.com','relógios')
produto.AcessarSite()
produto.buscador_de_preco('Relogio lançamento 2024',400)
