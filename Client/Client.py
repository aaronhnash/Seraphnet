import socket
import sys


def client(HOST, PORT, message):
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(message, 'ascii'))
            response = str(sock.recv(1024), 'ascii')

            print("Sent:     {}".format(message))
            print("Received: {}".format(response))

    except Exception as e:
        print(f"Unable to establish connection with {HOST}:{PORT}: {e}")
        exit()