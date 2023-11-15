# DESAFIO
'''
1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
    jogue as opções dentro de uma variável e depois crie um programa que imprime 'cara' ou 'coroa' na tela
 '''
import random
moeda = ['cara','coroa']
print(random.choice(moeda))

'''
2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
    Crie uma lista de 5 nomes e soreteie um nome de dentro dessa lista e exiba na tela
'''
nomes = ['Matheus','Rebeca','Carlos','Miguel','João']
print(random.choice(nomes))

'''
3. Escolha aleatoriamente um número de 10-100
    Imprima na tela um valor aleatório entre 10 e 100
'''
print(random.randint(10,100))