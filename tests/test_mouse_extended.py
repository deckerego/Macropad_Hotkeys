from unittest import TestCase, mock
from mouse_extended import MouseAdapter

class MockMouse:
    def __init__(self):
        self._mouse_device = MockDevice()

class MockDevice:
    def __init__(self):
        self.send_report = mock.Mock()

class TestMouseAdapter(TestCase):
    def test_init(self):
        mouse = MockMouse()
        MouseAdapter(mouse)
        self.assertEqual(len(mouse.report), 7)

    def test_click(self):
        mouse = MockMouse()
        adapter = MouseAdapter(mouse)
        adapter.click(MouseAdapter.LEFT_BUTTON)

        mouse._mouse_device.send_report.assert_called()

    def test_wheel(self):
        mouse = MockMouse()
        adapter = MouseAdapter(mouse)
        adapter.move(wheel = 1)

        self.assertEqual(mouse.report[5], 0x01)
        mouse._mouse_device.send_report.assert_called_once()

    def test_pan(self):
        mouse = MockMouse()
        adapter = MouseAdapter(mouse)
        adapter.move(pan = 1)

        self.assertEqual(mouse.report[6], 0x01)
        mouse._mouse_device.send_report.assert_called_once()