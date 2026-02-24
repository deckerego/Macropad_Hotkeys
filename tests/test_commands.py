from unittest import TestCase
from keyboard import Keyboard # DEPRECATED switch to command module after 3.x
from pause import Pause       # DEPRECATED switch to command module after 3.x
from mouse import Mouse       # DEPRECATED switch to command module after 3.x
from commands import Command

class TestKey(TestCase):
    def test_alpha(self):
        command = Command.get('O')
        self.assertIsInstance(command, Keyboard)

    def test_float(self):
        command = Command.get(1.0)
        self.assertIsInstance(command, Pause)
    
    def test_mouse(self):
        command = Command.get(Mouse(0))
        self.assertIsInstance(command, Mouse)
