'''for nome_da_variavel_temporaria in quantas_vezes:
    fazer_algo_aqui_dentro
'''
fotos = ['foto1','foto2','foto3','foto4','foto5']
for foto in fotos:
    print(foto)

# Você ja sabe a quantidade de vezes que deve rodar
for volume in range(1,11):
    print(f'Aumentando o volume para {volume}')

'''
Desafio
Exiba na tela usando o loop todas as palavras que esvierem dentro de uma lista. Voc~E PODE COLOCAR DENTRO DESSA LISTA OS NOMES DOS OBJETOS QUE VOCE MAIS USA NA SUA CASA, A QUANTIDADE DE NOMES FICA A SEU CRITÉRIO
'''
objetos = ['computador', 'celular' , 'mouse', 'teclado' , 'garrafa de agua']
for objeto in objetos:
    print(objeto)

'''
Desafio 2
Você precisa de 10 passos para finalizar uma tarefa. Imprima na tela: "Executando passo 1", até "Executando passo 10" usando laõ for
'''
for passo in range (1,11):
    print(f'Executando Passo {passo}...')
    