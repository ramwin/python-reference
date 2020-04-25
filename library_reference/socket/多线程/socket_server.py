#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-27 16:42:27

import time
import socket
import _thread


def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(2**10)
        print("接收到了消息: {}".format(msg))
        time.sleep(0.2)
        data = str(time.time())
        clientsocket.sendall(data.encode('utf-8'))


HOST = 'localhost'
PORT = 50008
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        print("等待链接")
        con, addr = s.accept()
        print("有链接来啦")
        print(con)
        _thread.start_new_thread(on_new_client, (con, addr))
