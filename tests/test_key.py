from unittest import mock
from unittest import TestCase
from key import Key

class MockCommand:
    def __init__(self):
        self.press = mock.Mock()
        self.release = mock.Mock()

class TestKey(TestCase):
    def test_press(self):
        macropad = mock.Mock()
        command = MockCommand()
        color = (0, 0, 0)
        key = Key(macropad, command, color)

        key.press()
        
        command.press.assert_called_once()
        command.release.assert_not_called()

    def test_release(self):
        macropad = mock.Mock()
        command = MockCommand()
        color = (0, 0, 0)
        key = Key(macropad, command, color)

        key.release()
        
        command.press.assert_not_called()
        command.release.assert_called_once()