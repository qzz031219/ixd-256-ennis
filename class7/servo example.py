from machine import Pin, PWM
import time

servo = PWM(Pin(7))
#configure PWM frequency:
servo.freq(50)

while(True):
    #move servo clockwive by changing PWM duty:
    servo.duty(26)
    time.sleep(1)
    #move servo clockwive by changing PWM duty:
    servo.duty(123)
    time.sleep(1)