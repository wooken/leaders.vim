if !has('python3')
    finish
endif

command! ListLeaders call leaders#ListLeaders()
