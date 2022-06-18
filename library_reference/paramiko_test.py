#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import paramiko
from dotenv import dotenv_values


client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.connect(
    hostname=dotenv_values()["REMOTE_HOST"],
    username=dotenv_values()["REMOTE_USER"],
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


def test_timeout():
    # 明明不会报错啊
    stdin, stdout, stderr = client.exec_command("sleep 5 && ls ~")
    print(stdout.read().decode("utf-8"))


if __name__ == "__main__":
    test_timeout()
