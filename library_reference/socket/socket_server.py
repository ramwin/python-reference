#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-18 15:01:05


# Echo server program
import uuid
import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        print("等待链接")
        conn, addr = s.accept()
        print("有链接来啦")
        print(conn)
        print(addr)
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1023)
                if not data: break
                print("接受到了数据: {}".format(uuid.uuid4()))
                print("    {}".format(data[0:10]))
                data = str(time.time())
                print("返回数据: {}".format(data))
                try:
                    conn.sendall(data.encode("utf-8"))
                except Exception as e:
                    print(e)
