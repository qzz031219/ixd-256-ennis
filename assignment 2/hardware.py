import os, sys, io
import M5
from M5 import *
from hardware import *
import time

adc = None
adc_val = None
rgb = None
adc_calibration_val = None
adc_timer = 0
button_pressed = False 

def setup():
    global adc, adc_val, rgb, adc_calibration_val
    M5.begin()
    adc = ADC(Pin(1), atten=ADC.ATTN_11DB)
    rgb = RGB(io=38, n=30, type="SK6812")
    time.sleep_ms(500)
    set_calibration()
      
def set_calibration():
    global adc_calibration_val
    adc_calibration_val = adc.read()
    print('set calibration value..', adc_calibration_val)

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def loop():
    global adc, adc_val, adc_timer, adc_calibration_val, button_pressed
    M5.update()

    if BtnA.wasPressed() and not button_pressed:
        button_pressed = True
        print('TOGGLE_SHAPE') 

    if not BtnA.isPressed() and button_pressed:
        button_pressed = False
    
    if (time.ticks_ms() > adc_timer + 100):
        adc_val = adc.read()
        mapped_val = map_value(adc_val, 0, 4095, 0, 255) 
        print(mapped_val)
        adc_timer = time.ticks_ms()

    time.sleep_ms(100)

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
