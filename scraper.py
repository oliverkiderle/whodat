import requests
import json
import urllib

personality = 'Karl Marx'
urllib.quote(personality)

r = requests.get('https://en.wikipedia.org/w/api.php?format=json'
                 '&action=query&prop=extracts&exintro&explaintext'
                 '&redirects=1&titles=%s' % personality)

j = json.loads(r.text)
print json.dumps(j['query']['pages']['16743']['extract'],
                 sort_keys=True, indent=4, separators=(',', ': '))
