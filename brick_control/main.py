# MAC address of the brick
ID = '00:16:53:0C:93:59'


import nxt.bluesock

import soundControl
import bluetoothConnection
import motorControl


motorCtrl = motorControl.MotorControl(brick, 127)

def darudeRun(distance):
	global motorCtrl

    motorCtrl.move(distance, 1)
    motorCtrl.spinAround(180*6)
    motorCtrl.move(distance, 1)
    motorCtrl.spinAround(180*6)

def dance():
	global motorCtrl

    motorCtrl.spinAround(180)
    motorCtrl.spinAround(-60)
    motorCtrl.spinAround(80)
    motorCtrl.spinAround(-60)
    motorCtrl.spinAround(20)
    motorCtrl.spinAround(-160)

#connect to brick via bluetooth
blueConn = bluetoothConnection.BluetoothConnection(ID)
brick = blueConn.connect()


dance()
