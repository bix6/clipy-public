#!/usr/bin/env python3

# main.py
# bix 1/11/19
# clipy create personalized master
# input is named snippets.xml

import re

DISPATCHERS = ['Carlos', 'Erica', 'Jack', 'Ron', 'Ryan', 'Trevor']
SNIPPETS_PATH = 'snippets.xml'
OUTPUT_PATH = 'output/'

print('Creating Snippets...')
with open(SNIPPETS_PATH, 'r') as f:
	snippets = f.read()

new_snippets = {r'$NAME$':snippets}
for name in DISPATCHERS:
	name_regex = re.compile(r'\$NAME\$')
	new_snippets[name] = name_regex.sub(name, snippets)

for k,v in new_snippets.items():
	with open(OUTPUT_PATH + k + '.xml', 'w') as f:
		f.write(v)
print('Done')