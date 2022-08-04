
def gen(x):
    while x:
        x -= 1
        yield x


g = gen(5)

# for i in gen(5):
#     print(i)

print(next(g))
# print(next(g))
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
