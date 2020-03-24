#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-18 15:01:05


import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("", 8866)
    tcp_server_socket.bind(addr)
    tcp_server_socket.listen(128)
    client_socket, client_addr = tcp_server_socket.accept()
    recv_data = client_socket.recv(1024)
    print("接收到的数据：%s" % recv_data.decode("utf-8"))
        
    # 6.给对方发送数据
    # client_socket.send("hahaha".encode("utf-8")) 


main()
