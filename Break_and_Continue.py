# Break
# estilos_musicais = ['rock','pop','hip-hop','rap']
# Rodar até que ele encontre o estilo musical "hip-hop"
# for estilo in estilos_musicais:
#    if estilo == 'hip-hop':
#        break
#    print(estilo)

# estilos_musicais = ['rock','pop','hip-hop','rap']
# for estilo in estilos_musicais:
    #if estilo == 'pop':
        #continue
    #print(estilo)

# DESAFIO 
# Desafio 1
'''
Crie uma lista de preços. Depois crie um laço que exibe os valores na tela até que ele chegue no valor que você está buscando. Quando ele encontrar o valor que você está buscando ele deve sair do laõ e imprimir ' encontramos o valor desejado'
'''

precos = ['25', '35', '50', '70']
for preco in precos:
    if preco == '50':
        print(preco)

# Desafio 2
'''
Crie uma lista de sites. O seu laço deve passar sobre todos os sites porem quando encontrar um determinado site (você irá determinar qual site é esse) ele deve simplesmente pular esse site e imprimir na tela: 'Site "nome do site" foi pulado'
'''

sites = ['facebook.com', 'twitter.com', 'youtube.com', 'instagram.com']
for site in sites:
    if site == 'twitter.com':
        break
    print('Twitter pulado')
