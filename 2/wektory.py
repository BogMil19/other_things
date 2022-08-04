from pakiet import vector as w
from datetime import date

text = "Kurs Pythona"


# print(format(text, '^20'))
# print(format(text, '=>20s'))
# print(format(text, '*^20s'))
# print(format('{:>10} {:>10} {:^20}'.format('Witaj', 'świecie', 'programisto')))


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)
# print(p)
# print(Pair(3, 4))
#
# print('p to {0!r}'.format(p))
# print('p to {0}'.format(p))

FORMATS = {}
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}-{d.month}-{d.year}',
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


# d = Date(2022, 8, 3)
# print(format(d))
# print(format(d, 'mdy'))
d = date(2022, 8, 3)
print(format(d, '%A, %B %d, %Y'))
print('Dziś jest: {:%d %b %Y}'.format(d))
