from unittest import mock
from unittest import TestCase
from screen import Screen
from adafruit_display_shapes.rect import Rect

class MockMacroPad:
    def __init__(self):
        self.display = MockDisplay()

class MockDisplay:
    def __init__(self):
        self.width = 128
        self.height = 64
        self.release_all = mock.Mock()
        self.refresh = mock.Mock()

class TestScreen(TestCase):
    def test_initalize(self):
        macropad = MockMacroPad()
        screen = Screen(macropad)
        screen.initialize()

        elementCount = len(screen.display.root_group)
        self.assertEqual(screen.display.root_group[0].color, 0xFFFFFF)
        self.assertIsInstance(screen.display.root_group[elementCount - 2], Rect)
        self.assertEqual(screen.display.root_group[elementCount - 1].color, 0x000000)

    def test_sleep(self):
        macropad = MockMacroPad()
        screen = Screen(macropad)
        screen.initialize()
        screen.sleep()

        self.assertEqual(len(screen.display.root_group), 0)
        self.assertEqual(screen.display.brightness, 0)

    def test_resume(self):
        macropad = MockMacroPad()
        screen = Screen(macropad)
        screen.initialize()
        screen.sleep()
        screen.resume()

        self.assertEqual(len(screen.display.root_group), 14)
        self.assertEqual(screen.display.brightness, 1)

    def test_highlight(self):
        macropad = MockMacroPad()
        screen = Screen(macropad)
        screen.initialize()
        screen.highlight(1)

        self.assertEqual(screen.display.root_group[0].color, 0xFFFFFF)
        self.assertEqual(screen.display.root_group[0].background_color, 0x000000)
        self.assertEqual(screen.display.root_group[1].color, 0x000000)
        self.assertEqual(screen.display.root_group[1].background_color, 0xFFFFFF)

    def test_reset(self):
        macropad = MockMacroPad()
        screen = Screen(macropad)
        screen.initialize()
        screen.highlight(1)
        screen.reset(1)

        self.assertEqual(screen.display.root_group[0].color, 0xFFFFFF)
        self.assertEqual(screen.display.root_group[0].background_color, 0x000000)
        self.assertEqual(screen.display.root_group[1].color, 0xFFFFFF)
        self.assertEqual(screen.display.root_group[1].background_color, 0x000000)
