# class Date:
#     __slots__ = ['year', 'month', 'day']
#
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

class String:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        if not isinstance(value, str):
            raise TypeError('Oczekiwano łańcucha znaków')
        instance.__dict__[self.name] = value


class Osoba:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Osoba):
    @property
    def name(self):
        print('Pobieranie imienia')
        return super().name

    @name.setter
    def name(self, value):
        print('Ustawianie imienia na', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Usuwanie imienia')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('Tomek')
s.name

s.name = "Paweł"
s.name

# s.name = 5454
# s.name

# class Person:
#     def __init__(self, first_name):
#         self.set_first_name(first_name)
#
#     def get_first_name(self):
#         return self._first_name
#
#     def set_first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Oczekiwano łańcucha znaków!')
#         self._first_name = value
#
#     def del_first_name(self):
#         raise AttributeError('Nie można usunąc atrybutu!')
#
#     name = property(get_first_name, set_first_name, del_first_name)
