# Usando a list compreheension crie a seguinte lista:
# [2,4,6,8,10]

print([i for i in range(11) if i not in (0,1,3,5,7,9)])

# Use a list compreheension usando a seguinte lista como base:
from pprint import pprint
cores = ['vermelho','azul','verde','amarelo','rosa','preto']
pprint([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])

# Desafio 3
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']

pprint([participante + ' PAGO' if participante in pagamento_realizado else participante + ' DEVENDO' for participante in participantes])

