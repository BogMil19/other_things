import time


class Test:

    def __init__(self, x):
        self.x = x

    def a(self, x):
        print(self.x)

    @classmethod
    def b(cls, x):
        print(cls, x)

    @staticmethod
    def c(x):
        print(x)


# t = Test()
# t.a(1)
# t.b(2)
# t.c(3)

# Test.a(1)
# Test.b(2)
# Test.c(3)


class Date:
    def __init__(self, *args):
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday)
        self.year, self.month, self.day = args

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

#
# a = Date()
# b = Date.today()


class NewDate(Date):
    pass


# c = Date.today()
# print(c)
# d = NewDate.today()
# print(d)


