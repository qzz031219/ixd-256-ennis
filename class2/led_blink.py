# blink an LED connected to pin G1 on and off

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

pin1 = None

def setup():
  global pin1

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)

def loop():
  global pin1
  M5.update()
  pin1.on()
  time.sleep(1)
  pin1.off()
  time.sleep(1)

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
