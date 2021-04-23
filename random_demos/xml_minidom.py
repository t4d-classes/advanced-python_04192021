from xml.dom import minidom

# parse an xml file by name
file = minidom.parse('sample.xml')

#use getElementsByTagName() to get tag
colors = file.getElementsByTagName('color')

# one specific item attribute
print(colors[1].attributes['hex'].value)

# all item attributes
for color in colors:
  print(color.attributes['hex'].value)

# one specific item's data
print(colors[1].firstChild.data)
print(colors[1].childNodes[0].data)

# all items data
for color in colors:
  print(color.firstChild.data)