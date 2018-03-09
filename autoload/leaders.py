import os

def get_vimrc(filename) -> list:
    with open(filename, 'r') as vimrc_fd:
        vimrc = vimrc_fd.read().splitlines()
    return vimrc

def is_comment(text: str) -> bool:
    return text.startswith('" ')

def is_mapping(text: str) -> bool:
    if not text:
        return False
    parts = text.split(' ')
    if parts[0][-3:] != 'map':
        return False
    if parts[0][0] == '"':
        return False
    if parts[1].lower()[:8] != '<leader>':
        return False
    return True

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
    for line, comment in comments_and_mappings:
        if is_mapping(line):
            relevant = line.split('>', 1)[1]
            mapping_info = relevant.split(' ', 1)
            mapping = mapping_info[0]
            binding = mapping_info[1]
            if comment:
                desc = comment.split('" ')[1]
            else:
                desc = binding
            output.append((mapping, desc))
    return output

def prettyfmt(list_to_print: list, title: str) -> str:
    output = ""
    output += title + '\n'
    output += '-' * len(title) + '\n'
    for idx, line in enumerate(list_to_print):
        spaces = ' ' * (6 - len(line[0]))
        output += f'{line[0]}{spaces}| {line[1]}'
        if idx < len(list_to_print) - 1:
            output += '\n'
    return output

def main():
    vimrc_filename = os.path.expanduser('~') + '/.vimrc'
    vimrc = get_vimrc(vimrc_filename)
    matches = extract_comments_and_mappings(vimrc)
    output = generate_output_list(matches)
    print(prettyfmt(output, vimrc_filename))

if __name__ == '__main__':
    main()
