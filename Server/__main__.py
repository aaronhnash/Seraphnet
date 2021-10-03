import socketserver, socket, threading
from RequestHandler import RequestHandler

if __name__=="__main__":
    # Only run if this program itself is run

    print("Initializing server...")
    hostname = socket.gethostname()

    HOST = "172.20.10.6"
    PORT = 9999

    class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass

    print(f"'{hostname}' starting server at: {HOST}:{PORT}")
    with ThreadedTCPServer((HOST, PORT), RequestHandler) as server:
        # Run until interrupted
        print("Threading...")
        # Thread when first started, will start one more thread for each request receieved
        server_thread = threading.Thread(target=server.serve_forever)

        # Terminate the server when the main thread terminates
        server_thread.daemon = True 

        print(f"Server loop running in thread: {server_thread.name}")
        server_thread.run()
