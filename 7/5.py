from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('https://planetpython.org/rss20.xml')
doc = parse(u)

# for item in doc.iterfind('channel/item'):
    # title = item.findtext('title')
    # print(title)
    # date = item.findtext('pubDate')
    # print(date)
    # link = item.findtext('link')
    # print(link)


print(doc)
e = doc.find('channel/item')
print(e)
print(e.tag)



# print(title)
# print(date)
# print(link)
# print()