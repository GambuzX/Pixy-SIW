import RPi.GPIO as GPIO
from time import sleep

V=11
B=13
B2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(V,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)

GPIO.output(V,GPIO.LOW)
GPIO.output(B,GPIO.LOW)

on = GPIO.HIGH
off = GPIO.LOW

def turn(letter,state):
    try:
        GPIO.output(letter,state)
        sleep(1)
    finally:
        GPIO.cleanup()

def turn_on_red():
    turn(Y,on)

def turn_on_white():
    turn(M,on)

def turn_off_C():
    turn(C,off)

def turn_off_A():
    turn(A,off)

