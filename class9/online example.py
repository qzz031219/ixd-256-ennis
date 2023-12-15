import os, sys, io
import M5
from M5 import *
from umqtt import *


mqtt_client = None


def mqtt_my_button_event(data):
  global mqtt_client
  print('hello')


def setup():
  global mqtt_client
  mqtt_client.subscribe('my_button', mqtt_my_button_event, qos=0)

  M5.begin()
  mqtt_client = MQTTClient('my_atom_board', 'mqtt.m5stack.com', port=1883, user='', password='', keepalive=0)


def loop():
  global mqtt_client
  M5.update()
  mqtt_client.publish('my_button', '', qos=0)


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
