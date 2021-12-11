import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

result = []

for item in root.iter('item'):
    obj = {}
    for child in item:
        obj[child.tag] = child.text
    result.append(obj)

with open("news_2.json", "w") as json_file:
    json_file.write(json.dumps(result))