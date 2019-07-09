import nxt.bluesock

class BluetoothConnection(object):
	# create socket to brick
	def __init__(self, mac):
		self.sock = nxt.bluesock.BlueSock(mac)

	# delete socket
	def __del__(self):
		self.sock.close()


	# connects and returns brick object
	def connect(self):
		return self.sock.connect()
