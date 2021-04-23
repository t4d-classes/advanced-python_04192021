import xml.etree.ElementTree as ET 

# Pass the path of the xml document 
tree = ET.parse('sample.xml') 

# get the parent tag 
root = tree.getroot() 

# print the root (parent) tag along with its memory location 
print(root) 

# print the attributes of the first tag  
print(root[0][0].attrib) 

# print the text contained within first subtag of the 5th tag from the parent 
print(root[0][2].text) 