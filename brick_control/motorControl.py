from nxt.motor import *
import threading

class MotorControl(object):

	def __init__(self, brick):
		self.brick = brick

	def spinAround(self):
		t1 = threading.Thread(target=self.turnMotor, args=(PORT_C, 100, 720,))
		t2 = threading.Thread(target=self.turnMotor, args=(PORT_A, -100, 720,))

		t1.start()
		#t2.start()

		t1.join()
		#t2.join()

	def turnMotor(self, port, power, tacho_units):
		motor = Motor(self.brick, port)
		motor.turn(power, tacho_units)

