import os
import re


MAP_RE = '[a-z]*map'
LEADER_RE = '<[L|l][E|e][A|a][D|d][E|e][R|r]>'
MAPPING_RE = r'[^\s]+'
CMD_RE = '[a-zA-Z0-9<>:]+'
COMMENT_RE = r'"\s+[a-z ]+'


def extract_mapping_and_info(item: str) -> list:
    mapping_info = re.split(LEADER_RE, item)[1]
    mapping_info_split = mapping_info.split(' ', 1)
    mapping = mapping_info_split[0]
    binding = mapping_info_split[1]
    if '"' in binding:
        desc = re.split(r'\s+"\s+', binding)[1]
    else:
        desc = binding
    return [mapping, desc]


def is_map_function(text: str) -> bool:
    map_function_re = MAP_RE + r'\s+' + LEADER_RE + MAPPING_RE + r'\s+' + CMD_RE + r'(\s+' + COMMENT_RE + ')?'
    is_valid = re.match(map_function_re, text)
    return bool(is_valid)


def main():
    with open(os.path.expanduser('~') + '/.vimrc', 'r') as vimrc_fd:
        vimrc = vimrc_fd.read().splitlines()

    matches = []
    for line in vimrc:
        if is_map_function(line):
            matches.append(line)

    for match in matches:
        info = extract_mapping_and_info(match)
        spaces = ' ' * (6 - len(info[0]))
        print('{}{}| {}'.format(info[0], spaces, info[1]))


if __name__ == '__main__':
    main()
