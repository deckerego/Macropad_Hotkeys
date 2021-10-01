VELOCITY = 127

class Midi:
    def __init__(self, note):
        self.note = note

    def press(self, macropad):
        if self.note < 0:
            macropad.midi.send(macropad.NoteOff(self.note, 0))
        else:
            macropad.midi.send(macropad.NoteOn(self.note, VELOCITY))

    def release(self, macropad):
        if self.note >= 0:
            macropad.midi.send(macropad.NoteOff(self.note, 0))
