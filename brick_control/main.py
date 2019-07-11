# MAC address of the brick
ID = '00:16:53:0C:93:59'


import nxt.bluesock

import soundControl
import bluetoothConnection
import motorControl

#connect to brick via bluetooth
blueConn = bluetoothConnection.BluetoothConnection(ID)
brick = blueConn.connect()

#do stuff with sound
soundCtrl = soundControl.SoundControl(brick)
soundCtrl.play("Mary")

#rotate robot
#motor = motorControl.MotorControl(brick, 127)
#motor.moveArm(5000, 1)

#motor.move(5000, 1)
#motor.spinAround(5000)
#motor.move(5000, -1)
