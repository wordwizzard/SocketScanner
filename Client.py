#!/usr/bin/python           # This is client.py file

import socket

s = socket.socket()
host = socket.gethostname() # Get local machine name
port = 7000
s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done