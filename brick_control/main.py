# MAC address of the brick
ID = '00:16:53:0C:93:59'


import nxt.bluesock

import soundControl
import bluetoothConnection

#connect to brick via bluetooth
blueConn = bluetoothConnection.BluetoothConnection(ID)

brick = blueConn.connect()

#do stuff with sound
soundCtrl = soundControl.SoundControl(brick).playSong()