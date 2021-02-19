#!/usr/bin/env python3

import socket
from struct import *
import base64

def read_temps(data):
    decode = base64.b64decode(data)
    heat, hum = unpack('ii', decode)
    return print('Heat is: ', recalc(heat), 'Hum is: ', recalc(hum))

def recalc(condition):
    return condition * 10**-2 

HOST = '127.0.0.1'               
PORT = 50010             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    data = conn.recv(1024)
    read_temps(data)
    #conn.send('Ok')
    break
    if not data: break
    #conn.sendall('got it'.encode())
conn.close()