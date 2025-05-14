#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import paho.mqtt.client as mqtt

globalinfo = {
        "cnt": 0
}
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("abc")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    globalinfo["cnt"] += 1
    if globalinfo["cnt"] % 100 == 0:
        print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
print("开始循环")
mqttc.loop_forever()
