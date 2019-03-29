#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
# ---
import json
import paho.mqtt.client as mqtt
from time import sleep

HOST = 'localhost'
PORT = 1883


def intent_received(client, userData, message):

    if message.topic == 'hermes/intent/jocavdh:introduce':
        print('introduce')
    elif message.topic == 'hermes/intent/jocavdh:play':
        print('play')
    else:
        return

 
client = mqtt.Client()
client.connect(HOST, PORT, 60)
client.on_connect = on_connect
client.connected_flag=False
listening = False

client.on_message = intent_received
client.loop_forever()