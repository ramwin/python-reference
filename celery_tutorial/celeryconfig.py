#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-09-03 11:18:59

broker_url = "amqp://@localhost:5672"
result_backend = "redis://localhost:6379/0"
timezone = 'Asia/Shanghai'
worker_concurrency=1
worker_redirect_stdouts_level="INFO"
worker_prefetch_multiplier=1
enable_utc = True
