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

lista = [34, 43, 22, 566, 1, 33]
logging.debug(f'To jest informacja z debug {lista}')


a = 5
b = 2

try:
    c = a / b
except Exception as e:
    logging.exception('To jest informacja z error')


valid_data = [{},
              {'name': 'Dawid', 'age': '25'},
              {'name': 'Marcin', 'age': '23'}]


def check(users,age):
    licznik = 0
    for user in users:
        try:
            if int(user['age']) < age:
                licznik += 1
        except KeyError:
            logging.exception(f'niepoprawne dane {user}')
        except ValueError:
            logging.warning(f'niepoprawny wiek {user}')

check(valid_data, 15)



# logging.info('To jest informacja z info')
# logging.warning('To jest informacja z warning')
# logging.critical('To jest informacja z critical')
