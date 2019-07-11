import nxt.locator

class USBConnection:

	def connect(self):
		return nxt.locator.find_one_brick()
