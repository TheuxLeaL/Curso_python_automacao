# Random
'''
1 Você QUER SIMULAR A OPÇÃO DE JOGAR UMA MOEDA E RESULTAR EM CARA OU COROA
2. SORTEIO ENTRE 300 NOMES EM UMA LISTA DE NOMES ]
3. ESCOLHER UM NUMERO ALEATORIAMENTE DE 10-100
4. ESCOLHER UMA CARTA ALEATORIAMENTE DENTRO DE UM BARALHO
5. GERAR NOMES DE USUARIO ALEATORIAMENTE
6. GERAR SENHAS SEGURAS
'''
import random

print(random.random()) # Valor 0.0 até 1.0
print(random.uniform(4,10)) # Valor decimal do mínimo ao máximo declarado
print(random.randint(12,55)) # Valor inteiro do minimo ao maximo declarado

cores = ['verde','vermelho','azul']
print(random.choice(cores)) # Escolher uma opção dentro de uma fonte

cartas_de_um_baralho = ['carta1','carta2','carta3','carta4','carta5']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho)