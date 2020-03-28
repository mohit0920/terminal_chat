#!/usr/bin/env python3


import socket
import sys

HOST, PORT = "::1", 44556
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM,0,0) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT,0,0))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
