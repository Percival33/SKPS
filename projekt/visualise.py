import matplotlib.pyplot as plt
import numpy as np
import time
import socket

MAX_DISTANCE = 10  # Set max_distance to the maximum range of your sensor
HOST = 'localhost'
PORT = 9999


def recv_until(sock, suffix):
    message = ''
    while not message.endswith(suffix):
        data = sock.recv(1024).decode('utf-8')
        if not data:
            raise ConnectionError("Connection lost")
        message += data
    return message


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    print(f"Connection from {addr}")

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_rmax(MAX_DISTANCE + 3)
    plt.show(block=False)

    while True:
        data = conn.recv(1024)
        if not data:
            continue

        data_decoded = recv_until(conn, '\n').strip()
        print(f"Received data: {data_decoded}")

        distance, angle = map(float, data_decoded.split(','))

        if angle == 179 or angle == 1:
            ax.clear()

        ax.scatter(np.deg2rad(angle), distance, c='blue')
        ax.plot([0, np.deg2rad(angle)], [0, distance], c='red')

        fig.canvas.draw()
        fig.canvas.flush_events()

        time.sleep(0.1)
