#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-18 15:02:44

import socket


# Echo client program
import time
import socket

HOST = 'localhost'    # The remote host
PORT = 50008              # The same port as used by the server
for i in range(100):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("链接上啦")
        print(s)
        for i in range(1):
            s.sendall(str(i).encode('utf-8'))
            data = s.recv(1024)
            print('Received', repr(data))
            time.sleep(0.1)
