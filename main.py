import re
import os
import errno
import threading
import brick_control.soundControl as soundControl
import brick_control.bluetoothConnection as bluetoothConnection
import brick_control.motorControl as motorControl
import brick_control.usbConnection as usbConnection
from high_leds import *

ID = '00:16:53:0C:93:59'
FIFO = '/tmp/pixy'
running_events = False


#connect to brick via usb
usbConn = usbConnection.USBConnection()
brick = usbConn.connect()

#create sound controller object
soundCtrl = soundControl.SoundControl(brick)    

#rotate robot
#motor = motorControl.MotorControl(brick, 127)

#motor.move(5000, 1)
#motor.spinAround(5000)
#motor.move(5000, -1)
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
        
    for object in frame:
        if object.signature == '4':
            #do stuff with sound
            blue_action()
            soundCtrl.playSuperMario()
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



    
