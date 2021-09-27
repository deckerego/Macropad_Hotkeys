import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect

class Display:
    def __init__(self, macropad):
        self.macropad = macropad

        self.macropad.display.auto_refresh = False

    def initialize(self):
        self.group = displayio.Group()
        for key_index in range(12):
            x = key_index % 3
            y = key_index // 3
            self.group.append(
                label.Label(terminalio.FONT,
                    text='',
                    color=0xFFFFFF,
                    anchored_position=((self.macropad.display.width - 1) * x / 2,
                    self.macropad.display.height - 1 - (3 - y) * 12),
                    anchor_point=(x / 2, 1.0)
                )
            )
        self.group.append(Rect(0, 0, self.macropad.display.width, 12, fill=0xFFFFFF))
        self.group.append(
            label.Label(
                terminalio.FONT,
                text='',
                color=0x000000,
                anchored_position=(self.macropad.display.width//2, -2),
                anchor_point=(0.5, 0.0)
            )
        )
        self.macropad.display.show(self.group)

    def sleep(self):
        self.macropad.display.auto_brightness = False
        self.macropad.display.brightness = 0
        self.macropad.display.show(displayio.Group())
        self.macropad.display.refresh()

    def resume(self):
        self.macropad.display.brightness = 1
        self.macropad.display.auto_brightness = True
        self.macropad.display.show(self.group)
        self.macropad.display.refresh()

    def setApp(self, app):
        self.group[13].text = app.name
        for i in range(12):
            if i < len(app.macros):
                self.group[i].text = app.macros[i][1]
            else:
                self.group[i].text = ''
        self.macropad.display.refresh()

    def setTitle(self, text):
        self.group[13].text = text
        for i in range(12):
            self.group[i].text = ''
        self.macropad.display.refresh()
