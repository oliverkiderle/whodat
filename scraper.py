#!/usr/bin/env python3

import requests
import json
import urllib
import re

personality = 'Karl Marx'
urllib.quote(personality)

r = requests.get('https://en.wikipedia.org/w/api.php?format=json'
                 '&action=query&prop=extracts&exintro&explaintext'
                 '&redirects=1&titles=%s' % personality)

j = json.loads(r.text)
bio = json.dumps(j['query']['pages']['16743']['extract'],
                 sort_keys=True, indent=4, separators=(',', ': '))

names = personality.split()
genitiv = [x + "'s" for x in names] + [x + "'" for x in names]
gendered_pronouns = ['he','she', 'He', 'She']

possessive = ['his', 'her', 'His', 'Her'] + genitiv

replaceables = [personality] + names + gendered_pronouns

for i in replaceables:
    bio = re.sub('\"' + i, 'This person', bio)
    
    p = re.compile('(\. )' + i)
    bio = p.sub(r'\1They', bio)

    p = re.compile('(\.)' + i)
    bio = p.sub(r'\1 They', bio)

    p = re.compile('(\s)' + i + '[ ,\n]' )
    bio = p.sub(r'\1they ', bio)

for i in possessive:
    p = re.compile('(\. )' + i)
    bio = p.sub(r'\1Their', bio)

    p = re.compile('(\.)' + i)
    bio = p.sub(r'\1Their', bio)

    p = re.compile('(\s)' + i + ' ')
    bio = p.sub(r'\1their ', bio)

print bio
