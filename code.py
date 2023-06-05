import os
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import socketpool
import wifi
import mdns
from adafruit_httpserver import Server, Request, Response, GET
import time

mdns.Server(wifi.radio).hostname = os.getenv("TEAM")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

@server.route("/enable", GET)
def sendEnable(request: Request):
    keyboard.press(Keycode.LEFT_BRACKET)
    keyboard.press(Keycode.RIGHT_BRACKET)
    keyboard.press(Keycode.BACKSLASH)
    time.sleep(0.1)
    keyboard.release_all()
    return Response(request, "Enabled")

@server.route("/disable", GET)
def sendDisable(request: Request):
    keyboard.press(Keycode.ENTER)
    time.sleep(0.1)
    keyboard.release_all()
    return Response(request, "Disabled")

@server.route("/estop", GET)
def sendEStop(request: Request):
    keyboard.press(Keycode.SPACEBAR)
    time.sleep(0.1)
    keyboard.release_all()
    return Response(request, "Estopped")

server.serve_forever(str(wifi.radio.ipv4_address))
