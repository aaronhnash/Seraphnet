import socketserver, threading, time
from typing import Type
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO pin mapping & setup
pinLED = 18
pinServo = 17

pin1 = 14
pin2 = 15
pin3 = 17
pin4 = 18

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

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
            self.request.sendall(response)

        elif command[0] == "forward":
            self.go_forward()
        elif command[0] == "left":
            self.go_forward()
        elif command[0] == "right":
            self.go_forward()
        elif command[0] == "stop":
            self.go_forward()
        elif command[0] == "back":
            self.go_back()


    def left_rotate(self, direction):
        """Rotates an attached servo to a specified angle. Min -90, max 90."""
        #TODO: Uncomment when connected to the RPi

        if direction=="cw":
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.LOW)
        
        elif direction=="ccw":
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.HIGH)
        
        elif direction=="stop":
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.HIGH)

    def right_rotate(self, direction):
        """Rotates an attached servo to a specified angle. Min -90, max 90."""
        #TODO: Uncomment when connected to the RPi

        if direction=="cw":
            GPIO.output(pin3, GPIO.HIGH)
            GPIO.output(pin4, GPIO.LOW)
        
        elif direction=="ccw":
            GPIO.output(pin3, GPIO.LOW)
            GPIO.output(pin4, GPIO.HIGH)
        
        elif direction=="stop":
            GPIO.output(pin3, GPIO.HIGH)
            GPIO.output(pin4, GPIO.HIGH)

    def go_forward(self):
        self.stop()
        self.left_rotate("cw")
        self.right_rotate("cw")
    
    def stop(self):
        self.left_rotate("stop")
        self.right_rotate("stop")

    def go_left(self):
        self.stop()
        self.left_rotate("ccw")
        self.right_rotate("cw")
    
    def go_right(self):
        self.stop()
        self.left_rotate("cw")
        self.right_rotate("ccw")

    def go_back(self):
        self.stop()
        self.left_rotate("ccw")
        self.right_rotate("ccw")