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
        (0x5E4001, 'Up     ', [Keycode.SHIFT, ' ']  ),
        # 2nd row ----------
        (0x095E06, '< Tab  ', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x095E06, 'Tab >  ', [Keycode.CONTROL, Keycode.TAB]               ),
        (0x5E4001, 'Down   ', ' '),
        # 3rd row ----------
        (0x5E143E, 'Reload ', [Keycode.COMMAND, 'r']),
        (0x5E143E, 'Home   ', [Keycode.COMMAND, 'H']),
        (0x5E143E, 'Private', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0x01255E, 'GitHub ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'https://github.com/notifications\n']),
        (0x01255E, 'AWS    ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                            'http://console.aws.amazon.com\n']),
        (0x01255E, 'Feedly ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                             'https://feedly.com/\n']),
        # Rotary Encoder ---
        (0x000000, None, Sleep()),
        (0x000000, None, []),
        (0x000000, None, []),
    ]
}
