# Logging
import logging
logging.basicConfig(
    filename='info.log',
    level=logging.DEBUG, # .DEBUG INFO WARNING ERROR CRITICAL
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)
logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

logging.debug('Isso é uma mensagem nivel debug')
logging.info('Isso é uma mensagem nivel info')
logging.warning('Isso é uma mensagem nivel warning')
logging.error('Isso é uma mensagem nivel error')
logging.critical('Isso é uma mensagem nivel critical')