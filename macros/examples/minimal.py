# MACROPAD Hotkeys: Sample macro page with only the minimum settings

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse as MouseCode

from consumer import Toolbar
from mouse import Mouse
from sleep import Sleep
from midi import Midi

app = {
    'name' : 'Minimal Macro',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # 2nd row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # 3rd row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # 4th row ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        # encoder ----------
        (0x000000, '       ', []),
        (0x000000, '       ', []),
        (0x000000, '       ', []),
    ]
}
