# Overview

Welcome to my first step in networking with embedded systems! In this project, I will be connecting a laptop 'client' with an offboard Raspberry Pi 'server'. This project is my first step into learning about networking, a subject I've run into numerous times while trying to work with my Raspberry Pi. 

This project comes as a set, with both a `Client` and a `Server` file. While each file is available in the same repository, each program should be run on the target computer. For example:
```python
python3 Server
```
should first be run on the target `Server` computer, and 
```python
python3 Client
```
should next be run on the target `Client` computer. No input is needed after running `Server`. `Client` offers built-in help for using each of the commands, which are listed below:

1. echo {argument}
    * Takes the supplied argument and responds, returning the argument to the client.
2. blink {n}
    * Blinks an LED n number of times, default 1.
3. rotate {n}
    * Rotates a servo to n degrees, from -90 to 90. 
4. help {command}
    * Provides information for any listed command


I've been wanting to learn about remotely controlling my Raspberry Pi, in the hopes of building something more hardware intensive down the line. This project gave me the perfect opportunity to learn about networking

[Software Demo Video](https://youtu.be/vZmuBncDaVg)

# Network Communication

This program utilizes the server/client architecture, given a threaded server that's capable of handling multiple requests simultaneously from one or more connected clients, though given the low amount of current available functions, more than one simultaneous client is not recommended. 

I used a TCP-based server for this project, in order to ensure efficient communication between the server and the client. By default this program uses the server's port 9999, but this can be changed as needed.

The messages sent between the server and the client are sent in bytes, and then interpreted according to the command received. 

# Development Environment

{Describe the tools that you used to develop the software}

This was developed using `VisualStudioCode`, `Git`, & `Github`, and is meant to be hosted on a `Raspberry Pi`.

This project was written in **Python**, libraries used are `socket`, `socketserver`, `threading` and `RPi.GPIO`, included in default installation of `Raspberry Pi OS`. 

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Stack Overflow - Connecting Separate Computers using Socket](https://stackoverflow.com/questions/67539425/how-can-i-connect-two-computers-with-python-socket)
* [Learn Robotics - Controlling a Servo using Duty Cycles](https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/)
* [The Pi Hut - Controlling an LED](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)
* [Python Docs - SocketServer documentation](https://docs.python.org/3.6/library/socketserver.html)
* [Python Docs - Socket documentation](https://docs.python.org/3.6/library/socket.html)
* [Web Site Name](http://url.link.goes.here)


# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Expanded functionality -- More onboard functions for RPi.
* Remote access -- Ability for Server/Client to be hosted on separate networks
* Client GUI
