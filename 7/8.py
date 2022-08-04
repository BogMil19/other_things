from xml.etree.ElementTree import parse, Element

doc = parse('data/pred.xml')
root = doc.getroot()
print(root)

root.remove(root.find('sri'))
root.remove(root.find('cr'))

root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'Testowo'
root.insert(2, e)

doc.write('newpred.xml',xml_declaration=True)