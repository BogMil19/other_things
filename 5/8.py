import math

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Oblicznie powierzchni')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Obliczanie obwodu')
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimeter)
print(c.radius)
print(c.perimeter)
print(vars(c))
print(c.area)
del c.area
print(vars(c))
print(c.area)