#idade = int(input('Qual sua idade?'))
#print(idade > 18)
#print(str(10))
#altura_da_parede = float(input('Qual é a altura de sua parede?'))
#print(altura_da_parede > 2.50)

modelos_de_carros = ('bmw','ford','citroen')
print(type(modelos_de_carros))
print(list(modelos_de_carros))

cores = ['Verde','Azul','rosa']
print(tuple(cores))


'''
str()
int()
float()
list()
tuple()
'''
#Desafio
'''
Pergunte ao usuário quantos litros de água ele ja bebeu hoje e depois imprima no console se esse valor é mauior que o valor recomendado
'''
litros = float(input('Quantos litros de agua você ja bebeu hoje? '))
recomendado = 3
if litros > recomendado:
    print('Você ja atingiu a meta recomendada de água hoje, parabéns')
else:
    print('Você está abaixo do nível recomendado de água, ainda faltam {}l de agua para voce atingir o recomendado'.format(recomendado - litros))


