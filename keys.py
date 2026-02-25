from key import Key
from commands import Command

BRIGHTNESS = 0.3

class Keys:
    LAUNCH = -1
    ENC_BUTTON = 12
    ENC_LEFT = 13
    ENC_RIGHT = 14
    MAX_LEDS = 12

    def __init__(self, macropad, app):
        self.app = app
        self.keys = []
        for i in range(len(self.app.macros)):
            color, label, sequence = self.app.macros[i]
            command = Command.get(sequence)
            self.keys += [Key(None, command, label, color)]

        self.macropad = macropad
        self.pixels = macropad.pixels
        self.pixels.auto_write = False
        self.pixels.brightness = BRIGHTNESS

    def __del__(self):
        return

    def press(self, key_index):
        return self.keys[key_index].press()

    def release(self, key_index):
        return self.keys[key_index].release()