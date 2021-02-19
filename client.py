#!/usr/bin/env python3

import socket
from struct import *
import base64
import random
import time
import sched

def create_temps(): 
    heat = random.randrange(-2147, 2147)
    hum = random.randrange(-2147, 2147)
    packed = pack('ii', heat, hum)
    return base64.b64encode(packed)

def sendMsg(s):
    msg = create_temps()
    s.send(msg)

#def generateTemps(): 

    

HOST = '127.0.0.1'    # The remote 
PORT = 50010          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
schedule = sched.scheduler(time.time, time.sleep)
schedule.enter(10, 1, sendMsg(s))


#msg = "hello world"
#s.sendall(msg.encode())
#encoded = create_temps()

#encoded = base64.b64encode(temps)
#s.send(encoded)
data = s.recv(1024)


s.close()
print ('Received', repr(data))