import re
import os
import errno
import threading
import brick_control.soundControl as soundControl
import brick_control.bluetoothConnection as bluetoothConnection
import brick_control.motorControl as motorControl
import brick_control.usbConnection as usbConnection
import ledsControl

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

def darudeRun(distance):
    motorCtrl.move(distance, 1)
    motorCtrl.spinAround(180*6)
    motorCtrl.move(distance, 1)
    motorCtrl.spinAround(180*6)

def dance():
    motorCtrl.spinAround(180)
    motorCtrl.spinAround(-60)
    motorCtrl.spinAround(80)
    motorCtrl.spinAround(-60)
    motorCtrl.spinAround(20)
    motorCtrl.spinAround(-160)

        

def filter(frame):
    global running_events
    global soundCtrl
    global motorCtrl
    global ledsCtrl
    
    for object in frame:

        if object.signature == '1':
            #half spin
            motorCtrl.spinAround(180*6)

            t1 = threading.Thread(target=soundCtrl.play, args=("Super Mario", ))
            t2 = threading.Thread(target=motorCtrl.moveArm, args=(4000, 1))
            t3 = threading.Thread(target=ledsCtrl.handle_music, args=("Super Mario", ))

            t1.start()
            t2.start()

            t1.join()
            t2.join()
            t3.join()
            break

        elif object.signature == '4':
            t1 = threading.Thread(target=soundCtrl.play, args=("Darude Sandstorm", ))
            t2 = threading.Thread(target=motorCtrl.moveArm, args=(4000, 1))
            t3 = threading.Thread(target=ledsCtrl.handle_music, args=("Darude Sandstorm", ))
            t4 = threading.Thread(target=darudeRun, args=(5000,))

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            break

        elif object.signature == '6':
            #blue_action()
            t1 = threading.Thread(target=soundCtrl.play, args=("Super Mario Underworld", ))
            t2 = threading.Thread(target=motorCtrl.moveArm, args=(4000, 1))
            t3 = threading.Thread(target=ledsCtrl.handle_music, args=("Super Mario Underworld", ))
            t4 = threading.Thread(target=dance)

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
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
    soundCtrl.playNote(500, 1000)

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



    
