# atom-lite-scripts

Circuitpython scripts to enable / disable / eStop an FRC Driver Station using an [AtomS3 Lite ESP32 dev kit](https://shop.m5stack.com/products/atoms3-lite-esp32s3-dev-kit). 

- [code.py](code.py) uses USB HID to emulate key presses in response to HTTP requests. 
- [boot.py](boot.py) prevents the CIRCUITPY device from mounting unless the onboard button is pressed when the board boots. 
- [settings.toml](settings.toml) holds field wifi network and team # config data.
