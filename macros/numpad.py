# MACROPAD Hotkeys: Universal Numpad

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Numpad',
    'order': 2,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004166, '7    ', Keycode.KEYPAD_SEVEN),
        (0x004166, '8    ', Keycode.KEYPAD_EIGHT),
        (0x004166, '9    ', Keycode.KEYPAD_NINE ),
        # 2nd row ----------
        (0x004166, '4    ', Keycode.KEYPAD_FOUR),
        (0x004166, '5    ', Keycode.KEYPAD_FIVE),
        (0x004166, '6    ', Keycode.KEYPAD_SIX ),
        # 3rd row ----------
        (0x004166, '1    ', Keycode.KEYPAD_ONE  ),
        (0x004166, '2    ', Keycode.KEYPAD_TWO  ),
        (0x004166, '3    ', Keycode.KEYPAD_THREE),
        # 4th row ----------
        (0x004166, '0    ', Keycode.KEYPAD_ZERO  ),
        (0x640A66, '.    ', Keycode.KEYPAD_PERIOD),
        (0x663F0A, 'ENTER', Keycode.KEYPAD_ENTER )
    ]
}
