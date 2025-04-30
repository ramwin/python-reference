#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pika


def callback(ch, method, properties, body):
    if int(body) > 9990:
        print(body)
    if int(body) < 10:
        print(body)


def main():
    rabbitmq = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = rabbitmq.channel()
    # channel.basic_consume(
    #         queue="hello",
    #         auto_ack=True,
    #         on_message_callback=callback)
    # channel.start_consuming()
    while True:
        method, properties, body = channel.basic_get("hello")
        if method is None:
            return
        # callback(channel, method, properties, body)
        channel.basic_ack(method.delivery_tag)


if __name__ == "__main__":
    main()
