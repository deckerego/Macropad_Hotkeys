import time

BRIGHTNESS = 0.3

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

    @staticmethod
    def hexToTuple(color):
        return (color >> 16, (color >> 8) & 0xFF, color & 0xFF)

    @staticmethod
    def blend(color_fg, color_bg, alpha_fg):
        red_fg, green_fg, blue_fg = Pixels.hexToTuple(color_fg)
        red_bg, green_bg, blue_bg = Pixels.hexToTuple(color_bg)
        alpha_bg = 1.0 - alpha_fg
        color_result_alpha = 1 - (1 - alpha_fg) * (1 - alpha_bg)
        color_result_red = red_fg * alpha_fg / color_result_alpha + red_bg * alpha_bg * (1 - alpha_fg) / color_result_alpha
        color_result_green = green_fg * alpha_fg / color_result_alpha + green_bg * alpha_bg * (1 - alpha_fg) / color_result_alpha
        color_result_blue = blue_fg * alpha_fg / color_result_alpha + blue_bg * alpha_bg * (1 - alpha_fg) / color_result_alpha
        return (color_result_red, color_result_green, color_result_blue)
