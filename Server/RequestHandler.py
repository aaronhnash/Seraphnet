import socketserver, threading
from typing import Type
#import GPIO

class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        """The functions and responses that should be taken when the server is run."""
        # How does it respond?
        self.data = str(self.request.recv(1024), "ascii").strip() # This is where the incoming data is stored

        command = self.data.split(" ", 1)
        if len(command) == 1: # Add a blank command if there's nothing there
            command.append(None)
        
        command[0] = command[0].lower() # Make sure that the command is lower case!
    
        # Thread the responses in case multiple processes will need to be run 
        cur_thread = threading.current_thread()
        
        print(f"{cur_thread.name}: {self.client_address} Says: {self.data}")

        if command[0] == "echo":
            response = bytes(f"Echoing '{command[1]}'", "ascii")

        elif command[0] == "blink":
            try:
                self.blink(int(command[1]))
                n = command[1]
            except: # If there's an error, then run as default.
                self.blink()
                n = 1
            response = bytes(f"Blinking {n} time(s)", "ascii")

        elif command[0] == "rotate":
            try:
                self.rotate(int(command[1]))
                n = command[1]
            except:
                self.rotate()
                n = 0
            response = bytes(f"Rotating {n} degrees", "ascii")

        elif command[0] == "help":
            if command[1] == "echo":
                response = bytes("Usage: echo (message); returns message to client", "ascii")
            elif command[1] == "blink":
                response = bytes("Usage: blink (integer); blinks LED n times. Default 1.", "ascii")
            elif command[1] == "rotate":
                response = bytes("Usage: rotate (integer); rotates servo n degrees. Default 0, range (-90, 90).", "ascii")
            else:
                response = bytes("Usage: help (command); available commands: echo, blink, rotate, help", "ascii")

        else:
            response = bytes(f"Invalid command! Type help for help.", "ascii")

        self.request.sendall(response) # Return an echo with capitalization


    #TODO: Write functions below

    def blink(self, count=1):
        """Turns an external LED on and off n times. Default 1."""
        #TODO: Get GPIO mapping and see which pin the LED is attached to. 

        pass

    def rotate(self, deg=0):
        """Rotates an attached servo to a specified angle. Min -90, max 90."""
        #TODO: Get GPIO mapping of servo.
        #TODO: Should the default action just spin for a little bit, and then go the other way?

        pass