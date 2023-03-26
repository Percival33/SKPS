import gpio4

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' # set direction to output
gpio27.value = 0

gpio18 = gpio4.SysfsGPIO(18)
gpio18.export = True # use the pin
gpio18.direction = 'in' # set direction to output

while True:
    if gpio18.value == 0:
        gpio27.value = 1
    elif gpio18.value == 1:
        gpio27.value = 0

gpio27.value = 0
gpio27.export = False # cleanup
gpio18.export = False # cleanup
