import re
import os
import errno
import threading
import brick_control.soundControl as soundControl
import brick_control.bluetoothConnection as bluetoothConnection
import brick_control.motorControl as motorControl
import brick_control.usbConnection as usbConnection
import leds_control as ledsControl
from high_leds import *

#global variables
ID = '00:16:53:0C:93:59'
FIFO = '/tmp/pixy'
running_events = False

#connect to brick via usb
usbConn = usbConnection.USBConnection()
brick = usbConn.connect()

#create sound controller object
soundCtrl = soundControl.SoundControl(brick)

#create motor controller object
motorCtrl = motorControl.MotorControl(brick, 120)

#create leds controller object
ledsCtrl = ledsControl.LEDsControl(brick)


class Object:
    width = 0
    height = 0
    x = 0
    y = 0
    signature = 0
    def __init__(self, signature, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.signature = signature
        

def filter(frame):
    global running_events
    global soundCtrl
    global motorCtrl
    global ledsCtrl
    
    for object in frame:

        if object.signature == '1':
            red_action()
            soundCtrl.playDarude()
            #mega spin

            #t1 = threading.Thread(target=soundCtrl.playDarude)
            #t2 = threading.Thread(target=motorCtrl.doSomething, args=(1,2,3,))
            break

        elif object.signature == '4':
            green_action()
            soundCtrl.playSuperMario()
            #danceeee
            break

        elif object.signature == '6':
            blue_action()
            soundCtrl.playSuperMarioUnderworld()
            #mega run
            break

    running_events = False
    

            
        
def processFrame (objectsFromFrame = []):
    
    frame = []
    for line in objectsFromFrame:
        print(line)
        objectAttributeList = re.findall(r'[0-9]+', line)
        if len(objectAttributeList) > 4: 
            object = Object(objectAttributeList[0],objectAttributeList[1],
                        objectAttributeList[2],objectAttributeList[3],
                        objectAttributeList[4])
    frame.append(object)
    return frame

    
        
    #print(dataRaw)


try:
    os.mkfifo(FIFO)
except OSError as oe: 
    if oe.errno != errno.EEXIST:
        raise

print("Waiting for camera connection")
with open(FIFO) as fifo:
    print("Camera has been connected")
    while True:
        data = fifo.readline()
        if len(data) == 0:
            print("Writer closed")
            break
        
        #.decode("utf-8")
        if running_events == False:
            running_events = True
            frame = processFrame(data.split('\n'))
            x = threading.Thread(target=filter, args=(frame,))
            x.start()



    
