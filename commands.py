import time

class Command:
    @staticmethod
    def get(item):
        if isinstance(item, Toolbar):
            return item
        elif isinstance(item, Mouse):
            return item
        elif isinstance(item, Midi):
            return item
        elif isinstance(item, Sleep):
            return item
        elif isinstance(item, float):
            return Pause(item)
        else:
            return Keyboard(item)

class Keyboard:
    def __init__(self, key):
        self.key = key

    def press(self, state):
        macropad = state["macropad"]
        if not isinstance(self.key, int):
            macropad.keyboard_layout.write(self.key)
        elif self.key < 0:
            macropad.keyboard.release(self.key)
        else:
            macropad.keyboard.press(self.key)

    def release(self, state):
        if isinstance(self.key, int) and self.key >= 0:
            state["macropad"].keyboard.release(self.key)

class Toolbar:
    def __init__(self, keycode):
        self.keycode = keycode

    def press(self, state):
        if self.keycode < 0:
            state["macropad"].consumer_control.release()
        else:
            state["macropad"].consumer_control.press(self.keycode)

    def release(self, state):
        state["macropad"].consumer_control.release()

class Mouse:
    def __init__(self, keycode):
        self.keycode = keycode

    def press(self, state):
        if self.keycode < 0:
            state["macropad"].mouse.release(self.keycode)
        else:
            state["macropad"].mouse.press(self.keycode)

    def release(self, state):
        state["macropad"].mouse.release(self.keycode)

class Midi:
    VELOCITY = 127
    
    def __init__(self, note):
        self.note = note

    def press(self, state):
        macropad = state["macropad"]
        if self.note < 0:
            macropad.midi.send(macropad.NoteOff(self.note, 0))
        else:
            macropad.midi.send(macropad.NoteOn(self.note, Midi.VELOCITY))

    def release(self, state):
        macropad = state["macropad"]
        if self.note >= 0:
            macropad.midi.send(macropad.NoteOff(self.note, 0))

class Pause:
    def __init__(self, seconds):
        self.seconds = seconds

    def press(self, state):
        time.sleep(self.seconds)

    def release(self, state):
        pass

class Sleep:
    def __init__(self):
        pass

    def press(self, state):
        if state["sleeping"]:
            state["screen"].resume()
            state["pixels"].resume()
        else:
            state["screen"].sleep()
            state["pixels"].sleep()
        state["sleeping"] = not state["sleeping"]

    def release(self, state):
        pass
