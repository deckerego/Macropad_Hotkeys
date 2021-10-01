# MACROPAD Hotkeys: Safari web browser for Mac

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'MacOS Safari',
    'order': 4,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A2B5E, '< Back ', [Keycode.COMMAND, '[']),
        (0x0A2B5E, 'Fwd >  ', [Keycode.COMMAND, ']']),
        (0x5E4001, 'Up     ', [Keycode.SHIFT, ' ']),
        # 2nd row ----------
        (0x095E06, '< Tab  ', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x095E06, 'Tab >  ', [Keycode.CONTROL, Keycode.TAB]),
        (0x5E4001, 'Down   ', ' '),
        # 3rd row ----------
        (0x5E143E, 'Reload ', [Keycode.COMMAND, 'r']),
        (0x5E143E, 'Home   ', [Keycode.COMMAND, 'H']),
        (0x5E143E, 'Private', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0x01255E, 'GitHub ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'https://github.com/notifications\n']),
        (0x01255E, 'Trello ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'https://trello.com/anvlsafe\n']),
        (0x01255E, 'Release', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                             'https://sites.google.com/anvl.com/release-dashboard\n'])
    ]
}
