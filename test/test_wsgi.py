#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-12-23 09:31:23


def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
    ])
    return iter([data])
