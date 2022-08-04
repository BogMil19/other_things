from collections import defaultdict

d = defaultdict(lambda: "nie występuje")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
# print(d.__missing__("a"))
print(d["c"])

input("Aby zakończyć program wciśnij ENTER")
