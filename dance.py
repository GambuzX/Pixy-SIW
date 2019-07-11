import RPi.GPIO as GPIO
from time import sleep
from leds import *

ledsToLight = []
sleepTimes = []

for i in range(len(ledsToLight)):
    x = ledsToLight[i]
    if x <= 3:
        #turn led3 on
        turn_on_leftRed()
    elif x > 6:
        #turn led6 on
        turn_on_leftRed()
    sleep(sleepTimes[i])