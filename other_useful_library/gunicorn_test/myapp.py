#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-09-05 09:38:26

import time


delay = 0


def app(environ, start_response):
    print("启动gunicorn{}".format(delay))
    time.sleep(delay)
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
