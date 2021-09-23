import socket
import sys


def client(HOST, PORT, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')

        print("Sent:     {}".format(message))
        print("Received: {}".format(response))
