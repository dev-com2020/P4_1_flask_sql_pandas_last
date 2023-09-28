import logging

# logging.basicConfig(level=logging.ERROR)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logging.debug('To jest informacja z debug')
logging.info('To jest informacja z info')
logging.warning('To jest informacja z warning')
logging.error('To jest informacja z error')
logging.critical('To jest informacja z critical')
