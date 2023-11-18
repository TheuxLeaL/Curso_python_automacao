## Como podemos criar listas? ## 
## Crias listas usando loops e range() ##
#numeros = []
#for i in range(5):
#    numeros.append(i)
#print(numeros)

## Map ##
#nomes = ['Larissa', 'Rafael', 'Marcus', 'john']
def aprovar_pessoa(nome):
    # Poderia ser uma logica mais complexa
    return nome + ' APROVADO '

#print(list(map(aprovar_pessoa,nomes)))


## Como usar uma list compreheension ##
#nova_lista = [2 * i for i in range(10)]
## [expressão for membro in iterável] ##
#print(nova_lista)
#nomes = ['Larissa', 'Rafael', 'Marcus', 'john']
#print([nome + 'APROVADO' for nome in nomes])
#print(aprovar_pessoa(nome for nome in nomes))

'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
from pprint import pprint
pprint([[i for i in range(1,6)] for x in range (5)])

# Usar condicionais em list compreheension
# [expressão for membro in iterável (condicional if)]
nomes = ['Larissa', 'Rafael', 'Marcus', 'john']
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])

# Valores numéricos
def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
print([i for i in range(20) if i not in (1,5,15,19)])
print([i for i in range(20) if eh_numero_par(i)])

# A condicional é flexivel
# [expressão (condicional if) for membro in iterável]
participantes = ['Larissa', 'Rafael', 'Marcus', 'John']
ganhadores = ['Marcus','John']
print([i + ' GANHADOR ' if i in ganhadores else i + ' NÃO SELECIONADO' for i in participantes])


