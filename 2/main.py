from pakiet import vector as w
from functools import reduce

# from pakiet import *

v1 = w.Vector()
# print(abs(v1))
# print(v1)



# v2 = vector2()

# symbols = '$%^&*'
# codes = [_ for _ in symbols]


# for symbol in symbols:
#     codes.append(ord(symbol))

# print(codes)

# lambda <parametr/y> : wyrażenie

# funkcja wyższego rzędu!
def funkcja(f, liczba):
    return f(liczba)


# x = 100
# y = 50
# print(funkcja(lambda x: x + 1, 100))
# print(funkcja(lambda x: x * 7, 50))
# print(funkcja(lambda x: x / 7, 50))
#
# lista = [1, 3, 5, 7, 9]
# print(f"Nasza lista: {lista}\n")
# print(f"Nasza lista z mapowaniem: {list(map(lambda _: _ * 2, lista))}")
# print(f"Nasza lista z filtrowaniem: {list(filter(lambda _: _ > 3, lista))}")
# print(f"Nasza lista z redukcją: {reduce(lambda x, y: x + y, lista)}")
#
# slownik = {'c': 11, 'b': 12, 'a': 33}
# print(sorted(slownik.items(),  key=lambda x: x[0]))
