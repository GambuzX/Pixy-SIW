from nxt.sensor import *

class ColorControl(object):

	def __init__(self, brick):
		self.brick = brick
		self.colorSensor = Color20(brick, PORT_1)

	def get_color(self):
		return self.colorSensor.get_color()

	def get_light_color(self):
		return self.colorSensor.get_light_color()

	def set_light_color(self, color):
		self.colorSensor.set_light_color(color)
