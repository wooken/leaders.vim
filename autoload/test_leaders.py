import leaders

MAP_CMDS = [
    'map',
    'nmap',
    'noremap',
    'nnoremap',
]

def test_is_comment():
    cases = [
        ('" this is a comment', True),
        ('"" commented comment', False),
        ('" valid comment:.,!@#$%^&*()_+', True),
        ('not a " comment', False),
    ]
    for case, expected in cases:
        assert leaders.is_comment(case) is expected

def test_is_mapping_basic():
    for cmd in MAP_CMDS:
        assert leaders.is_mapping(f'{cmd} <leader>c :Commands<cr>') is True
    assert leaders.is_mapping('this is just regular text') is False

def test_is_mapping_ignore_commented_out():
    assert leaders.is_mapping('"noremap <leader>c :Commands<cr>') is False

def test_is_mapping_ctrl_commands():
    assert leaders.is_mapping('noremap <leader>c :Commands<cr><C-w><C-w>') is True

def test_is_mapping_multiword_commands():
    assert leaders.is_mapping('nnoremap <LEADER>co :botright copen<CR><C-w><C-w>') is True

def test_is_mapping_case_insensitive():
    assert leaders.is_mapping(f'nnoremap <LEaDeR>c :Commands<CR>') is True

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
