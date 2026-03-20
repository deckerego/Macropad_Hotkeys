from adafruit_hid.mouse import Mouse

try:
    from typing import Optional, Sequence
    import usb_hid # type: ignore (part of CircuitPython standard libs)
except ImportError:
    pass

## 
# Adapter for the Macropad Mouse HID device that allows for extended properties.
# Inspired by and portions derived from:
# https://github.com/s117/Adafruit_CircuitPython_HID/blob/feature/better_mouse_forwarding/adafruit_hid/mouse.py
##
class MouseAdapter():
    WHEEL          = 0x118
    PAN            = 0x119
    LEFT_BUTTON    = 1 << 0
    RIGHT_BUTTON   = 1 << 1
    MIDDLE_BUTTON  = 1 << 2
    SIDE_BUTTON    = 1 << 3
    EXTRA_BUTTON   = 1 << 4
    FORWARD_BUTTON = 1 << 5
    BACK_BUTTON    = 1 << 6
    TASK_BUTTON    = 1 << 7
    
    def __init__(self, mouse: Mouse) -> None:
        self.mouse = mouse
        self.mouse.report = bytearray(7)

    def __str__(self):
        return str(self.mouse._mouse_device)

    def press(self, buttons: int) -> None:
        self.mouse.report[0] |= buttons
        self._send_no_move()

    def release(self, buttons: int) -> None:
        self.mouse.report[0] &= ~buttons
        self._send_no_move()

    def release_all(self) -> None:
        self.mouse.report[0] = 0
        self._send_no_move()

    def click(self, buttons: int) -> None:
        self.press(buttons)
        self.release(buttons)

    def move(self, x: int = 0, y: int = 0, wheel: int = 0, pan: int = 0) -> None:
            while x != 0 or y != 0 or wheel != 0 or pan != 0:
                partial_x = MouseAdapter._limit_i16(x)
                partial_y = MouseAdapter._limit_i16(y)
                partial_wheel = MouseAdapter._limit_i8(wheel)
                partial_pan = MouseAdapter._limit_i8(pan)
                self.mouse.report[1] = partial_x & 0xFF
                self.mouse.report[2] = (partial_x >> 8) & 0xFF
                self.mouse.report[3] = partial_y & 0xFF
                self.mouse.report[4] = (partial_y >> 8) & 0xFF
                self.mouse.report[5] = partial_wheel & 0xFF
                self.mouse.report[6] = partial_pan & 0xFF
                self.mouse._mouse_device.send_report(self.mouse.report, 0x82)
                x -= partial_x
                y -= partial_y
                wheel -= partial_wheel
                pan -= partial_pan

    def _send_no_move(self, ex: bool = True) -> None:
        self.mouse.report[1] = 0
        self.mouse.report[2] = 0
        self.mouse.report[3] = 0
        self.mouse.report[4] = 0
        self.mouse.report[5] = 0
        self.mouse.report[6] = 0

        self.mouse._mouse_device.send_report(self.mouse.report, 0x82)
    
    @staticmethod
    def _limit_i8(dist: int) -> int:
        return min(127, max(-127, dist))
    
    @staticmethod
    def _limit_i16(dist: int) -> int:
        return min(32767, max(-32767, dist))