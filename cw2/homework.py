import time
import sys

def wypelnienie():
    p = .5 # wspolczynnik wypelnienia
    freq = 1
    mul = 1000
    period = 1/freq * mul
    duty_cycle = period * p

    curr_time = 0
    X = 10
    signal = []

    while X:
        if curr_time <= duty_cycle:
            print("true")
        else:
            print("false")

        curr_time += 1

        if curr_time >= period:
            curr_time = 0
            X -= 1

            if p >= 1:
                p = 0

            p += 0.1
            duty_cycle = period * p

        time.sleep(0.001)


def czestotliwosc():
    p = .5  # wspolczynnik wypelnienia
    freq = 1
    mul = 1000
    period = 1/freq * mul
    duty_cycle = period * p

    curr_time = 0
    X = 10
    signal = []

    while X:
        if curr_time <= duty_cycle:
            print("true")
        else:
            print("false")

        curr_time += 1

        if curr_time >= period:
            curr_time = 0
            X -= 1

            if freq == 5:
                freq = 0

            freq += 1
            period = 1 / freq * mul
            duty_cycle = period * p

        time.sleep(0.001)


if __name__ == "__main__":
    if sys.argv[1] == "-wyp":
        wypelnienie()
    elif sys.argv[1] == "-cze":
        czestotliwosc()
        
