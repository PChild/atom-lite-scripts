import os
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import socketpool
import wifi
import mdns
from adafruit_httpserver import Server, Request, Response, GET

mdns.Server(wifi.radio).hostname = os.getenv("TEAM")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

@server.route("/enable", GET)
def sendEnable(request: Request):
    keyboard_layout.write("[]\\")
    return Response(request, "Enabled")

@server.route("/disable", GET)
def sendDisable(request: Request):
    keyboard_layout.write("\n")
    return Response(request, "Disabled")

server.serve_forever(str(wifi.radio.ipv4_address))
