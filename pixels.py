from commands import Sleep

class PixelListener:
    BRIGHTNESS = 0.3
    MAX_LEDS = 12
    sleeping = False
    shaders = None
    pixels = None

    def __init__(self, macropad):
        self.pixels = macropad.pixels
        self.pixels.auto_write = False
        self.pixels.brightness = PixelListener.BRIGHTNESS
        self.keycolors = []
        self.shaders = []
        self.sleeping = False

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
        # Ignore any button presses until we wake up
        if self.sleeping: return

        self.highlight(index)

        commands = keys[index].commands
        if not commands: return

        if isinstance(commands[0], Sleep):
            self.sleep()

    def released(self, keys, index):
        self.reset(index)

        commands = keys[index].commands
        if not commands: return
        
        if isinstance(commands[0], Sleep):
            self.resume()
    
    def tick(self, keys, frames):
        for shader in self.shaders:
            shader.tick(keys, frames)
        self.shaders = list(filter(lambda s: not s.done(), self.shaders))
    
    def sleep(self):
        if self.sleeping: return
        self.pixels.brightness = 0.0
        self.pixels.show()
        self.sleeping = True

    def resume(self):
        if not self.sleeping: return
        self.pixels.brightness = PixelListener.BRIGHTNESS
        self.pixels.show()
        self.sleeping = False

    def highlight(self, key_index):
        self.shaders += [BlinkShader(self, key_index)]

    def reset(self, key_index):
        pass

class BlinkShader:
    listener = None
    key_index = None
    frame_index = None

    def __init__(self, listener, key_index, frames=5):
        self.listener = listener
        self.key_index = key_index
        self.frame_index = frames

    def tick(self, _, frames):
        self.frame_index -= frames
        if self.key_index >= PixelListener.MAX_LEDS: return

        if self.frame_index > 0:
            self.listener.pixels[self.key_index] = 0xFFFFFF
            self.listener.pixels.show()
        else:
            self.listener.pixels[self.key_index] = self.listener.keycolors[self.key_index] if self.key_index < len(self.listener.keycolors) else 0x000000
            self.listener.pixels.brightness = PixelListener.BRIGHTNESS
            self.listener.pixels.show()
        
    def done(self):
        return self.frame_index <= 0