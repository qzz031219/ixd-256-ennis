#controlling a servo using servo library
#servo_online.py library file should be burned on AtomS3 board

from servo_online import Servo
from hardware import *
import time


servo = Servo(pin=7)
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)


      
def map_value(in_val, in_min, in_max, out_min, out_max):
  v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if (v < out_min): 
    v = out_min 
  elif (v > out_max): 
    v = out_max
  return int(v)

while(True):
    # read 12-bit analog value (0 - 4095 range):
    adc_val = adc.read()
    # convert adc_val from 12-bit to 8-bit (0 - 255 range):
    servo_val = map_value(adc_val, in_min = 0, in_max = 4095,
                           out_min = 90, out_max = 150)
    
    print(adc_val, end=' => ')
    print(servo_val)
    servo.move(servo_val)  
    time.sleep_ms(100)  
