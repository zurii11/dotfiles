source $HOME/.config/nvim/themes/airline.vim

" Tab stuff
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent

set cmdheight=2
set guicursor=
set nowrap
set nu rnu
set hidden
set ic
set nohlsearch
set incsearch
set noswapfile
set nobackup
set noerrorbells
set scrolloff=8

"let g:codedark_term256=1
"set t_ut=

call plug#begin('~/.vim/plugged')

Plug 'tomasiser/vim-code-dark'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'airblade/vim-rooter'
Plug 'rust-lang/rust.vim'
"Plug 'autozimu/LanguageClient-neovim', { 'do': ':UpdateRemotePlugins'}
Plug 'ziglang/zig.vim'

call plug#end()

"autocmd BufReadPost *.rs setlocal filetype=rust

"let g:LanguageClient_serverCommands = {
"\   'rust': ['rustup', 'run', 'nightly', 'rls'],
"\ }

"let g:LanguageClient_autoStart = 1

"nnoremap <silent> K :call LanguageClient_textDocument_hover()
"nnoremap <silent> gd :call LanguageClient_textDocument_definition()
"nnoremap <silent> <F2> :call LanguageClient_textDocument_rename() 

let g:coc_global_extensions = ['coc-json', 'coc-css', 'coc-css', 'coc-eslint', 'coc-snippets', 'coc-tsserver', 'coc-pairs', '@yaegassy/coc-intelephense',]
let g:coc_explorer_global_presets = {
\   'floating': {
\       'position': 'floating',
\       'open-action-strategy': 'sourceWindow',
\   }
\ }
" buffer navigation   
nnoremap <silent> <A-l> :bnext<CR>
nnoremap <silent><A-h> :bprevious<CR>
nnoremap <silent><A-k> :bdelete<CR>

" fzf keybindings
let g:fzf_action = {
\	'ctrl-t': 'tab split',
\	'ctrl-x': 'split',
\	'ctrl-v': 'vsplit' }

map <C-f> :Files<CR>
map <S-f> :Rg<CR>

" explorer stuff
nnoremap <silent><space>e :CocCommand explorer<CR>
nnoremap <silent><space>f :CocCommand explorer --preset floating<CR>
autocmd BufEnter * if (winnr("$") == 1 && &filetype == 'coc-explorer') | q | endif

" Use tab to trigger completion with characters ahead and navigate
inoremap <silent><expr> <A-TAB>
    \ pumvisible() ? "\<C-n>" :
    \ <SID>check_back_space() ? "\<A-TAB>" :
    \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
    let col = col('.') - 1
    return !col || getline('.')[col - 1] =!# '\s'
endfunction

" Use <C-space> to trigger completion
if has('nvim')
    inoremap <silent><expr> <c-space> coc#refresh()
else
    inoremap <silent><expr> <c-@> coc#refresh()
endif

" Make Enter to autoselect first item in completion
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
    \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

" GoTo code navigation
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
    if (index(['Vim','help'], &filetype) >= 0)
        execute 'h '.expand('<cword>')
    elseif (coc#rpc#ready())
        call CocActionAsync('doHover')
    else
        execute '!' . $keywordprg . " " . expand('<cword>')
    endif
endfunction

" Highlight the symbol and it's references when holding the cursor
autocmd CursorHold * silent call CocActionAsync('highlight')

" Add NeoVim's native statusline support
"set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

set t_Co=256
colorscheme codedark
