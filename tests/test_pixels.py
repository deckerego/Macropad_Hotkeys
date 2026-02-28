from unittest import mock, TestCase
from keys import Keys, Key
from pixels import PixelListener
from commands import Commands, Sleep

class MockKeys(Keys):
    def __init__(self, listeners, app):
        self.keys = [
            Key(mock.Mock(), "", 0x0000FF),
            Key(mock.Mock(), "", 0x00FF00),
            Key(mock.Mock(), "", 0xFF0000),
        ]

class MockMacroPad:
    def __init__(self):
        self.pixels = MockPixels()

class MockPixels:
    def __init__(self):
        self.auto_write = True
        self.brightness = 1.0
        self.leds = [0x000000] * 12
        self.show = mock.Mock()
    def __getitem__(self, key):
        return self.leds[key]
    def __setitem__(self, key, value):
        self.leds[key] = value
    def clear(self):
        self.leds.clear()

class TestPixels(TestCase):
    def test_initalize(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.initialize()

        self.assertEqual(pixels.pixels[1], 0x000000)

    def test_sleep(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.sleep()

        self.assertEqual(pixels.pixels.brightness, 0.0)

    def test_sleep_twice(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.sleep()
        pixels.sleep()

        pixels.pixels.show.assert_called_once()

    def test_resume(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.sleep()
        pixels.resume()

        self.assertEqual(pixels.pixels.brightness, PixelListener.BRIGHTNESS)

    def test_resume_twice(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.sleep()

        pixels.pixels.show.reset_mock()
        pixels.resume()
        pixels.resume()

        pixels.pixels.show.assert_called_once()

    def test_highlight(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.highlight(1)

        self.assertEqual(pixels.pixels[0], 0x000000)
        self.assertEqual(pixels.pixels[1], 0xFFFFFF)

    def test_reset(self):
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.highlight(1)
        pixels.reset(1)

        self.assertEqual(pixels.pixels[0], 0x000000)
        self.assertEqual(pixels.pixels[1], 0x000000)

    def test_set_keys(self):
        keys = MockKeys([], None)
        macropad = MockMacroPad()
        pixels = PixelListener(macropad)
        pixels.register(keys)

        self.assertEqual(pixels.pixels[0], 0x0000FF)
        self.assertEqual(pixels.pixels[1], 0x00FF00)
        self.assertEqual(pixels.pixels[2], 0xFF0000)
        self.assertEqual(pixels.pixels[3], 0x000000)

    def test_press(self):
        keys = MockKeys([], None)
        class MockPixelListener(PixelListener):
            highlight = mock.Mock()
            reset = mock.Mock()
        macropad = MockMacroPad()
        pixels = MockPixelListener(macropad)
        pixels.register(keys)
        pixels.pressed(keys, 1)

        pixels.highlight.assert_called_once()
        pixels.reset.assert_not_called()

    def test_release(self):
        keys = MockKeys([], None)
        class MockPixelListener(PixelListener):
            highlight = mock.Mock()
            reset = mock.Mock()
        macropad = MockMacroPad()
        pixels = MockPixelListener(macropad)
        pixels.register(keys)
        pixels.released(keys, 1)

        pixels.reset.assert_called_once()
        pixels.highlight.assert_not_called()

    def test_sleep_command(self):
        keys = MockKeys([], None)
        keys[0].commands = Commands(Sleep())
        class MockPixelListener(PixelListener):
            highlight = mock.Mock()
            reset = mock.Mock()
            sleep = mock.Mock()
        macropad = MockMacroPad()
        screen = MockPixelListener(macropad)
        screen.register(keys)
        screen.pressed(keys, 0)

        screen.sleep.assert_called_once()
