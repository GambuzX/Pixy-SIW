from time import sleep
import nxt.locator


class SoundControl(object):
	def __init__(self, brick):
		self.brick = brick

		# C5, D5, ...
		# https://en.wikipedia.org/wiki/Piano_key_frequencies
		self.freq = {
			'B0' : 31,
			'C1' : 33,
			'CS1' : 35,
			'D1' : 37,
			'DS1' : 39,
			'E1' : 41,
			'F1' : 44,
			'FS1' : 46,
			'G1' : 49,
			'GS1' : 52,
			'A1' : 55,
			'AS1' : 58,
			'B1' : 62,
			'C2' : 65,
			'CS2' : 69,
			'D2' : 73,
			'DS2' : 78,
			'E2' : 82,
			'F2' : 87,
			'FS2' : 93,
			'G2' : 98,
			'GS2' : 104,
			'A2' : 110,
			'AS2' : 117,
			'B2' : 123,
			'C3' : 131,
			'CS3' : 139,
			'D3' : 147,
			'DS3' : 156,
			'E3' : 165,
			'F3' : 175,
			'FS3' : 185,
			'G3' : 196,
			'GS3' : 208,
			'A3' : 220,
			'AS3' : 233,
			'B3' : 247,
			'C4' : 262,
			'CS4' : 277,
			'D4' : 294,
			'DS4' : 311,
			'E4' : 330,
			'F4' : 349,
			'FS4' : 370,
			'G4' : 392,
			'GS4' : 415,
			'A4' : 440,
			'AS4' : 466,
			'B4' : 494,
			'C5' : 523,
			'CS5' : 554,
			'D5' : 587,
			'DS5' : 622,
			'E5' : 659,
			'F5' : 698,
			'FS5' : 740,
			'G5' : 784,
			'GS5' : 831,
			'A5' : 880,
			'AS5' : 932,
			'B5' : 988,
			'C6' : 1047,
			'CS6' : 1109,
			'D6' : 1175,
			'DS6' : 1245,
			'E6' : 1319,
			'F6' : 1397,
			'FS6' : 1480,
			'G6' : 1568,
			'GS6' : 1661,
			'A6' : 1760,
			'AS6' : 1865,
			'B6' : 1976,
			'C7' : 2093,
			'CS7' : 2217,
			'D7' : 2349,
			'DS7' : 2489,
			'E7' : 2637,
			'F7' : 2794,
			'FS7' : 2960,
			'G7' : 3136,
			'GS7' : 3322,
			'A7' : 3520,
			'AS7' : 3729,
			'B7' : 3951,
			'C8' : 4186,
			'CS8' : 4435,
			'D8' : 4699,
			'DS8' : 4978,
			'R' : None
		}

		self.songs = {
			"Super Mario" : {
				"freqs" : ['E7', 'E7', 'R', 'E7', 'R', 'C7', 'E7', 'R', 'G7', 'R', 'R', 'R', 'G6', 'R', 'R', 'R', 'C7', 'R', 'R', 'G6', 'R', 'R', 'E6', 'R', 'R', 'A6', 'R', 'B6', 'R', 'AS6', 'A6', 'R', 'G6', 'E7', 'G7', 'A7', 'R', 'F7', 'G7', 'R', 'E7', 'R', 'C7', 'D7', 'B6', 'R', 'R', 'C7', 'R', 'R', 'G6', 'R', 'R', 'E6', 'R', 'R', 'A6', 'R', 'B6', 'R', 'AS6', 'A6', 'R', 'G6', 'E7', 'G7', 'A7', 'R', 'F7', 'G7', 'R', 'E7', 'R', 'C7', 'D7', 'B6', 'R', 'R'],
				"tempos" : [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
			},

			"Super Mario Underworld" : {
				"freqs" : ['C4', 'C5', 'A3', 'A4', 'AS3', 'AS4', 'R', 'R', 'C4', 'C5', 'A3', 'A4', 'AS3', 'AS4', 'R', 'R', 'F3', 'F4', 'D3', 'D4', 'DS3', 'DS4', 'R', 'R', 'F3', 'F4', 'D3', 'D4', 'DS3', 'DS4', 'R', 'R', 'DS4', 'CS4', 'D4', 'CS4', 'DS4', 'DS4', 'GS3', 'G3', 'CS4', 'C4', 'FS4', 'F4', 'E3', 'AS4', 'A4', 'GS4', 'DS4', 'B3', 'AS3', 'A3', 'GS3', 'R', 'R', 'R'],
				"tempos" : [12, 12, 12, 12, 12, 12, 6, 3, 12, 12, 12, 12, 12, 12, 6, 3, 12, 12, 12, 12, 12, 12, 6, 3, 12, 12, 12, 12, 12, 12, 6, 6, 18, 18, 18, 6, 6, 6, 6, 6, 6, 18, 18, 18, 18, 18, 18, 10, 10, 10, 10, 10, 10, 3, 3, 3]
			},

			"Darude Sandstorm" : {
				"freqs" : ['B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'E4', 'R', 'E4', 'R', 'E4', 'R', 'E4', 'R', 'E4', 'R', 'E4', 'R', 'E4', 'R', 'D4', 'R', 'D4', 'R', 'D4', 'R', 'D4', 'R', 'D4', 'R', 'D4', 'R', 'D4', 'R', 'A3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'E4', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'B3', 'R', 'E4', 'R'],
				"tempos" : [80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500, 80, 500]
			},
			"Mary" : {
				"freqs" : ['E5', 'D5', 'C5', 'D5', 'E5', 'E5', 'E5', 'R', 'D5', 'D5', 'D5', 'R', 'E5', 'G5', 'G5', 'R', 'E5', 'D5', 'C5', 'D5', 'E5', 'E5', 'E5', 'E5', 'D5', 'D5', 'E5', 'D5', 'C5'],
				"tempos" : None
			}
		}

		self.songs["Super Mario"]["tempos"] = [x / 1.8 for x in self.songs["Super Mario"]["tempos"]]
		self.songs["Super Mario Underworld"]["tempos"] = [x / 1.8 for x in self.songs["Super Mario Underworld"]["tempos"]]
		self.songs["Darude Sandstorm"]["tempos"] = [x / 10 for x in self.songs["Darude Sandstorm"]["tempos"]]


	def play(self, song):		
		try:
			self.playSong(self.songs[song]["freqs"], self.songs[song]["tempos"])
		except KeyError:
			return


	def playSong(self, notes, tempo=None):
		for i in range(len(notes)):
			if (tempo == None):
				self.playNote(self.freq[notes[i]])
			else:
				dur = 1000 / tempo[i] #note duration in seconds
				self.playNote(self.freq[notes[i]], dur)
		

	def playNote(self, note, duration=500):
	    if note:
	        self.brick.play_tone_and_wait(note, duration)
	    else:
	    	self.brick.play_tone_and_wait(0, duration)