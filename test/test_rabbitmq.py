#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pika
import time

from redis import Redis


rabbitmq = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = rabbitmq.channel()

redis = Redis()


def callback(*args, **kwargs):
    pass


def test_rabbitmq():
    start = time.time()
    channel.queue_declare(queue="hello")
    for i in range(10000):
        channel.basic_publish(exchange="", routing_key="hello", body=str(i))
    send_time = time.time()
    print("rabbitmq 发送耗时", send_time - start)
    # print("rabbitmq 接收耗时", end - send_time)


def test_redis():
    start = time.time()
    for i in range(10000):
        redis.rpush("list", i)
    send_time = time.time()
    for i in range(9000):
        a = redis.lpop("list")
        callback(a)
    end = time.time()
    print("redis 发送耗时", send_time - start)
    print("redis 接收耗时", end - send_time)


if __name__ == "__main__":
    test_rabbitmq()
    test_redis()
