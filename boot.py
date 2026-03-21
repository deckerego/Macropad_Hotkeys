import board
import digitalio
import storage

# Mount the CIRCUITPY drive as read-only unless the top-left key is held down
encoder_switch = digitalio.DigitalInOut(board.KEY1)
encoder_switch.switch_to_input(pull=digitalio.Pull.UP)
if(encoder_switch.value):
    print("Disabling USB Storage")
    storage.disable_usb_drive()
else:
    print("Mounting Read/Write")
