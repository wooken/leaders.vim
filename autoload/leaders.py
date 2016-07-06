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
        binding_and_info = re.split(r'<[L|l][E|e][A|a][D|d][E|e][R|r]>', match)[1]
        binding_and_info_split = binding_and_info.split(' ', 1)
        binding = binding_and_info_split[0]
        info = binding_and_info_split[1]
        if '"' in info:
            desc = re.split(r'\s+"\s+', info)[1]
        else:
            desc = info
        spaces = ' ' * (8 - len(binding))
        print('{}{}| {}'.format(binding, spaces, desc))

if __name__ == '__main__':
    main()
