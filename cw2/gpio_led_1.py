import gpio4
import time
gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' # set direction to output

for _ in range(10):
    gpio27.value = 0 # set value to low
    time.sleep(0.2)
    gpio27.value = 1 # set value to high
    time.sleep(1)

gpio27.export = False # cleanup
