"""The library for the server's embedded functions. Contains the FunctionHandler class, to be called and modified by RequestHandler."""

#import GPIO

class FunctionHandler():
    """Contains the function response methods, called by RequestHandler."""
    
    def __init__(self):
        """Initializes the FunctionHandler class."""
        #TODO: Are there any variables that should/could be shared between methods?
        self.servo_pos = 0

        pass

    def blink(self, count=1):
        """Turns an external LED on and off n times. Default 1."""
        #TODO: Get GPIO mapping and see which pin the LED is attached to. 
        count = int(count)

        pass

    def rotate(self, deg=0):
        """Rotates an attached servo to a specified angle. Min -90, max 90."""
        #TODO: Get GPIO mapping of servo.
        #TODO: Should the default action just spin for a little bit, and then go the other way?
        deg = int(deg)

        pass