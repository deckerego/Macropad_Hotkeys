from unittest import TestCase, mock
from adafruit_hid.keycode import Keycode
from keyboard import Keyboard # pyright: ignore[reportMissingImports, reportMissingModuleSource] Switch to command module after 3.x
from pause import Pause       # pyright: ignore[reportMissingImports, reportMissingModuleSource] Switch to command module after 3.x
from mouse import Mouse       # pyright: ignore[reportMissingImports, reportMissingModuleSource] Switch to command module after 3.x
from commands import Commands, Sequence

class MockKeycode(Keycode):
    MOCK_1 = mock.Mock()
    MOCK_2 = mock.Mock()
    MOCK_3 = mock.Mock()
    MOCK_4 = mock.Mock()

class TestFactory(TestCase):
    def test_alpha(self):
        command = Commands.build('O')
        self.assertIsInstance(command, Keyboard)

    def test_float(self):
        command = Commands.build(1.0)
        self.assertIsInstance(command, Pause)
    
    def test_mouse(self):
        command = Commands.build(Mouse(0))
        self.assertIsInstance(command, Mouse)

class TestCommands(TestCase):
    def test_iterator(self):
        commands = Commands([[MockKeycode.MOCK_1, MockKeycode.MOCK_2], [MockKeycode.MOCK_3, MockKeycode.MOCK_2, MockKeycode.MOCK_1], MockKeycode.MOCK_4])
        command_index = []
        for command in commands:
            command_index += [command]
        
        self.assertIsInstance(command_index[0], Sequence)
        self.assertIsInstance(command_index[1], Sequence)
        self.assertIsInstance(command_index[2], Keyboard)
