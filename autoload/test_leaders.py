import leaders


def test_is_map_function_basic():
    all_map_commands = [
        'map',
        'nmap',
        'noremap',
        'nnoremap',
    ]
    for cmd in all_map_commands:
        assert leaders.is_map_function('{} <leader>c :Commands<cr>'.format(cmd)) is True
    assert leaders.is_map_function('this is just regular text') is False


def test_is_map_function_comments():
    assert leaders.is_map_function('nnoremap <leader>c :Commands<cr> " contains a comment') is True
