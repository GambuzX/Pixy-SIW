# Program to make NXT brick beep using NXT Python with Bluetooth socket
#
# Simon D. Levy  CSCI 250   Washington and Lee University    April 2011

# Change this ID to match the one on your brick.  You can find the ID by doing Settings / NXT Version.  
# You will have to put a colon between each pair of digits.
ID = '00:16:53:0C:93:59'

# This is all we need to import for the beep, but you'll need more for motors, sensors, etc.
import nxt.bluesock


from time import sleep
import nxt.locator

# Create socket to NXT brick
sock = nxt.bluesock.BlueSock(ID)

# Connect to brick
brick = sock.connect()

# Play tone A above middle C for 1000 msec
brick.play_tone_and_wait(440, 1000)

C = 523
D = 587
E = 659
G = 784
R = None

def play(note):
    if note:
        brick.play_tone_and_wait(note, 500)
    else:
        sleep(0.5)

for note in [E, D, C, D, E, E, E, R, D, D, D, R, E, G, G, R, E, D, C, D, E, E, E, E, D, D, E, D, C]:
    play(note)

# Close socket
sock.close()

# EOF