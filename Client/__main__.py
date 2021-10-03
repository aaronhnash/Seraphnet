from Client import client

HOST= "172.20.10.6"
PORT = 9999


if __name__ == "__main__":
    print("Initializing client...")
    client(HOST, PORT, "echo connected")
    
    while True:
        message = input("> ")
        client(HOST, PORT, message)
