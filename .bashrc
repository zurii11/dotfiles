#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# fzf files
source /usr/share/fzf/completion.bash
source /usr/share/fzf/key-bindings.bash

# Set keyboard layouts
setxkbmap -model pc105 -layout us,ge -option grp:alt_shift_toggle

alias ls='ls --color=auto'
alias sail='./vendor/bin/sail'
alias postman='/home/zura/Postman/Postman/Postman'
# Temporary alias to enter psql in docker for sait
alias dp='docker exec -tiu postgres dashboard_pgsql_1 psql'
PS1='[\u@\h \W]\$ '
. "$HOME/.cargo/env"
