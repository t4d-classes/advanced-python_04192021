import xml.etree.ElementTree as ET
from typing import cast

# Pass the path of the xml document 
tree = ET.parse('sample.xml') 

# get the parent tag 
root = tree.getroot()

for color in root[0]:
    if color.text:
        content = color.text
    else:
        content = ""
    color.text = content.capitalize()

tree.write("updated_sample.xml")