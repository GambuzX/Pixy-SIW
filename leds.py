import RPi.GPIO as GPIO
from time import sleep

V=11
B=13
B2 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(V,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(B2,GPIO.OUT)

GPIO.output(V,GPIO.LOW)
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

