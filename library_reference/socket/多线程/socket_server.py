#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-27 16:42:27

import socket
import thread


def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(2**10)
        print("接收到了消息: {}".format(msg))


HOST = 'ramwin.com'
PORT = 50008
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        print("等待链接")
        conn, addr = s.accept()
        print("有链接来啦")
        print(conn)
        thread.start_new_thread(on_new_client, (coon, addr))
