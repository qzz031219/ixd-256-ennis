import network
import urequests
import M5
from M5 import *
from hardware import *

wlan = network.WLAN(network.STA_IF)
print('wlan.isconnected() =', wlan.isconnected())

while(True):
    M5.update()
    if BtnA.wasPressed():
        print('button pressed!')
        req = urequests.request(
            method='POST',
            #url='https://maker.ifttt.com/trigger/button_press/with/key/cMJoJED0JlNmz4qDTLZKjD',
            url='https://maker.ifttt.com/trigger/button_press/json/with/key/cMJoJED0JlNmz4qDTLZKjD',
            json={'value1':'0'},
            headers={'Content-Type': 'application/json'})
        print('success!')