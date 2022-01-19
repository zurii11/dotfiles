#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

export EDITOR="nano"
export TERMINAL="urxvt"
export BROWSER="firefox"
export PATH=$PATH:/usr/bin/

#setxkbmap -model pc105 -layout us,ge -variant , -option grp:alt_shift_toggle

[[ $(fgconsole 2>/dev/null) == 1 ]] && exec startx -- vt1
. "$HOME/.cargo/env"
