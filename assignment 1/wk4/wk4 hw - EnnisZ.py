import os, sys, io
import M5
from M5 import *
from hardware import *
import time

pin1 = None
pwm1 = None
pin2 = None

def setup():
    global pin1, pwm1, pin2

    M5.begin()
    pin1 = Pin(1, mode=Pin.OUT)
    pwm1 = PWM(Pin(1), freq=20000, duty=512)
    pin2 = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP) 

def loop():
    global pin1, pwm1, pin2
    M5.update()

    if input_pin.value() == 1: # disconnected
        for i in range(100,500,2): 
            pwm1.duty(i)
            time.sleep_ms(10)
        for duty in range(500, 100, -2):
            pwm1.duty(i)
            time.sleep_ms(10)
    else:
        pwm1.duty(0) # connected

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
