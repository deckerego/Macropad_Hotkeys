import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect

class Display:
    def __init__(self, macropad):
        self.display = macropad.display
        self.display.auto_refresh = False

    def initialize(self):
        self.group = displayio.Group()
        for key_index in range(12):
            x = key_index % 3
            y = key_index // 3
            self.group.append(
                label.Label(terminalio.FONT,
                    text='',
                    color=0xFFFFFF,
                    anchored_position=((self.display.width - 1) * x / 2,
                    self.display.height - 1 - (3 - y) * 12),
                    anchor_point=(x / 2, 1.0)
                )
            )
        self.group.append(Rect(0, 0, self.display.width, 12, fill=0xFFFFFF))
        self.group.append(
            label.Label(
                terminalio.FONT,
                text='',
                color=0x000000,
                anchored_position=(self.display.width//2, -2),
                anchor_point=(0.5, 0.0)
            )
        )
        self.display.show(self.group)

    def sleep(self):
        self.display.auto_brightness = False
        self.display.brightness = 0
        self.display.show(displayio.Group())
        self.display.refresh()

    def resume(self):
        self.display.brightness = 1
        self.display.auto_brightness = True
        self.display.show(self.group)
        self.display.refresh()

    def setApp(self, app):
        self.group[13].text = app.name
        for i in range(12):
            if i < len(app.macros):
                self.group[i].text = app.macros[i][1]
            else:
                self.group[i].text = ''
        self.display.refresh()

    def setTitle(self, text):
        self.group[13].text = text
        for i in range(12):
            self.group[i].text = ''
        self.display.refresh()
