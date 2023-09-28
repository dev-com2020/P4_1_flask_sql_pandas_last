import logging

# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(filename='app.log', filemode='w', format='%(process)d - %(levelname)s - %(message)s')
# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(process)d - %(levelname)s - %(message)s')
logging.basicConfig(filename='app.log',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(process)d - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


# logging.info('To jest informacja z info')
# logging.warning('To jest informacja z warning')
# logging.critical('To jest informacja z critical')
