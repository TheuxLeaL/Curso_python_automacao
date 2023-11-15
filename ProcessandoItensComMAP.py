# Como podemos criar listas?
# Crias listas usando loops e range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'john']
def aprovar_pessoa(nome):
    # Poderia ser uma logica mais complexa
    return nome + ' APROVADO '

print(list(map(aprovar_pessoa,nomes)))
