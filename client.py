#!/usr/bin/env python3

import socket
from struct import *
import base64
import random
import time
import sched

def create_temps(): 
    heat = random.randrange(-1000, 2000)
    hum = random.randrange(0, 1000)
    packed = pack('<hH', heat, hum)
    return base64.b64encode(packed)

def send_message(connection):
        msg = create_temps()
        connection.sendall(msg)

HOST = '127.0.0.1'    
PORT = 50010 
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scheduler = sched.scheduler(time.time, time.sleep)

for _ in range(5):
    try: 
        connection.connect((HOST, PORT))
        starttime = time.time()
        while True:
            send_message(connection)
            time.sleep(10)
    except:    
        print('Something went wrong:', socket.error)
        print('attempting to reconnect.')