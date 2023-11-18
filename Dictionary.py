# Dictionary compreheension
# [expressão for membro in iterável]
# {chave:expressão for membro in iterável}
from pprint import pprint
pprint({i: i for i in range(20)})
# Popular um dicionario com valores
produtos = ['produto1','produto2','produto3','produto4','produto5']
#pprint({produto: 1 for produto in produtos})
# Gerar uma matriz de valores de teste
pprint({produto: [0 for i in range(5)] for produto in produtos})
# [expressão for membro in iterável]
pprint({produto: [i*2 for i in range(5)] for produto in produtos})
# Gerar valores de teste
import random
pprint({produto: [random.randint(1000,15000) for i in range(5)] for produto in produtos})