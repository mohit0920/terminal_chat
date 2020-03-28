#!/usr/bin/env python3

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
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
       
        #send_back=input("Enter  Your reponse: ").encode()
        #send_back="Delivered".encode()
        self.request.sendall("Delivered".encode())


if __name__ == "__main__":
    HOST, PORT = '', 44556 #Blank to recive from all ips.

    # Create the server, binding to localhost on port 44556
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running untl you
        # interrupt the program with Ctrl-C
        server.serve_forever()

#print("Just checking execution")
