let s:autoload_path = fnamemodify(resolve(expand('<sfile>:p')), ':h')
function! leaders#ListLeaders()
    execute 'py3file ' . s:autoload_path . '/leaders.py'
endfunc
