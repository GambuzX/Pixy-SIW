import threading
import brick_control.soundControl as soundControl
import brick_control.usbConnection as usbConnection
import brick_control.motorControl as motorControl
import ledsControl

#connect to brick via usb
usbConn = usbConnection.USBConnection()
brick = usbConn.connect()

#create sound controller object
soundCtrl = soundControl.SoundControl(brick)

#create leds controller object
ledsCtrl = ledsControl.LEDsControl(brick)

ledsCtrl.turn_row_on(1)

''''
t1 = threading.Thread(target=soundCtrl.play, args=("Super Mario",))
t2 = threading.Thread(target=ledsCtrl.handle_music, args=("Super Mario",))

t1.start()
t2.start()

t1.join()
t2.join()
    '''
