import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect

class ScreenListener:
    def __init__(self, macropad):
        self.display = macropad.display
        self.display.auto_refresh = False

    def __del__(self):
        self.display = None

    def initialize(self):
        self.group = displayio.Group()
        for key_index in range(12):
            x = key_index % 3
            y = key_index // 3
            self.group.append(
                label.Label(terminalio.FONT,
                    text='',
                    color=0xFFFFFF,
                    background_color=0x000000,
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
        self.display.root_group = self.group

    def setTitle(self, text):
        self.group[13].text = text
        self.display.refresh()

    def register(self, keys):
        for i in range(12):
            if i < len(keys):
                self.group[i].text = keys[i].label
            else:
                self.group[i].text = ''
        self.display.refresh()

    def pressed(self, _, index):
        self.highlight(index)

    def released(self, _, index):
        self.reset(index)

    def sleep(self):
        self.display.brightness = 0
        self.display.root_group = displayio.Group()
        self.display.refresh()

    def resume(self):
        self.display.brightness = 1
        self.display.root_group = self.group
        self.display.refresh()

    def highlight(self, key_index):
        self.group[key_index].color = 0x000000
        self.group[key_index].background_color = 0xFFFFFF
        self.display.refresh()
    
    def reset(self, key_index):
        self.group[key_index].color = 0xFFFFFF
        self.group[key_index].background_color = 0x000000
        self.display.refresh()
