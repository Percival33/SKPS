import time
import gpio4

pin_number = 27
gpio_pin = gpio4.SysfsGPIO(pin_number)
gpio_pin.export = True
gpio_pin.direction = 'out'


def set_angle(angle):
    # Convert angle to duty cycle
    # 0 degrees = 0.05, 180 degrees = 0.1
    duty = 0.05 + (angle / 180) * 0.05
    period = 0.02 # s

    print(angle)

    high_time = period * duty
    low_time = period - high_time
    
    for _ in range(100):
        gpio_pin.value = 1
        time.sleep(high_time)
        gpio_pin.value = 0
        time.sleep(low_time)


def go_brr():
    for angle in range(0, 181, 10):
        set_angle(angle)
        time.sleep(0.01)

    for angle in range(180, -1, -10):
        set_angle(angle)
        time.sleep(0.01)


while True:
    go_brr()

gpio_pin.export = False  # cleanup