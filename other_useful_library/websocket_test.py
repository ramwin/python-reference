#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-01-14 11:24:14

import json
import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)
    if json.loads(message)["type"] == "message":
        pass
    else:
        ws.send(json.dumps({
            "type": "message",
            "user": {
                "id": 2586,
                "name": "王祥",
                "avatar": "https://publicstatic.duishang.net/avatar-2586",
            },
            "message": "我收到消息了",
        }))

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        # ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9999/ws/group/123/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    # ws.on_open = on_open
    ws.run_forever()
