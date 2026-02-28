import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from commands import Sleep

class ScreenListener:
    MAX_LABELS = 12
    sleeping = False

    def __init__(self, macropad):
        self.display = macropad.display
        self.display.auto_refresh = False
        sleeping = False

    def __del__(self):
        self.display = None

    def initialize(self):
        self.group = displayio.Group()
        for key_index in range(ScreenListener.MAX_LABELS):
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
        if self.sleeping: return
        self.display.brightness = 0
        self.display.root_group = displayio.Group()
        self.display.refresh()
        self.sleeping = True

    def resume(self):
        if not self.sleeping: return
        self.display.brightness = 1
        self.display.root_group = self.group
        self.display.refresh()
        self.sleeping = False

    def highlight(self, key_index):
        if key_index >= ScreenListener.MAX_LABELS: return
        self.group[key_index].color = 0x000000
        self.group[key_index].background_color = 0xFFFFFF
        self.display.refresh()
    
    def reset(self, key_index):
        if key_index >= ScreenListener.MAX_LABELS: return
        self.group[key_index].color = 0xFFFFFF
        self.group[key_index].background_color = 0x000000
        self.display.refresh()
