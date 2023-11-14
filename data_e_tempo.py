from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

print(datetime(2020,1,25))

data_postagem_foto = datetime.strptime(input('Quando devemos postar essa foto?'),'%d/%m/%Y') #Y maiusculo para 4 digitos no ano
print(type(data_postagem_foto))

data_inicio = datetime.now()
data_entrega = datetime(2024,1,15)

prazo_entrega = data_entrega - data_inicio
print(prazo_entrega)

data1 = datetime.now()
data_aniversario = datetime(2024,10,2)

tempo_que_falta = data_aniversario - data1
print(tempo_que_falta)

