#re.match

import re

text = "Python is a powerful language"
result = re.match("python", text)

if result:
    print("Python")
else:
    print("No match")

#re.search 

import re

text = "The weather is hot today"
result = re.search("hot", text)

if result:
    print("Yes, it's hot")
else:
    print("Not found")

#re.findall

import re

text = "My marks are 85, 90, 78 and 92"
numbers = re.findall(r"\d+", text)

print("All numbers:", numbers)

#re.finditer

import re
text = "apple banana apple mango"
for match in re.finditer("apple", text):
    print(f"Found: {match.group()}")
    print(f"Start: {match.start()} End: {match.end()}")

#re.split

import re
text = "python, Java; c++ | Javascript"
languages = re.split("[,;|]", text)
print(f"Languages: {languages}")

#re.sub

import re
text = "My phone number is 9876543210"
hidden = re.sub(r"\d", "x", text)
print(hidden)