import matplotlib.pyplot as plt
import time

# freq = 1 # Hz
# # ms
# step = int(1 / freq * 1000)
# MAX_T = 3 # s
# p = .2

# def generate_pwm(p: float) -> tuple[list[float], list[float]]:
#     Y = []
#     for _ in range(MAX_T):
#         on = int(step * p)
#         off = step - on
#         for x in range(on):
#             Y.append(1)
#
#         for x in range(off):
#             Y.append(0)
#
#     x = [x / 1000 for x in range(MAX_T * step)]
#     return x, Y

# plt.grid()
# plt.xlabel("time [s]")
# plt.ylabel("output value")
# plt.ylim(-0.1, 1.1)
# x, y = generate_pwm(p)
# plt.plot(x, y, color='r')
# plt.show()

def wypelnienie():
    p = .5 # 0.5 wspolczynnik wypelnienia
    freq = 1 # Hz
    mul = 1000 # milisec
    period = 1/freq * mul
    duty_cycle = period * p

    curr_time = 0
    X = 10
    signal = []

    while X:
        # print(curr_time, end="\t")
        if curr_time <= duty_cycle:
            signal.append(1)
            # print("true")
        else:
            signal.append(0)
            # print("false")

        curr_time += 1

        if curr_time >= period:
            print(f'{curr_time:=} {period:=}')
            curr_time = 0
            X -= 1

            if p >= 1:
                p = 0

            p += 0.1
            duty_cycle = period * p

        # time.sleep(0.1)



    x = [x for x in range(len(signal))]
    plt.plot(x, signal)
    plt.show()

def czestotliwosc():
    p = .5  # 0.5 wspolczynnik wypelnienia
    freq = 1 # Hz
    mul = 1000 # milisec
    period = 1/freq * mul
    duty_cycle = period * p

    curr_time = 0
    X = 10
    signal = []

    while X:
        # print(curr_time, end="\t")
        if curr_time <= duty_cycle:
            signal.append(1)
            # print("true")
        else:
            signal.append(0)
            # print("false")

        curr_time += 1

        if curr_time >= period:
            print(f'{curr_time:=} {period:=}')
            curr_time = 0
            X -= 1

            if freq == 5:
                freq = 0

            freq += 1
            period = 1 / freq * mul
            duty_cycle = period * p

    x = [x for x in range(len(signal))]
    plt.plot(x, signal)
    plt.show()

if __name__ == "__main__":
    # wypelnienie()
    czestotliwosc()