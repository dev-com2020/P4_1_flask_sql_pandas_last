import logging

lista = [34, 43, 22, 566, 1, 33]
logging.debug(f'To jest informacja z debug {lista}')

test()

a = 5
b = 2

try:
    c = a / b
except Exception as e:
    logging.exception('To jest informacja z error')


valid_data = [{'name': 'Adam', 'age': '12'},
              {'name': 'Dawid', 'age': '25'},
              {'name': 'Marcin', 'age': '23'}]


def check(users,age):
    licznik = 0
    for user in users:
        try:
            user_age = int(user['age'])
        except KeyError:
            logging.exception(f'niepoprawne dane {user}')
        except ValueError:
            logging.warning(f'niepoprawny wiek {user}')
        else:
            licznik += 1 if user_age < age else 0
        finally:
            print(valid_data)

check(valid_data, 15)