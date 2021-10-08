
## Flash MicroPython

```bash
esptool.py --port /dev/ttyUSB0 erase_flase
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 --verify write_flash -z 0x1000 ~/Downloads/esp32-20210902-v1.17.bin
```

### ampy

Make sure user is in the dialout group to have write permissions to the /dev/ttyUSB0 device.


Install Python modules for ampy (can use Python virtualenv or install globally since it shouldn't conflict with anything else)

```bash
pip3 install adafruit-ampy
pip3 install rshell
```

```bash
ampy --port /dev/ttyUSB0 --baud 115200 put boot.py
ampy --port /dev/ttyUSB0 --baud 115200 put main.py
ampy --port /dev/ttyUSB0 --baud 115200 put ssd1306.py
```

### screen

The screen command is used to connect to the serial port

```bash
sudo apt-get install -y screen
```

Attach to USB port

```bash
screen /dev/ttyUSB0 115200
```

After attaching to USB port, press "Enter" to get Python shell (see [Python shell help](#python-shell-help) below).

Once in the screen session and in the python shell (not screen command), press Ctrl-D to soft-reboot after uploading a file.  You cannot upload a file with ampy if screen is also attached via the serial port.

Exit screen (kill screen).  The Ctrl-a is the default escape key to send the command to screen (not for Python shell).
```
Ctrl-a, k
```

## Python shell help

```
>>> help()
Welcome to MicroPython on the ESP32!

For generic online docs please visit http://docs.micropython.org/

For access to the hardware use the 'machine' module:

import machine
pin12 = machine.Pin(12, machine.Pin.OUT)
pin12.value(1)
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
print(pin13.value())
i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
i2c.scan()
i2c.writeto(addr, b'1234')
i2c.readfrom(addr, 4)

Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
>>> 
```

## Install mqtt library in project

```bash
wget https://raw.githubusercontent.com/pycom/pycom-libraries/master/examples/mqtt/mqtt.py
ampy --port /dev/ttyUSB0 --baud 115200 put mqtt.py
```

## Install ssd1306 OLED library in project

```bash
wget https://raw.githubusercontent.com/micropython/micropython/master/drivers/display/ssd1306.py
ampy --port /dev/ttyUSB0 --baud 115200 put ssd1306.py
```

