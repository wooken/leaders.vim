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


def test_extract_comments_and_mappings():
    vimrc_in = [
        '" Neomake: open location window',
        'nnoremap <LEADER>lo :lopen<CR>',
        'set tabstop=4               " number of spaces that a <tab> in the file counts for',
        'set shiftwidth=4            " number of spaces to use for each step of (auto)indent',
        '" Neomake: close location window',
        'nnoremap <LEADER>lc :lclose<CR>',
    ]
    assert leaders.extract_comments_and_mappings(vimrc_in) == [
        ('nnoremap <LEADER>lo :lopen<CR>', '" Neomake: open location window'),
        ('nnoremap <LEADER>lc :lclose<CR>', '" Neomake: close location window'),
    ]


def test_is_comment_basic():
    assert leaders.is_comment('" valid comment:.,!@#$%^&*()_+') is True
    assert leaders.is_comment('not a " comment') is False


def test_is_mapping_basic():
    for cmd in MAP_CMDS:
        assert leaders.is_mapping('{} <leader>c :Commands<cr>'.format(cmd)) is True
    assert leaders.is_mapping('this is just regular text') is False


def test_is_mapping_case_insensitive():
    for variation in LEADER_VARIATIONS:
        assert leaders.is_mapping('nnoremap {}c :Commands<CR>'.format(variation)) is True


def test_is_mapping_no_mapping_inline_comment_support():
    assert leaders.is_mapping('nnoremap <leader>c :Commands<cr> " contains an unsupported comment') is False
