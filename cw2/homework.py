import matplotlib.pyplot as plt
import time
import sys

def wypelnienie():
    p = .5 # wspolczynnik wypelnienia
    freq = 1 # Hz
    mul = 1000
    period = 1/freq * mul
    duty_cycle = period * p

    curr_time = 0
    X = 10
    signal = []

    while X:
        if curr_time <= duty_cycle:
            # signal.append(1)
            print("true")
        else:
            # signal.append(0)
            print("false")

        curr_time += 1

        if curr_time >= period:
            # print(f'{curr_time:=} {period:=}')
            curr_time = 0
            X -= 1

            if p >= 1:
                p = 0

            p += 0.1
            duty_cycle = period * p

        time.sleep(0.001)



    # x = [x for x in range(len(signal))]
    # plt.plot(x, signal)
    # plt.show()

def czestotliwosc():
    p = .5  # wspolczynnik wypelnienia
    freq = 1 # Hz
    mul = 1000
    period = 1/freq * mul
    duty_cycle = period * p

    curr_time = 0
    X = 10
    signal = []

    while X:
        if curr_time <= duty_cycle:
            # signal.append(1)
            print("true")
        else:
            # signal.append(0)
            print("false")

        curr_time += 1

        if curr_time >= period:
            # print(f'{curr_time:=} {period:=}')
            curr_time = 0
            X -= 1

            if freq == 5:
                freq = 0

            freq += 1
            period = 1 / freq * mul
            duty_cycle = period * p

        time.sleep(0.001)
    # x = [x for x in range(len(signal))]
    # plt.plot(x, signal)
    # plt.show()

if __name__ == "__main__":
    if sys.argv[1] == "-wyp":
        wypelnienie()
    elif sys.argv[1] == "-cze":
        czestotliwosc()