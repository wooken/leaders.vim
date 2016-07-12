import os
import re


COMMENT_RE = r'^"\s+.*$'
MAP_RE = '[a-z]*map'
LEADER_RE = '<[L|l][E|e][A|a][D|d][E|e][R|r]>'
MAPPING_RE = r'[^\s]+'
CMD_RE = '[a-zA-Z0-9<>:]+'


def get_vimrc(filename) -> list:
    with open(filename, 'r') as vimrc_fd:
        vimrc = vimrc_fd.read().splitlines()
    return vimrc


def is_comment(text: str) -> bool:
    return bool(re.match(COMMENT_RE, text))


def is_mapping(text: str) -> bool:
    map_function_re = '^' + MAP_RE + r'\s+' + LEADER_RE + MAPPING_RE + r'\s+' + CMD_RE + '$'
    return bool(re.match(map_function_re, text))


def extract_comments_and_mappings(vimrc: list) -> list:
    # returns a list[tuple]
    comments_and_mappings = []  # type: list
    for idx, line in enumerate(vimrc):
        if is_mapping(line):
            prev_line = vimrc[idx - 1]
            if is_comment(prev_line):
                comment = prev_line
            else:
                comment = None
            comments_and_mappings.append((line, comment))
    return comments_and_mappings


def generate_output_list(comments_and_mappings: list) -> list:
    output = []  # type: list
    for idx, item in enumerate(comments_and_mappings):
        comment = item[1]
        line = item[0]
        if is_mapping(line):
            relevant = re.split(LEADER_RE, line)[1]
            mapping_info = relevant.split(' ', 1)
            mapping = mapping_info[0]
            binding = mapping_info[1]

            # deal with comment
            if comment:
                desc = re.split(r'"\s+', comment)[1]
            else:
                desc = binding
            output.append([mapping, desc])
    return output


def prettyprint(output: list) -> None:
    for line in output:
        spaces = ' ' * (6 - len(line[0]))
        print('{}{}| {}'.format(line[0], spaces, line[1]))


def main():
    vimrc_filename = os.path.expanduser('~') + '/.vimrc'
    vimrc = get_vimrc(vimrc_filename)
    matches = extract_comments_and_mappings(vimrc)
    output = generate_output_list(matches)
    print(vimrc_filename)
    print('-' * len(vimrc_filename))
    prettyprint(output)

if __name__ == '__main__':
    main()
