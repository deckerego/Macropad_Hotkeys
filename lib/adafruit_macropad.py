class MacroPad:
    def __init__(self):
        self.keyboard = Keyboard()
        self.encoder_switch_debounced = EncoderSwitch() 
        self.display = Display()

class Display:
    def __init__(self):
        self.width = 0
        self.height = 0

    def release_all(self):
        return
    
    def refresh(self):
        return

class Keyboard:
    def __init__(self):
        return

    def release_all(self):
        return

class EncoderSwitch:
    def __init__(self):
        return
    
    def update(self):
        return