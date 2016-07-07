import leaders
import re

MAP_CMDS = [
    'map',
    'nmap',
    'noremap',
    'nnoremap',
]

LEADER_VARIATIONS = [
    '<Leader>',
    '<LEADER>',
    '<leader>',
]


def test_map_re():
    assert re.match(leaders.MAP_RE, '') is None
    for cmd in MAP_CMDS:
        assert re.match(leaders.MAP_RE, cmd) is not None
    assert re.match(leaders.MAP_RE, 'notvalidcmd') is None


def test_leader_re():
    assert re.match(leaders.LEADER_RE, '') is None
    for variation in LEADER_VARIATIONS:
        assert re.match(leaders.LEADER_RE, variation) is not None
    assert re.match(leaders.LEADER_RE, '<notvalidleader>') is None


def test_mapping_re():
    assert re.match(leaders.MAPPING_RE, '') is None
    assert re.match(leaders.MAPPING_RE, 'll') is not None
    assert re.match(leaders.MAPPING_RE, 'idjf') is not None


def test_cmd_re():
    assert re.match(leaders.CMD_RE, '') is None
    assert re.match(leaders.CMD_RE, 'validcmd') is not None


def test_comment_re():
    assert re.match(leaders.COMMENT_RE, '') is None
    assert re.match(leaders.COMMENT_RE, '" this is a valid comment') is not None
    assert re.match(leaders.COMMENT_RE, r'" this is also \:=<>() valid') is not None


def test_extract_mapping_and_info():
    assert leaders.extract_mapping_and_info('nnoremap <LEADER>c :Commands<CR>') == ['c', ':Commands<CR>']
    assert leaders.extract_mapping_and_info('nnoremap <LEADER>] :lnext<CR>           " go to next error/warning') == [']', 'go to next error/warning']


def test_is_map_function_basic():
    for cmd in MAP_CMDS:
        assert leaders.is_map_function('{} <leader>c :Commands<cr>'.format(cmd)) is True
    assert leaders.is_map_function('this is just regular text') is False


def test_is_map_function_case_insensitive():
    for variation in LEADER_VARIATIONS:
        assert leaders.is_map_function('nnoremap {}c :Commands<CR>'.format(variation)) is True


def test_is_map_function_comments():
    assert leaders.is_map_function('nnoremap <leader>c :Commands<cr> " contains a comment') is True
