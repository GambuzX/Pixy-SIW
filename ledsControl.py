import RPi.GPIO as GPIO
from time import sleep

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
		self.GW2=18 # group white 2

		self.setup_leds()


	def setup_leds(self):
		global on
		global off

		try:
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(self.GR1,GPIO.OUT)
			GPIO.setup(self.GR2,GPIO.OUT)
			GPIO.setup(self.GR3,GPIO.OUT)
			GPIO.setup(self.GW1,GPIO.OUT)
			GPIO.setup(self.GW2,GPIO.OUT)
		
		except:
			GPIO.cleanup()


		GPIO.output(self.GR1,off)
		GPIO.output(self.GR2,off)
		GPIO.output(self.GR3,off)
		GPIO.output(self.GW1,off)
		GPIO.output(self.GW2,off)


	def turn(self, letter,state):
		GPIO.output(letter,state)


	def turn_row_on(self, row):
		global on
		global off

		if row == 1:
		    self.turn(self.GR1, on)

		if row == 2:
		    self.turn(self.GR2, on)

		if row == 3:
		    self.turn(self.GR3, on)

		if row == 4:
		    self.turn(self.GW1, on)

		if row == 5:
			self.turn(self.GW2, on)


	def turn_row_off(self, row):
		global on
		global off

		if row == 1:
		    self.turn(self.GR1, off)

		if row == 2:
		    self.turn(self.GR2, off)

		if row == 3:
		    self.turn(self.GR3, off)

		if row == 4:
		    self.turn(self.GW1, off)

		if row == 5:
			self.turn(self.GW2, off)


	def handle_music(self, music):
		ledsToLight = self.soundControl.freqScale(music)
		sleepTimes = self.soundControl.temposDurations(music)

		for i in range(len(ledsToLight)):
		    x = ledsToLight[i]

		    if x > 0:
		    	#turn on first group
		    	self.turn_row_on(1)
		    if x > 1:
		    	#turn on second group
		    	self.turn_row_on(2)
		    if x > 2:
		    	#turn on third group
		    	self.turn_row_on(3)
		    if x > 3:
		    	#turn on fourth group
		    	self.turn_row_on(4)

		    if x > 4:
		    	#turn on fifth group
		    	self.turn_row_on(5)

		    sleep(sleepTimes[i])

		    #turn off everything
		    self.turn_row_off(1)
		    self.turn_row_off(2)
		    self.turn_row_off(3)
		    self.turn_row_off(4)
		    self.turn_row_off(5)