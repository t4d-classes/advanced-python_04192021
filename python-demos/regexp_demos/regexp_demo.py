import re

# content = "as busy as a bee"
# r = re.compile(r"b[a-z]*")

# print(r.match(content))
# print(r.search(content))
# print(r.findall(content))
# print(list(r.finditer(content)))

# content = "red|green;blue:yellow"
# r = re.compile(r"[|;:]")
# print(r.split(content))
# print(r.sub(',', content))

# content = """apple
# banana
# Apple
# banana
# banana
# apple
# """

# r = re.compile(r"^apple", re.MULTILINE | re.IGNORECASE)

# print(list(r.finditer(content)))

content = "My name is Bob Smith"

# r = re.compile(r"My name is ([A-Za-z]*) ([A-Za-z]*)")
# match = r.match(content)
# if match:
#     print(match.groups())

r = re.compile(r"My name is (?P<first_name>[A-Za-z]*) (?P<last_name>[A-Za-z]*)")
match = r.match(content)
if match:
    print(match.groupdict())