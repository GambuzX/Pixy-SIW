import threading
import brick_control.soundControl as soundControl
import brick_control.usbConnection as usbConnection
import brick_control.motorControl as motorControl
import ledsControl

from time import sleep

#connect to brick via usb
usbConn = usbConnection.USBConnection()
brick = usbConn.connect()

#create sound controller object
soundCtrl = soundControl.SoundControl(brick)

#create leds controller object
ledsCtrl = ledsControl.LEDsControl(brick)

motorCtrl = motorControl.MotorControl(brick)

ledsCtrl.turn_row_on(1)
ledsCtrl.turn_row_on(2)
ledsCtrl.turn_row_on(3)
ledsCtrl.turn_row_on(4)


t1 = threading.Thread(target=soundCtrl.play, args=("Super Mario",))
t2 = threading.Thread(target=ledsCtrl.handle_music, args=("Super Mario",))
t2 = threading.Thread(target=motorCtrl.moveArm, args=(50000, 100,))

t1.start()
t3.start()

t1.join()
t3.join()

sleep(10)