# Listas
site1 = 'youtube.com'
site2 = 'facebook.com'
site3 = 'instagram.com'

sites = ['youtube.com','facebook.com','instagram.com']
# print(sites[1])

# Adicionando na lista
sites.append('novosite.com')
print(sites)

# Removendo na lista
sites.remove('facebook.com')
print(sites)

# Listas dinâmicas

sites = ['youtube.com','facebook.com','instagram.com', 35, True]

# Lista de listas
pessoas = [['Rafael',25], ['Amanda',19]]
print(pessoas)
print(pessoas[1][0])

# Desafio 1
''' Desafio 1 crie uma lista que tenha os nome de 3 objetos que você mais usa durante o dia e imprima ele na tela'''
objetos = ['pc','celular','chinelo']
print(objetos)
''' Dentro de cada um coloque uma info extra, coloque o valor em reais desse objeto tambem e imprima ele na tela'''
objetos2 = [['pc',4000.00], ['celular',2000.00],['chinelo',100.00]]
print(objetos2)


