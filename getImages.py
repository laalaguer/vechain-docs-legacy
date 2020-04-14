import os
import re

result = []

for root, dirs, files in os.walk('.'):
    for filename in files:
        if 'rst' == filename.split('.')[-1]:
            result.append(os.path.join(root, filename))
        if 'md' == filename.split('.')[-1]:
            result.append(os.path.join(root, filename))

def extractImages(filename):
    lines = []
    with open (filename, 'r') as f:
        # print(len( f.readlines()))
        lines.extend(f.readlines())
    
    p = re.compile('http(.*?)(png|jpg|jpeg|gif)', re.IGNORECASE)
    for line in lines:
        m = p.search(line)
        if m and 'readme' in m.group():
            print(m.group())


for element in result:
    extractImages(element)