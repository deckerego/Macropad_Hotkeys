from key import Key

BRIGHTNESS = 0.3

class Keys:
    LAUNCH = -1
    ENC_BUTTON = 12
    ENC_LEFT = 13
    ENC_RIGHT = 14
    MAX_LEDS = 12
    MAX_KEYS = 14

    def __init__(self, macropad, app):
        self.app = app
        self.keys = [Keys.MAX_KEYS]
        for i in range(len(self.app.macros)):
            color, label, macro = self.app.macros[i]
            self.keys[i] = Key(None, macro, label, color)

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