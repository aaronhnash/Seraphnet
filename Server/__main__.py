import socketserver
import threading
from RequestHandler import RequestHandler

if __name__=="__main__":
    # Only run if this program itself is run
    HOST, PORT = "localhost", 9999

    print("Initializing server...")
    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        # Run until interrupted
        print("Threading...")
        # Thread when first started, will start one more thread for each request receieved
        server_thread = threading.Thread(target=server.serve_forever)

        # Terminate the server when the main thread terminates
        server_thread.daemon = True 

        print(f"Server loop running in thread: {server_thread.name}")
        server_thread.run()



# Note about what I've learned:
# This code currently works for local servers. It supports multi-threading, but at the moment I have no need for more than one thread.
# I decided to leave it in in case it would be useful for later modifications.