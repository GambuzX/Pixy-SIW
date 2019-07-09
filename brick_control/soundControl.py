from time import sleep
import nxt.locator


class SoundControl(object):
	def __init__(self, brick):
		self.brick = brick

	def playSong(self):	
		C = 523
		D = 587
		E = 659
		G = 784
		R = None

		for note in [E, D, C, D, E, E, E, R, D, D, D, R, E, G, G, R, E, D, C, D, E, E, E, E, D, D, E, D, C]:
		    self.play(note)
		

	def play(self, note):
	    if note:
	        self.brick.play_tone_and_wait(note, 500)
	    else:
	        sleep(0.5)