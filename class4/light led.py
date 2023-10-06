import os, sys, io
import M5
from M5 import *
from hardware import *
import time


rgb = None
state = 'green'

def setup():
  global rgb

  M5.begin()
  rgb = RGB(io=2, n=30, type="SK6812")
  #initialize pin 38 as input
  input_pin = Pin(38, mode=Pin.IN, pull=Pin.PULL_UP)




def loop():
  global rgb, state
  M5.update()
  if (state=='green'): #if button is pressed change to red state
      if (input_pin.value()):
      #if BtnA.isPressed():
        state = 'red'
        time.sleep(1)
      else:
        #fade in all rgb leds green
        for i in range (100):
          rgb.fill_color(get_color(0,i,0))
          time.sleep_ms(20)
  elif(state == 'red'):
      #if BtnA.isPressed():
      if (input_pin.value()):
        state = 'green'
        time.sleep(1)
      else:
        rgb.set_color(0,0,255)
        time.sleep_ms(20)

  else:
    for i in range (30):
      rgb.set_color(i,0x034830)
      time.sleep_ms(300) 
    rgb.fill_color(0x896f56)
    time.sleep_ms(200)
  
def get_color(r,g,b):
  rgb_color = (r<<16)|(g<<8)|b
  return rgb_color

print('color=',hex(get_color(255,0,0)))
print('color=',hex(get_color(0,255,0)))




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
