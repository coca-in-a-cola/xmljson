from urllib.request import urlopen
from json import loads
import itertools
from datetime import datetime

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
rev = data['query']['pages']['192203']['revisions']

key_func = lambda x: \
    datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')

for key, group in itertools.groupby(rev, key_func):
    print(f'{key} {len(list(group))}')