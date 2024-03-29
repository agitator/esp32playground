# esp32playground

Notes on esp32 with Micropython.

Hardware
--------
- https://esphome.io/devices/nodemcu_esp32.html

Firmware
--------
- v1.20.0 (2023-04-26) from https://micropython.org/download/esp32/
  to get mip instead of unsupported upip https://github.com/micropython/micropython/issues/7486

Basic Tooling
-------------
- Uploading firmware https://github.com/espressif/esptool/
  `esptool.py --chip esp32 --port /dev/tty.usbserial-0001  --baud 460800 write_flash -z 0x1000  /Users/peter/Downloads/esp32-20230426-v1.20.0.bin`

- Uploading files
  - https://github.com/scientifichackers/ampy
  - https://github.com/dhylands/rshell
  - https://github.com/wendlers/mpfshell
  - sticking to pymakr for now - just be cautios to not have other pymakr project opens that block that serial
  - https://www.digikey.ch/en/maker/projects/micropython-basics-load-files-run-code/fb1fcedaf11e4547943abfdd8ad825ce


Network Config
--------------
- esp32 Networking https://docs.micropython.org/en/latest/esp32/quickref.html#networking
- Managing credentials
    - Managing credentials https://swharden.com/blog/2021-05-15-python-credentials/
    - Configure network with some kind of dotenv https://forum.micropython.org/viewtopic.php?t=9369
    - mpy_env: manually installed, disabled msgpack support to run it
        - https://pypi.org/project/micropython-mpy-env/
        - https://github.com/ShenTengTu/micropython-env/blob/master/examples/main.py


API-Webserver
-------------

- https://www.electronicsforu.com/electronics-projects/api-server-esp8266-using-micropython
- https://github.com/peterhinch/micropython-samples

- https://bhave.sh/micropython-microdot/ ESP32 Web Server using Microdot
- https://microdot.readthedocs.io “The impossibly small web framework for Python and MicroPython”

