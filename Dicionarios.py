# Dicionários

'''
Pessoa
    nome
    idade
    altura
'''
pessoa = {'Nome':'Mateus','Idade':19,'Altura':168}
print(pessoa)

filme = dict(nome="Homen-Aranha", ano_lancamento="2025", nota="8")
print(filme)

#remover valores duplicados
nomes = ['Adolfo','Adriana','Adriana','Adão']
print(list(dict.fromkeys(nomes)))