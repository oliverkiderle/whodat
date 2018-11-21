#!/usr/bin/env python3

import requests
import json
import urllib
import re


def main():
    personality = 'Karl Marx'
    urllib.quote(personality)

    r = requests.get('https://en.wikipedia.org/w/api.php?format=json'
                     '&action=query&prop=extracts&exintro&explaintext'
                     '&redirects=1&titles=%s' % personality)

    j = json.loads(r.text)

    bio = json.dumps(j['query']['pages']['16743']['extract'],
                     sort_keys=True, indent=4, separators=(',', ': '))

    bio = removeNameAndGenederedPronouns(bio, personality)

    print bio


def removeNameAndGenederedPronouns(bio, personality):
    names = personality.split()

    gendered_pronouns = ['he', 'she', 'He', 'She']

    replace_with_they = [personality] + names + gendered_pronouns

    genitiv = [x + "'s" for x in names] + [x + "'" for x in names]

    replace_with_their = ['his', 'her', 'His', 'Her'] + genitiv

    for i in replace_with_they:
        bio = re.sub('\"' + i, 'This person', bio)

        bio = re.sub('(\\. )' + i, r'\1They', bio)

        bio = re.sub('(\\.)' + i, r'\1 They', bio)

        bio = re.sub('(\\s)' + i + '[ ,\n]', r'\1they ', bio)

    for i in replace_with_their:
        bio = re.sub('(\\. )' + i, r'\1Their', bio)

        bio = re.sub('(\\.)' + i, r'\1Their', bio)

        bio = re.sub('(\\s)' + i + ' ', r'\1their ', bio)

    return bio


if __name__ == '__main__':
    main()
