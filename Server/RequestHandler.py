import socketserver, threading
from typing import Type
from FunctionHandler import FunctionHandler

actions = FunctionHandler()

class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        """The functions and responses that should be taken when the server is run."""
        # How does it respond?
        self.data = self.request.recv(1024).strip() # This is where the incoming data is stored

        command = ((str(self.data)).replace("'","")[1:]).split(" ", 1)
        # Formats into something more usable--turns (b'first test') to ['first', 'test']
        if len(command) == 1: # Add a blank command if there's nothing there
            command.append(None)
        
        command[0] = command[0].lower() # Make sure that the command is lower case!
    
        # Thread the responses in case multiple processes will need to be run 
        cur_thread = threading.current_thread()
        
        print(f"{cur_thread.name}: {self.client_address} Says: {print(self.data)}")

        if command[0] == "echo":
            response = bytes(f"Echoing '{command[1]}'", "ascii")

        elif command[0] == "blink":
            try:
                actions.blink(command[1])
            except TypeError: # If the modifier is None or a string that can't be changed into an int, then it won't work. 
                actions.blink()

        else:
            response = bytes(f"No valid command", "ascii")

        self.request.sendall(response) # Return an echo with capitalization