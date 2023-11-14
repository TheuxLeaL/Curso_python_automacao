# Exceptions
import logging

logging.basicConfig(
    filename='info.log',
    level=logging.DEBUG, # .DEBUG INFO WARNING ERROR CRITICAL
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)
logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

try:
    ano_atual = int(input('Qual é o ano atual?'))
except ValueError: 
    logging.warning('Você deve digitar um número.')

try:
    print(5/0)
except ZeroDivisionError:
    logging.warning('Não é possível dividir por 0')

try:
    print(5/0)
except:
    logging.warning('Ocorreu um erro')

try:
    print(5/0)
except:
    print('Ocorreu um erro')
finally:
    logging.info('usuario X realizou cálculos no sistema.')

#for pagina in range(10):
#    try:
#        print('Buscando informações')
#        print(5/0)
#    except:
#        pass