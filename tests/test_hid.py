from unittest import mock, TestCase
from keys import Keys, Key
from hid import InputDeviceListener
from adafruit_hid.keycode import Keycode

class MockKeys(Keys):
    def __init__(self, listeners, app):
        self.keys = [
            Key(Keycode.A),
            Key([Keycode.A, Keycode.B]),
            Key([[Keycode.SHIFT, Keycode.A], Keycode.B]),
        ]

class MockMacroPad:
    def __init__(self):
        self.keyboard = MockKeyboard()
        self.keyboard_layout = MockKeyboardLayout()

class MockKeyboard:
    def __init__(self):
        self.press = mock.Mock()
        self.release = mock.Mock()
        self.release_all = mock.Mock()

class MockKeyboardLayout:
    write = mock.Mock()

class TestInputDevice(TestCase):
    def test_init_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)

        macropad.keyboard.release_all.assert_called_once()        

    def test_press_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.pressed(keys, 0)

        macropad.keyboard.press.assert_called_once()
        macropad.keyboard.release.assert_not_called()

    def test_release_keyboard(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        listener = InputDeviceListener(macropad)
        listener.register(keys)
        listener.released(keys, 0)

        macropad.keyboard.release.assert_called_once()
        macropad.keyboard.press.assert_not_called()
