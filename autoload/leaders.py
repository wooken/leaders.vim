import os
import re

with open(os.path.expanduser('~') + '/.vimrc', 'r') as f:
    vimrc = f.read()

matches = re.findall('[a-z]+map <leader>[a-z]+ [a-zA-Z0-9<>:]+', vimrc)

for match in matches:
    parts = match.split(' ')
    print('{} {}'.format(parts[1], parts[2]))
