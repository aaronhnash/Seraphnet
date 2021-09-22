import socketserver

class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        """The functions and responses that should be taken when the server is run."""
        # How does it respond?
        self.data = self.request.recv(1024).strip() # This is where the incoming data is stored
        print("{} Says: ".format(self.client_address[0]))
        print(self.data)

        self.request.sendall(f"Echoing {self.data.upper()}") # Return an echo with capitalization

        

