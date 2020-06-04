import json

with open('cobfuscator/cthings.json') as cthings_file:
    cthings = json.load(cthings_file)

whitespace = cthings['whitespace']
operators = cthings['operators']
delimiters = whitespace + operators + cthings['other']