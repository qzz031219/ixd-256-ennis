from machine import Pin
import time

relay_pin = Pin(7, mode = Pin.OUT)

while(True):
    relay_pin.on()
    time.sleep(1)
    relay_pin.off()
    time.sleep(1)