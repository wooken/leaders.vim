import leaders
import re

VIMRC = """
map <C-c> <ESC><ESC>
imap <C-c> <ESC><ESC>

nnoremap <LEADER>, :Next<CR>
nnoremap <LEADER>. :next<CR>
" Neomake: open location window
nnoremap <LEADER>lo :lopen<CR>
Plug 'tpope/vim-dispatch'
" vim-dispatch: Dispatch
nnoremap <LEADER>r :w<CR>:Dispatch<CR>
" vim-dispatch: open quickfix window
nnoremap <LEADER>co :Copen<CR>
" vim-dispatch: close quickfix window
nnoremap <LEADER>cc :cclose<CR>
" Python
autocmd FileType python setlocal
            \ nosmartindent  " pep8-indent comments
"""


def test_final_output():
    matches = leaders.extract_comments_and_mappings(VIMRC.split('\n'))
    output = leaders.generate_output_list(matches)

    assert (',', ':Next<CR>') in output
    assert ('.', ':next<CR>') in output
    assert ('lo', 'Neomake: open location window') in output
    assert ('r', 'vim-dispatch: Dispatch') in output
    assert ('co', 'vim-dispatch: open quickfix window') in output
    assert ('cc', 'vim-dispatch: close quickfix window') in output
