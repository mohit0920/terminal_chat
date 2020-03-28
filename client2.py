#!/usr/bin/env python3

# Echo client program
import socket
import sys

HOST = input("Enter ip to connect: ")    # The remote host
PORT = 44556              # The same port as used by the server

s = None
print(socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM))
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        print("oe2")
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
