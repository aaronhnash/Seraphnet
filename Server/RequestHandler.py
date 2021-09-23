import socketserver
import threading


class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        """The functions and responses that should be taken when the server is run."""
        # How does it respond?
        self.data = self.request.recv(1024).strip() # This is where the incoming data is stored

        # Thread the responses in case multiple processes will need to be run 
        cur_thread = threading.current_thread()
        
        print(f"{cur_thread.name}: {self.client_address} Says:")
        print(self.data)

        response = self.data.upper()

        self.request.sendall(response) # Return an echo with capitalization