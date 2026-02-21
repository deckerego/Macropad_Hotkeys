from unittest import mock
from key import Key

class MockCommand:
    def __init__(self):
        self.press = mock.Mock()

def test_press():
    macropad = mock.Mock()
    command = MockCommand()
    color = (0, 0, 0)
    key = Key(macropad, command, color)
    key.press()
    command.press.assert_called_once()
    