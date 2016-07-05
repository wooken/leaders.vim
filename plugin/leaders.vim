if !has('python3')
    finish
endif

command! ListLeaders call ll#ListLeaders()
nnoremap <leader>l :ListLeaders<cr>
