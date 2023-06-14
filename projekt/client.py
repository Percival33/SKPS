import socket
import time
import random

HOST = 'localhost'
PORT = 9999
MAX_DISTANCE = 10


def generate_angles():
    angle = 0
    direction = 1  # 1 for increasing, -1 for decreasing

    while True:
        yield angle

        if angle == 180:
            direction = -1
        elif angle == 0:
            direction = 1

        angle += direction


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((HOST, PORT))

    angle_generator = generate_angles()

    while True:
        distance = round(random.uniform(0, MAX_DISTANCE), 2)
        angle = next(angle_generator)

        data = f"{distance},{angle}\n"
        print(f"Sending: {data}")
        sock.sendall(data.encode('utf-8'))

        time.sleep(0.2)

    sock.close()
