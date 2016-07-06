import os
import re


def main():
    with open(os.path.expanduser('~') + '/.vimrc', 'r') as vimrc_fd:
        vimrc = vimrc_fd.read()

    matches = re.findall(r'[a-z]+map <leader>[^\s]+ [a-zA-Z0-9<>:]+', vimrc)

    for match in matches:
        parts = match.split(' ')
        print('{} {}'.format(parts[1], parts[2]))

if __name__ == '__main__':
    main()
