import storage
import board
import digitalio

btn = digitalio.DigitalInOut(board.BTN)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

if btn.value:
    print("Button not pressed during boot, drive disabled.")
    storage.disable_usb_drive()
