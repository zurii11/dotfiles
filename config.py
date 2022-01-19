# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

ph = "urxvt"

layout_theme = {
	"margin": 4,
	"border_focus_stack": "dbb0b0",
	"border_focus": "bc7373"
}

groups = [Group(i) for i in "123456789"]

colours = [["#141414", "#141414"], # Background
		   ["#FFFFFF", "#FFFFFF"], # Foreground
		   ["#848484", "#848484"], # Grey Colour
		   ["#E35374", "#E35374"],
		   ["#98C379", "#98C379"],
		   ["#F0C674", "#F0C674"],
		   ["#61AFEF", "#61AFEF"],
		   ["#C678DD", "#C678DD"],
		   ["#56B6BC", "#56B6BC"]]

def changeMarginPlus(qtile):
    max = 40
    layout = qtile.current_group.layout

    if layout.margin < max:
        layout.margin += 4

def changeMarginMinus(qtile):
    min = 0
    layout = qtile.current_group.layout

    if layout.margin > min:
        layout.margin -= 4


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
	
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 5- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 5+ unmute")),
	
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

    # Rofi
    Key([mod], "a", lazy.spawn("rofi -show run")),

    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Change margin
    Key([mod], "equal", lazy.function(changeMarginPlus)),
    Key([mod], "minus", lazy.function(changeMarginMinus)),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

widget_defaults = dict(
	background= colours[0],
	foreground=colours[1],
	font="SF Pro Text Regular",
	fontsize=14,
	padding=1
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
					highlight_method='line',
					active='E3FF22',
					inactive=colours[6],
					padding=0,
					margin=2,
					this_current_screen_border=colours[7],
					urgent_alert_method='text',
					disable_drag=True,
					invert_mouse_wheel=True
				),
				widget.Sep(
					foreground=colours[2],
					linewidth=1,
					padding=10
				),
                widget.KeyboardLayout(),
                widget.Sep(
                    foreground=colours[2],
                    linewidth=1,
                    padding=10
                ),
                widget.WindowName(),
                widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[3],
	            	fontsize=14,
	            	padding=0,
	            	text=' '
	            ),
	            widget.CPU(
	            	foreground=colours[3],
	            	format='{load_percent}%',
	            	update_interval=1.0
	            ),
	            widget.Sep(
	            	foreground=colours[2],
	            	linewidth=1,
	            	padding=10
	            ),
	            widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[4],
	            	fontsize=14,
	            	padding=0,
	            	text='﬙ '
	            ),
	            widget.Memory(
	            	foreground=colours[4],
	            	format='{MemUsed} MB'
	            ),
	            widget.Sep(
	            	foreground=colours[2],
	            	linewidth=1,
	            	padding=10
	            ),
	            widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[5],
	            	fontsize=14,
	            	padding=0,
	            	text=' '
	            ),
	            widget.CheckUpdates(
	            	colour_have_updates=colours[5],
	            	colour_no_updates=colours[5],
	            	custom_command='checkupdates+aur',
	            	display_format='{updates} Updates',
	            	no_update_string='Up to date!',
	            	update_interval=900
	            ),
	            widget.Sep(
	            	foreground=colours[2],
	            	linewidth=1,
	            	padding=10
	            ),
					            widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[5],
	            	fontsize=12,
	            	padding=0,
	            	text=' '
	            ),
	            widget.Backlight(
	            	foreground=colours[5],
	            	foreground_alert=colours[3],
	            	backlight_name='intel_backlight', # ls /sys/class/backlight/
	            	change_command='brightnessctl set {0}',
	            	step=5
	            ),
				widget.Sep(
					foreground=colours[2],
					linewidth=1,
					padding=10
				),
	            widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[6],
	            	fontsize=14,
	            	padding=0,
	            	text='墳 '
	            ),
	            widget.Volume(
	            	foreground=colours[6],
	            	step=5
	            ),
	            widget.Sep(
	            	foreground=colours[2],
	            	linewidth=1,
	            	padding=10
	            ),
	            widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[7],
	            	fontsize=14,
	            	padding=0,
	            	text='爵 '
	            ),
	            widget.Net(
	            	foreground=colours[7],
	            	interface='wlan0',
	            	format='{down}  '
	            	),
				widget.Sep(
					foreground=colours[2],
					linewidth=1,
					padding=10
				),
	            widget.Battery(
	            	font="JetBrainsMono Nerd Font Regular",
	            	fontsize=14,
	            	padding=0,
	            	foreground=colours[7],
	            	charge_char=' ',
	            	discharge_char=' ',
	            	empty_char=' ',
	            	full_char=' ',
	            	unknown_char=' ',
	            	format='{char}',
	            	low_foreground=colours[3],
	            	low_percentage=0.2,
	            	show_short_text=False
	            ),
	            widget.Battery(
	            	foreground=colours[7],
	            	format='{percent:2.0%}',
	            	low_foreground=colours[3],
	            	low_percentage=0.2,
	            	notify_below=20,
	            ),
	            widget.Sep(
	            	foreground=colours[2],
	            	linewidth=1,
	            	padding=10
	            ),
	            widget.TextBox(
	            	font="JetBrainsMono Nerd Font Regular",
	            	foreground=colours[8],
	            	fontsize=14,
	            	padding=0,
	            	text=' '
	            ),
	            widget.Clock(
	            	foreground=colours[8],
	            	format='%a %b %d  %I:%M %P    '
	            ),
                        ],
                        24,
                    ),
                ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
