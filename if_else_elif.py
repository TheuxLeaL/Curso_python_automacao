# if
# elif
# else

# se ela chegar antes das 8 : 'Loja fechada'
# se ela chegar depois das 18 : 'Loja fechada'
# qualquer outro horário : 'Volte outro horário'
horario_chegada = int(input('Qual foi o horario de chegada?'))
if horario_chegada < 8:
    print('loja ainda não abriu')
elif horario_chegada > 18:
    print('Loja já fechou')
else:
    print('volte outro horário')

# cenario realista
if horario_chegada >= 8 and horario_chegada <= 12:
    print('Loja está aberta')
elif horario_chegada >= 14 and horario_chegada <= 18:
    print('Loja está aberta')
else:
    print('Loja está fechada')

#Você tem uma lista de pessoas aprovadas para entrar no evento

#wl = ('josé, marcos, camilla')
nome = (input('Qual seu nome:'))
if nome == 'josé' or 'marcos' or 'camilla':
    print('Seu nome está na lista, pode entrar')
else:
    print('Seu nome não está na lista, acesso negado')
