#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-18 15:02:44

import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.连接服务器
    dest_ip = "localhost"
    dest_port = 8866
    dest_addr = (dest_ip, dest_port)
    tcp_socket.connect(dest_addr)

    # 3. 接收/发送数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))    

    # 接收服务器发送的数据
    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("utf-8"))    

    # 4. 关闭套接字socket
    tcp_socket.close()


main()
