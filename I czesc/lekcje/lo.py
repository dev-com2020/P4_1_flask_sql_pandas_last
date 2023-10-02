# print("Cześć Python!")

zmienna = "Tomek"
temp = 37.1
rok = 2023
pytanie = True
nic = None

# print(type(zmienna))
# print(type(temp))
# print(type(rok))
# print(type(pytanie))
# print(type(nic))
#
# lista = [zmienna, temp, rok, pytanie, nic]
# print(lista[0])
# print(lista[0:2])
# print(lista[3:8])
# print(lista[3:])
# lista.append("Tomek")
# print(lista.count("Tomek"))
# print(lista)
# print(type(lista))
#
# krotka = tuple(lista)
# print(krotka)
#
# zestaw = ("a", "b", "c", "d")
#
# a, b, *c = zestaw
#
# print(a)
# print(b)
# print(c)
#
slownik = {"imie": "Tomek",
           1: 2023,
           'lista': ["a", "b", "c", "d"],
           'krotka': (1, 2, 3)}
#
# print(slownik[1])
# print(slownik['lista'][0])
# slownik[123] = 123456
# print(type(slownik))
#
# zestawik = {23, 45, 66, 34, 1, 45, 23}
# set_z_listy = set(lista)
# print(set_z_listy)
#
# if rok == 2022:
#     print("Mamy 2022 rok")
# elif rok == 2023:
#     print("Mamy 2023 rok")
# else:
#     print("Nie wiem jaki mamy rok?")

# x = (2, 3)

# od wersji 3.10
# match x:
#     case (0, 0):
#         print("X oraz Y wynosi 0,0")
#     case (0, 1):
#         print("X oraz Y wynosi 0,1")
#     case (2, 3):
#         print("X oraz Y wynosi 2,3")
#     case _:
#         print("Nie znam współrzędnych")

# numery = [1, 2, 3, 4, 5]
# for i in numery:
#     print(i+10)
#
# for x in zmienna:
#     print(x.capitalize())
#
# for s in slownik.values():
#     if s == "Tomek":
#         print(s.islower())

# licznik = 0
# while licznik < 5:
#     liczba = int(input("Wprowadź liczbę, od 0 do 5"))
#     print(licznik)
#     licznik += liczba


# licznik = 0
# while licznik < 5:
#     licznik += 1
#     if licznik == 3:
#         break
#     print(licznik)

liczby = []
while True:
    wynik = input("Podaj liczbę lub 'q' aby zakończyć")
    if wynik == 'q':
        break
    liczby.append(int(wynik))
print(liczby)

