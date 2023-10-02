# def drukowanie(x=1):
#     return "drukuje..." * x

drukowanie = lambda x: "drukuje..." * x

print(drukowanie(5))
lista = []
lista.append(drukowanie(3))
print(lista)

kwadraty = [i * i for i in range(10)]
parzyste_kwadraty = [i * i for i in range(10) if i % 2 == 0]

# for i in range(10):
#     kwadraty.append(i * i)

print(kwadraty)
print(parzyste_kwadraty)

slownik_kw = {i: i * i for i in range(5)}
# for i in range(5):
#     slownik_kw[i] = i * i

print(slownik_kw)
