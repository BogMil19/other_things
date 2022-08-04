from urllib.request import urlopen
import warnings
import os
import json

URL = 'https://github.com/AllenDowney/fluent-python-notebooks/blob/master/19-dyn-attr-prop/oscon/'
JSON = 'data/osconfeed-sample.json'


def load():
    if not os.path.exists(JSON):
        msg = 'Ściągam {} do {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
    with open(JSON) as fp:
        return json.load(fp)


feed = load()
print(sorted(feed['Schedule'].keys()))

for k, v in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(v), k))

print(feed['Schedule']['speakers'][0]['name'])
print(feed['Schedule']['events'][0]['categories'][1])
