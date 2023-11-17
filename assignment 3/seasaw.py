from machine import Pin, PWM
import time

servo = PWM(Pin(7)) 
servo.freq(50)      

BUTTON_PIN = 41  
PRESSURE_SENSOR_PIN = 6  
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
pressure_sensor = Pin(PRESSURE_SENSOR_PIN, Pin.IN)


STOP_DUTY = 75

def rotate_servo(direction, duration=0.5):
    if direction == "forward":
        servo.duty(81)  # Rotate forward
    elif direction == "backward":
        servo.duty(70)  # Rotate backward
    time.sleep(duration)  # Adjust rotation duration
    servo.duty(STOP_DUTY)  # Stop servo

def seesaw_control():
    while True:
        if not button.value():
            print("Button pressed")
            rotate_servo("forward")

            while True:
                pressure_value = pressure_sensor.value()
                print("Pressure Sensor Value:", pressure_value)
                time.sleep(0.1)

                if pressure_value == 0:
                    break

            rotate_servo("backward")

# Run the seesaw control
seesaw_control()
