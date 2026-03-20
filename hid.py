from commands import Commands, Command, Toolbar, Keyboard, Midi, Mouse, Pause, Sequence, Sleep
from mouse_extended import MouseAdapter
import time

class InputDeviceListener:
    MIDI_VELOCITY = 127
    sleeping = False

    def __init__(self, macropad):
        self.macropad = macropad
        self.mouse = MouseAdapter(macropad.mouse)
        self.sleeping = False
    
    def __del__(self):
        pass

    def register(self, _):
        pass

    def pressed(self, keys, index):
        key = keys[index]
        self.pressCommands(key.commands)

    def released(self, keys, index):
        key = keys[index]
        self.releaseCommands(key.commands)

    def pressCommands(self, commands: Commands):
        for command in commands:
            self.press(command)

    def releaseCommands(self, commands: Commands):
        for command in commands:
            self.release(command)

    def press(self, command: Command):
        if self.sleeping: return # Ignore any button presses until we wake up

        if isinstance(command, Keyboard): return self.pressKeyboard(command)
        elif isinstance(command, Sequence): return self.pressSequence(command)
        elif isinstance(command, Toolbar): return self.pressToolbar(command)
        elif isinstance(command, Mouse): return self.pressMouse(command)
        elif isinstance(command, Pause): return self.pressPause(command)
        elif isinstance(command, Midi): return self.pressMidi(command)
        elif isinstance(command, Sleep): return self.sleep(command)

    def release(self, command: Command):
        if isinstance(command, Keyboard): return self.releaseKeyboard(command)
        elif isinstance(command, Toolbar): return self.releaseToolbar(command)
        elif isinstance(command, Mouse): return self.releaseMouse(command)
        elif isinstance(command, Midi): return self.releaseMidi(command)
        elif isinstance(command, Sleep): return self.resume(command)
        
    def pressToolbar(self, command:Toolbar):
        if command.keycode < 0:
            self.macropad.consumer_control.release()
        else:
            self.macropad.consumer_control.press(command.keycode)

    def pressMouse(self, command:Mouse):
        if command.keycode < 0:
            self.mouse.release(command.keycode)
        elif command.keycode == MouseAdapter.PAN:
            self.mouse.move(pan=command.value)
        elif command.keycode == MouseAdapter.WHEEL:
            self.mouse.move(wheel=command.value)
        else:
            self.mouse.press(command.keycode)

    def pressMidi(self, command:Midi):
        if command.keycode < 0:
            self.macropad.midi.send(self.macropad.NoteOff(command.keycode, 0))
        else:
            self.macropad.midi.send(self.macropad.NoteOn(command.keycode, InputDeviceListener.MIDI_VELOCITY))

    def pressPause(self, command:Pause):
        time.sleep(command.keycode)

    def pressSequence(self, sequence:Sequence):
        for command in sequence:
            self.press(command)
        for command in sequence:
            self.release(command)

    def pressKeyboard(self, command:Keyboard):
        if not isinstance(command.keycode, int):
            self.macropad.keyboard_layout.write(command.keycode)
        elif command.keycode < 0:
            self.macropad.keyboard.release(command.keycode)
        else:
            self.macropad.keyboard.press(command.keycode)

    def releaseToolbar(self, command:Toolbar):
        self.macropad.consumer_control.release()

    def releaseMouse(self, command:Mouse):
        self.mouse.release(command.keycode)

    def releaseMidi(self, command:Midi):
        if command.keycode >= 0:
            self.macropad.midi.send(self.macropad.NoteOff(command.keycode, 0))

    def releaseKeyboard(self, command:Keyboard):
        if isinstance(command.keycode, int) and command.keycode >= 0:
            self.macropad.keyboard.release(command.keycode)

    def sleep(self, command:Sleep):
        self.sleeping = True

    def resume(self, command:Sleep):
        self.sleeping = False
