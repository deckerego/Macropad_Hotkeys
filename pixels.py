from commands import Sleep

class PixelListener:
    BRIGHTNESS = 0.3
    MAX_LEDS = 12

    def __init__(self, macropad):
        self.pixels = macropad.pixels
        self.pixels.auto_write = False
        self.pixels.brightness = PixelListener.BRIGHTNESS
        self.keycolors = []

    def __del__(self):
        self.pixels.clear()

    def initialize(self):
        self.keycolors = []
        for i in range(PixelListener.MAX_LEDS):
            if i < len(self.keycolors):
                self.pixels[i] = self.keycolors[i]
            else:
                self.pixels[i] = 0x000000
        self.pixels.show()

    def register(self, keys):
        self.keycolors = list(map(lambda k: k.color, keys))
        for i in range(PixelListener.MAX_LEDS):
            if i < len(self.keycolors):
                self.pixels[i] = self.keycolors[i]
            else:
                self.pixels[i] = 0x000000
        self.pixels.show()

    def pressed(self, keys, index):
        self.highlight(index)

        commands = keys[index].commands
        if isinstance(commands[0], Sleep):
            self.sleep()

    def released(self, keys, index):
        self.reset(index)

        commands = keys[index].commands
        if isinstance(commands[0], Sleep):
            self.resume()

    def sleep(self):
        self.pixels.brightness = 0.0
        self.pixels.show()

    def resume(self):
        self.pixels.brightness = PixelListener.BRIGHTNESS
        self.pixels.show()

    def highlight(self, key_index, color=0xFFFFFF):
        if key_index >= PixelListener.MAX_LEDS: return
        self.pixels[key_index] = color
        self.pixels.show()

    def reset(self, key_index):
        if key_index >= PixelListener.MAX_LEDS: return
        self.pixels[key_index] = self.keycolors[key_index] if key_index < len(self.keycolors) else 0x000000
        self.pixels.brightness = PixelListener.BRIGHTNESS
        self.pixels.show()
