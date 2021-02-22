#!/usr/bin/env python3

import socket
from struct import *
import base64
from threading import * 

host = '127.0.0.1'               
port = 50010             
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(10)

def read_temps(data):
    decode = base64.b64decode(data)
    heat, hum = unpack('<hH',  decode)
    return print('Heat is: ', recalc(heat), 'Hum is: ', recalc(hum))

def recalc(condition):
    return condition * 10**-2 


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
          data = self.sock.recv(1024)
          if data:
            read_temps(data)
          else:
              self.sock.close()
              break

while True:
    clientsocket, addr = serversocket.accept()
    print ('Connected by', addr)
    client(clientsocket, addr)