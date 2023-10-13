import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb = None
input_pin = None
has_dimmed = False  

# 2 color sets
colors_set1 = [
    (14, 29, 195),  
    (78, 45, 206), 
    (12, 23, 210),  
    (11, 117, 164), 
    (13, 107, 223), 
    (55, 54, 194), 
    (18, 49, 206), 
    (78, 79, 203), 
    (14, 76, 156),  
    (43, 19, 124) 
] * 3  

colors_set2 = [
    (220, 90, 70),  
    (232, 38, 94), 
    (191, 10, 12), 
    (200, 27, 70),
    (241, 24, 3), 
    (215, 84, 85), 
    (204, 84, 58),
    (247, 92, 47),  
    (241,48, 11),
    (238, 69, 98)
] * 3

current_colors = colors_set1 

def setup():
    global rgb, input_pin
    M5.begin()
  
    rgb = RGB(io=2, n=30, type="SK6812")
    input_pin = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)

def loop():
    global input_pin, has_dimmed, current_colors
    M5.update()

    if input_pin.value() == 0:
        if not has_dimmed: 
            for intensity in reversed(range(10)):
                for i in range(30): 
                    r, g, b = current_colors[i]
                    rgb.set_color(i, get_color(int(r * intensity / 10), int(g * intensity / 10), int(b * intensity / 10)))
                time.sleep_ms(10)
            has_dimmed = True
    else:


        initial_delay = 450 
        decrease_factor = 15 
        current_delay = initial_delay
        for i in range(30): 
            r, g, b = current_colors[i]
            rgb.set_color(i, get_color(r, g, b))
            time.sleep_ms(current_delay)
            current_delay = max(10, current_delay - decrease_factor) 
            
        if current_colors == colors_set2:
          for _ in range(2):  
            # Fade out
            for intensity in reversed(range(28)):
                for i in range(30): 
                    r, g, b = colors_set2[i]
                    rgb.set_color(i, get_color(int(r * intensity / 10), int(g * intensity / 10), int(b * intensity / 10)))
                time.sleep_ms(10)
            
            # Fade in
            for intensity in range(20):
                for i in range(30): 
                    r, g, b = colors_set2[i]
                    rgb.set_color(i, get_color(int(r * intensity / 10), int(g * intensity / 10), int(b * intensity / 10)))
                time.sleep_ms(10)
                
        if current_colors == colors_set1:
            current_colors = colors_set2
        else:
            current_colors = colors_set1
            
        has_dimmed = False 

def get_color(r, g, b):
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color

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
