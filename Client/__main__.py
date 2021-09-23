from Client import client

HOST, PORT = "localhost", 9999

if __name__ == "__main__":
    print("Initializing client...")
    while True:
        message = input("> ")
        client(HOST, PORT, message)
