import RPi.GPIO as GPIO
from time import sleep

V=11
V1=19
V2=21
V3=23
V4=22
V5=24
V6=26
B=13
B2=15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(V,GPIO.OUT)
GPIO.setup(V1,GPIO.OUT)
GPIO.setup(V2,GPIO.OUT)
GPIO.setup(V3,GPIO.OUT)
GPIO.setup(V4,GPIO.OUT)
GPIO.setup(V5,GPIO.OUT)
GPIO.setup(V6,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(B2,GPIO.OUT)

GPIO.output(V,GPIO.LOW)

GPIO.output(V,GPIO.LOW)
GPIO.output(B,GPIO.LOW)
GPIO.output(B2,GPIO.LOW)
GPIO.output(V,GPIO.LOW)
GPIO.output(B,GPIO.LOW)
GPIO.output(B2,GPIO.LOW)
GPIO.output(B,GPIO.LOW)
GPIO.output(B2,GPIO.LOW)

on = GPIO.HIGH
off = GPIO.LOW

def turn(letter,state):
    GPIO.output(letter,state)

def turn_on_red():
    turn(V,on)

def turn_on_white():
    turn(B,on)
    turn(B2,on)

def turn_off_red():
    turn(V,off)

def turn_off_white():
    turn(B,off)
    turn(B2,off)

def turn_on_mush():
    turn_on_red()
    turn_on_white()
    sleep(1)

def turn_off_mush():
    turn_off_red()
    turn_off_white()
    sleep(1)

def turn_on_leftRed():
    turn(V1,on)
    turn(V2,on)

def turn_on_middleRed():
    turn(V3,on)
    turn(V4,on)
    turn_on_white()

def turn_on_rightRed():
    turn(V5,on)
    turn(V6,on)

def turn_off_leftRed():
    turn(V1,off)
    turn(V2,off)
    
def turn_off_middleRed():
    turn(V3,off)
    turn(V4,off)
    turn_off_white()

def turn_off_rightRed():
    turn(V5,off)
    turn(V6,off)
