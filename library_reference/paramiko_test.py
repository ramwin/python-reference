#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import paramiko


client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.connect(
    hostname="<hostname>",
    username="<username>",
)


def test_error():
    stdin, stdout, stderr = client.exec_command("ls ~")
    if stderr.read():
        raise Exception()
    print(stdout.read().decode("utf-8"))
    stdin, stdout, stderr = client.exec_command("ls non_exist")
    if stderr.read():
        raise Exception()
    print(stdout.read().decode("utf-8"))


if __name__ == "__main__":
    test_error()
