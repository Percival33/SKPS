import math
import time
import gpio4

gpio9 = gpio4.SysfsGPIO(9)
gpio9.export = True # use the pin
gpio9.direction = 'out' # set direction to output

start = time.process_time()

sounds = [
    261,
    294,
    330,
    349,
    392,
    440,
    494,

    523,
    587,
    659,
    698,
    784,
    880,
    987
]

def play(st):
    gpio9.value = 1 # set value to high
    time.sleep((1/st))
    gpio9.value = 0 # set value to high
    time.sleep((1/st))

def duty_cycle_pwm():
    duty_cycle = 0.5
    for sound in sounds:
        curr_time = time.process_time()
        
        for _ in range(200):
            play(sound)
    
        if time.process_time() - start >= 10:
            break
        


duty_cycle_pwm()

gpio9.export = False # cleanup
