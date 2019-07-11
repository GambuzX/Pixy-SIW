import RPi.GPIO as GPIO
from time import sleep
from leds import *

from brick_control.soundControl import *
from brick_control.bluetoothConnection import *

on = GPIO.HIGH
off = GPIO.LOW

class LEDsControl:
	def __init__(self, brick):
		self.soundControl = SoundControl(brick)

		self.GR1=11 # group red 1
		self.GR2=13 # group red 2
		self.GR3=15 # group red 3
		self.GW1=16 # group white 1

		self.setup_leds()


	def setup_leds(self):
		global on
		global off

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.GR1,GPIO.OUT)
		GPIO.setup(self.GR2,GPIO.OUT)
		GPIO.setup(self.GR3,GPIO.OUT)
		GPIO.setup(self.GW1,GPIO.OUT)

		GPIO.output(self.GR1,off)
		GPIO.output(self.GR2,off)
		GPIO.output(self.GR3,off)
		GPIO.output(self.GW1,off)


	def turn(letter,state):
	    GPIO.output(letter,state)


	def turn_row_on(row):
		global on
		global off

	    if row == 1:
	        turn(self.GR1, on)
	    if row == 2:
	        turn(self.GR2, on)
	    if row == 3:
	        turn(self.GR3, on)
	    if row == 4:
	        turn(self.GW1, on)


	def turn_row_off(row):
		global on
		global off

	    if row == 1:
	        turn(self.GR1, off)
	    if row == 2:
	        turn(self.GR2, off)
	    if row == 3:
	        turn(self.GR3, off)
	    if row == 4:
	        turn(self.GW1, off)


	def handle_music(music):
		ledsToLight = self.soundControl.freqScale(music)
		sleepTimes = self.soundControl.temposDurations(music)

		for i in range(len(ledsToLight)):
		    x = ledsToLight[i]

		    if x > 0:
		    	#turn on first group
		    	turn_row_on(1)
		    if x > 1:
		    	#turn on second group
		    	turn_row_on(2)
		    if x > 2:
		    	#turn on third group
		    	turn_row_on(3)
		    if x > 3:
		    	#turn on fourth group
		    	turn_row_on(4)

		    sleep(sleepTimes[i])

		    #turn off everything
		    turn_row_off(1)
		    turn_row_off(2)
		    turn_row_off(3)
		    turn_row_off(4)