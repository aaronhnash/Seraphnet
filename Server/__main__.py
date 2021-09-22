import socketserver
from RequestHandler import RequestHandler

if __name__=="__main__":
    # Only run if this program itself is run
    HOST, PORT = "localhost", 9999 


    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        # Run until interrupted
        server.serve_forever()