from math import hypot

class Vector:
    '''
    Klasa obliczająca wektor z x i y
    pozdrawiam Jolkę :P
    @:param x
    @:param y
    '''

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self)) #o.o
        # return bool(self.x or self.y) #brak wartości

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

