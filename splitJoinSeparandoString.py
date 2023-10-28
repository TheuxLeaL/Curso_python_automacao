frase = 'Olá, bem-vindo ao treinamento mestres da automação'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #guitar #gamer #coder #pyton'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
## como concatenar (combinar strings)
hashtag_separadas_por_espaco = hashtags.split(' ')
print(','.join(hashtag_separadas_por_espaco))
print('.'.join(hashtag_separadas_por_espaco))
print(' '.join(hashtag_separadas_por_espaco))

# Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variavel chamada palavras1
frase1 = 'Desafio manipulacao de strings'

palavras1 = frase1.split()
print(palavras1)

# Desafio2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variavel chamada palavras2
frase2 = 'jhonatan,rafael,carol,camilla'
palavras2 = frase2.split((','))
print(palavras2)

# Desafio3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console
print(','.join(palavras1))


# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.
print(' & '.join(palavras2))


