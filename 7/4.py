import json

#
# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
#
# json_str = json.dumps(data)
#
# data = json.loads(json_str)
#
# with open('osconfeed-sample.json','r') as f:
#     data2 = json.load(f)
#     print(data2)


# json.dumps(False)
# d = {'a': True,
#      'b': 'Hello',
#      'c': None}

# print(json.dumps(d))
from collections import OrderedDict

string = '{"conferences": [{"serial": 115 }],"events": [{ "serial": 34505,"name": "Why Schools Don´t Use Open Source to Teach Programming"}]}'


# dict2 = json.loads(string)
# print(json.dumps(dict2, indent=4, sort_keys=True))

# data = json.loads(string, object_pairs_hook=OrderedDict)
# print(data)


class JSON_Obj:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(string, object_hook=JSON_Obj)
d1 = data.events
print(d1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

classes = {'Point':Point}

def unseralize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for k, v in d.items():
            setattr(obj, k, v)
            return obj

p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unseralize_object)
print(a)
print(a.x)