
import ssd1306

# setup I2C
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# This example simulates a scrolling log screen.
# The logs list is used as a line buffer when the screen is redrawn.

# contrast:
# according to documentation, 0=dim/off, 255=bright/max
# it seems to be more of a percent brightness (0 - 100)
display.contrast(50)

# y_offsets for each row of text
y_offsets = [0, 10, 20, 30, 40, 50]

# initialize logs for display
logs = []
i = 0
while i < len(y_offsets):
    logs.append('')
    i += 1

while True:
  time.sleep(1)
  time_str = time.time()  # for log entry
  display.fill(0)  # clear display by filling with black
  logs = logs[1:]  # remove first element by starting at index 1 (removes index 0)
  logs.append(time_str)  # add log entry to end of list
  # write display buffer with logs
  for i, y in enumerate(y_offsets):
    display.text(str(logs[i]), 0, y, 1)
  display.show()  # update display