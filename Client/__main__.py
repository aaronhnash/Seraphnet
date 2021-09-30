from Client import client


# 10.244.133.138 (school mac)
HOST, PORT = "10.244.133.138", 9999
#HOST = 'localhost'
# 10.46.13.201 (pi)
#10.46.13.204 (mac)

if __name__ == "__main__":
    print("Initializing client...")
    client(HOST, PORT, "echo Connected!")
    
    while True:
        message = input("> ")
        client(HOST, PORT, message)
