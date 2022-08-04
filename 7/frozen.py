import keyword
from collections import abc
from osconfeed import load


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.__data[k] = v

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


raw_feed = load()
feed = FrozenJSON(raw_feed)
print(len(feed.Schedule.speakers))
print(feed.Schedule.speakers[0].name)
talk = feed.Schedule.events[0]
print(type(talk))
print(talk.name)
print(talk.categories[1])

gradd = FrozenJSON({'name': 'Tomek', 'class': 1999})
print(gradd.name)
print(gradd.class_)
# print(getattr(gradd, 'class'))

