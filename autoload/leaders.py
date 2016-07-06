import os
import re


def is_map_function(text):
    is_valid = re.match(r'[a-z]*map <leader>[^\s]+ [a-zA-Z0-9<>:]+(\s+"\s+[a-z ]+)?', text)
    return bool(is_valid)


def main():
    with open(os.path.expanduser('~') + '/.vimrc', 'r') as vimrc_fd:
        vimrc = vimrc_fd.read().splitlines()

    matches = []
    for line in vimrc:
        if is_map_function(line):
            matches.append(line)

    for match in matches:
        info = match.replace('<cr>', '').split('<leader>')
        print(info[1])

if __name__ == '__main__':
    main()
