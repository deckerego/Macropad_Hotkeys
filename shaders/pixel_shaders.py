class PressedShader:
    MAX_FRAMES = 4
    neopixels = None
    key_index = None
    frame_index = None
    start_color = None

    def __init__(self, neopixels, key_index):
        self.neopixels = neopixels
        self.key_index = key_index
        if key_index < len(self.neopixels): # This is an addressable range
            self.start_color = neopixels[key_index]
            self.frame_index = PressedShader.MAX_FRAMES
        else:
            self.start_color = None
            self.frame_index = 0

    def tick(self, _, frames):
        self.frame_index -= frames
        if self.frame_index > 0:
            color_val =  0xFF * (self.frame_index / PressedShader.MAX_FRAMES)
            self.neopixels[self.key_index] = (color_val, color_val, color_val)
            self.neopixels.show()
        elif self.start_color:
            self.neopixels[self.key_index] = self.start_color
            self.neopixels.show()
        
    def done(self):
        return self.frame_index <= 0