from nxt.motor import *
import threading

class MotorControl(object):

	def __init__(self, brick, power):
		self.brick = brick
		self.power = power
		self.degrees_correction = 6

	def spinAround(self, degrees, direction):
		t1 = threading.Thread(target=self.turnMotor, args=(PORT_C, self.power*direction, degrees,))
		#t2 = threading.Thread(target=self.turnMotor, args=(PORT_A, -1 * self.power, degrees,))

		t1.start()
		#t2.start()

		t1.join()
		#t2.join()

	def move(self, degrees, dir):
		t1 = threading.Thread(target=self.turnMotor, args=(PORT_A, self.power * dir, degrees,))
		t2 = threading.Thread(target=self.turnMotor, args=(PORT_C, self.power * dir, degrees,))

		t1.start()
		t2.start()

		t1.join()
		t2.join()

	def moveArm(self, degrees, dir):
		self.turnMotor(PORT_B, self.power * dir, degrees)


	def turnMotor(self, port, power, degrees):
		motor = Motor(self.brick, port)
		motor.turn(self.power, degrees * self.degrees_correction)

