#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-09-04 18:00:27


import time
import configparser
import signal, os

config = configparser.ConfigParser()
config.read('example.ini')


def main():
    for i in range(10000):
        print("{}, 准备处理".format(i))
        print(config["DEFAULT"]["number"])
        time.sleep(2)
        print(config["DEFAULT"]["number"])  # signal触发时，会变成3
        print("{}, 处理结果\n\n".format(i))  # signal触发时，i循环继续．i仍然是i


def handler(signum, frame):
    print("Signal handler called with signal", signum)
    config.read('example.ini')


signal.signal(signal.SIGHUP, handler)


if __name__ == "__main__":
    main()
