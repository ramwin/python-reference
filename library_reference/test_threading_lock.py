#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import random
import time
import threading
import queue


class SocketClient:

    def __init__(self):
        self.queue = queue.Queue()

    def create(self):
        for i in range(10):
            data = json.dumps([
                    time.time()
                    for i in range(10)
            ]).encode("UTF-8")
            time.sleep(random.random() / 1000)
            self.queue.put(data)


def test_no_lock():
    client = SocketClient()
    threads = []
    for i in range(100):
        thread = threading.Thread(target=client.create, group=None)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    n = 0
    print("插入完毕")
    while True:
        try:
            client.queue.get(timeout=1)
            n += 1
        except Exception:
            break
            pass
    print("不加锁,最后的长度", n)


if __name__ == "__main__":
    test_no_lock()
