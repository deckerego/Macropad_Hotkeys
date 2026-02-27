import time

class Commands:
    def __init__(self, macro):
        self.commands = []
        if isinstance(macro, list):
            for item in macro:
                self.commands += Commands.build(item)
        else:
            self.commands += [macro]

    def __bool__(self):
        return len(self.commands) > 0
    
    def __iter__(self):
        return iter(self.commands)

    def __getitem__(self, index):
        return self.commands[index]

    def __len__(self):
        return len(self.commands)

    @staticmethod
    def build(item):
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
        elif isinstance(item, list):
            return Sequence(item)
        else:
            return Keyboard(item)

class Command:
    def __init__(self, keycode):
        self.keycode = keycode

class Sequence(Command):
    def __init__(self, keycodes):
        self.commands = []
        for keycode in keycodes:
            self.commands += [Commands.build(keycode)]

    def __bool__(self):
        return len(self.commands) > 0
    
    def __iter__(self):
        return iter(self.commands)

    def __getitem__(self, index):
        return self.commands[index]

    def __len__(self):
        return len(self.commands)

class Keyboard(Command):
    def __init__(self, key):
        self.keycode = key

class Toolbar(Command):
    def __init__(self, keycode):
        self.keycode = keycode

class Mouse(Command):
    def __init__(self, keycode):
        self.keycode = keycode

class Midi(Command):
    def __init__(self, note):
        self.keycode = note

class Pause(Command):
    def __init__(self, seconds):
        self.keycode = seconds

class Sleep(Command):
    def __init__(self):
        pass
