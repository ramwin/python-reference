#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from redis import Redis


c = Redis()
# 这时候把redis服务器停止
c.get('foo')  # 报错
# 这时候把redis服务器启动
c.get('foo')  # 正常
