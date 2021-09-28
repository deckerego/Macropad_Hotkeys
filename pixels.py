BRIGHTNESS = 0.6

class Pixels:
    def __init__(self, macropad):
        self.pixels = macropad.pixels
        self.pixels.auto_write = False
        self.pixels.brightness = BRIGHTNESS

    def setApp(self, app):
        self.macros = app.macros

        for i in range(12):
            if i < len(self.macros):
                self.pixels[i] = self.macros[i][0]
            else:
                self.pixels[i] = 0
        self.pixels.show()

    def sleep(self):
        self.pixels.brightness = 0.0
        self.pixels.show()

    def resume(self):
        self.pixels.brightness = BRIGHTNESS
        self.pixels.show()

    def highlight(self, key_index, color):
        self.pixels[key_index] = color
        self.pixels.show()

    def reset(self, key_index):
        self.pixels[key_index] = self.macros[key_index][0]
        self.pixels.brightness = BRIGHTNESS
        self.pixels.show()
