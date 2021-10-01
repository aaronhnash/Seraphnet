import socketserver, threading, time
from typing import Type
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO pin mapping & setup
pinLED = 18
pinServo = 17

GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinServo, GPIO.OUT)

servo = GPIO.PWM(pinServo, 50)
servo.start(0)

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

        elif command[0] == "blink":

            if command[1] == None:
                n = 1
            else:
                n = command[1]
            response = bytes(f"Blinking {n} time(s)", "ascii")
            self.request.sendall(response)

            try:
                self.blink(int(command[1]))
            except: # If there's an error, then run as default.
                self.blink()

        elif command[0] == "rotate":

            if command[1] == None:
                n = 0
            else:
                n = command[1]
            response = bytes(f"Rotating to {n} degrees", "ascii")
            self.request.sendall(response)

            try:
                self.rotate(int(command[1]))
            except:
                print("Defauling to 0")
                self.rotate()

        elif command[0] == "help":
            if command[1] == "echo":
                response = bytes("Usage: echo (message); returns message to client", "ascii")
            elif command[1] == "blink":
                response = bytes("Usage: blink (integer); blinks LED n times. Default 1.", "ascii")
            elif command[1] == "rotate":
                response = bytes("Usage: rotate (integer); rotates servo to n degrees. Default 0, range (-90, 90).", "ascii")
            else:
                response = bytes("Usage: help (command); available commands: echo, blink, rotate, help", "ascii")
            self.request.sendall(response)
        else:
            response = bytes(f"Invalid command! Type help for help.", "ascii")
            self.request.sendall(response)


    #TODO: Write functions below

    def blink(self, count=1):
        """Turns an external LED on and off n times. Default 1."""
        #TODO: Get GPIO mapping and see which pin the LED is attached to. 
        for n in range(count):
            print(f"Blink {n+1}...")
            GPIO.output(pinLED, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(pinLED, GPIO.LOW)
            time.sleep(0.3)

    def rotate(self, deg=0):
        """Rotates an attached servo to a specified angle. Min -90, max 90."""
        #TODO: Uncomment when connected to the RPi

        # Formula for calculating duty percentage
        cycle = deg*(5/90)+7.5
        servo.ChangeDutyCycle(cycle)
        time.sleep(0.4)
        servo.ChangeDutyCycle(0)

