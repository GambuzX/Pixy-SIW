# MAC address of the brick
ID = '00:16:53:0C:93:59'

import nxt.bluesock

import soundControl

# Create socket to NXT brick and connect to it
sock = nxt.bluesock.BlueSock(ID)

brick = sock.connect()

soundCtrl = soundControl.SoundControl(brick)

soundCtrl.playSong()

# Close socket
sock.close()