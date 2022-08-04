from xml.etree.ElementTree import iterparse
from collections import Counter


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


holes_by_zip = Counter()

data = parse_and_remove('rows.xml', 'row/row')
for hole in data:
    holes_by_zip[hole.findtext('zip')] += 1
for zipcode, num in holes_by_zip.most_common():
    print(zipcode, num)
