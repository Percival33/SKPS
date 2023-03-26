import math
import time
import gpio4

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' # set direction to output

start = time.time()

def duty_cycle_pwm():
    duty_cycle = 0
    cnt = 0
    period = 0.02 # s
    while True:
        gpio27.value = 1 # set value to high
        time.sleep(period * duty_cycle)
        gpio27.value = 0  # set value to low
        time.sleep(period * (1 - duty_cycle))

        cnt += 0.2
        duty_cycle = (math.sin(cnt) + 1) / 2

        if time.time() - start >= 10:
            break


duty_cycle_pwm()

gpio27.export = False # cleanup
