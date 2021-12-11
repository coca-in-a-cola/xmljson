import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)

result = []

for item in root.iter('item'):
    result.append({
        'pubDate': item.find('pubDate').text,
        'title': item.find('title').text,
    })

with open("news.json", "w") as json_file:
    json_file.write(json.dumps(result))