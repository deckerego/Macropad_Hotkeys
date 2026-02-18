from key import Key

BRIGHTNESS = 0.3

class Keys:
    LAUNCH = -1
    ENC_BUTTON = 12
    ENC_LEFT = 13
    ENC_RIGHT = 14
    MAX_LEDS = 12

    def __init__(self, macropad, app):
        self.app = app
        for i in range(Keys.MAX_LEDS):
            macro = self.app.macros[i][2]
            color = self.app.macros[i][0]
            self.keys[i] = Key(None, color, macro)

        self.macropad = macropad
        self.pixels = macropad.pixels
        self.pixels.auto_write = False
        self.pixels.brightness = BRIGHTNESS

    def __del__(self):
        return
