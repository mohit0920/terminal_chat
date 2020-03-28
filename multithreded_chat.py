#!/usr/bin/env python3

import logging
import threading, sys, socket
import time


import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print("{} wrote:".format(self.client_address[0]))
        print(">>>>"+self.data.decode())
        # just send back the same data, but upper-cased
       
        #send_back=input("Enter  Your reponse: ").encode()
        #send_back="Delivered".encode()
        self.request.sendall("Delivered".encode())


def rcvr_fxn():
    HOST, PORT = '', 44556 #Blank to recive from all ips.

    # Create the server, binding to localhost on port 44556
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running untl you
        # interrupt the program with Ctrl-C
        server.serve_forever()

def sender_fxn():
    HOST, PORT = input("Enter ip to connect:"), 44556
    while(True):
        # Create a socket (SOCK_STREAM means a TCP socket)
        data = input()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print(">{}".format(received))
        #print("Received: {}".format(received))


def thread_function(name):
    #logging.info("Thread %s: starting", name)
    #time.sleep(2)
    rcvr_fxn()
    #logging.info("Thread %s: finishing", name)

def thread_function2(name):
    #logging.info("Thread %s: starting", name)
    #time.sleep(2)
    sender_fxn()
    #logging.info("Thread %s: finishing", name)
if __name__ == "__main__":
    #format = "%(asctime)s: %(message)s"
    #logging.basicConfig(format=format, level=logging.INFO,
     #                   datefmt="%H:%M:%S")

    #logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=thread_function2, args=(2,))
   # logging.info("Main    : before running thread")
    x.start()
    y.start()

    #logging.info("Main    : wait for the thread to finish")
    # x.join()
    #logging.info("Main    : all done")

