import RPi.GPIO as GPIO
from time import sleep

Y=11
M=13
C=11
A=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Y,GPIO.OUT)
GPIO.setup(M,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(A,GPIO.OUT)
fconfigi
GPIO.output(Y,GPIO.LOW)
GPIO.output(M,GPIO.LOW)
GPIO.output(C,GPIO.LOW)
GPIO.output(A,GPIO.LOW)

on = GPIO.HIGH
off = GPIO.LOW

def turn(letter,state):
    try:
        GPIO.output(letter,state)
        sleep(1)
    finally:
        GPIO.cleanup()

def turn_on_Y():
    turn(Y,on)

def turn_on_M():
    turn(M,on)

def turn_on_C():
    turn(C,on)

def turn_on_A():
    turn(A,on)

def turn_off_Y():
    turn(Y,off)

def turn_off_M():
    turn(M,off)

def turn_off_C():
    turn(C,off)

def turn_off_A():
    turn(A,off)

