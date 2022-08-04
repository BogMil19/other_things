from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring


def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'Tomek', 'wiek': 39, 'pensja': 49800}
e = dict_to_xml('stock', s)
print(e)
# print(tostring(e))
e.set('_id', '12')
print(tostring(e))
