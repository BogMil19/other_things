# class A:
#     def spam(self):
#         print('A.spam')
#
#
# class B(A):
#     def spam(self):
#         print('B.spam')
#         super().spam()  # wywołanie metody z klasy bazowej!
#
#
# class Prosta:
#     def __init__(self, obj):
#         self._obj = obj
#
#     def __getattr__(self, name):
#         return getattr(self._obj, name)
#
#     def __setattr__(self, name, value):
#         if name.startswith('_'):
#             super().__setattr__(name, value)
#         else:
#             setattr(self._obj, name, value)


class Base:
    def __init__(self):
        print('Baza.__init__')

class A(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        super().__init__()
        print('C.__init__')

c = C()
print(c)
print(C.__mro__)