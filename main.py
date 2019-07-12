import re
import os
import errno
import threading
import brick_control.soundControl as soundControl
import brick_control.bluetoothConnection as bluetoothConnection
import brick_control.motorControl as motorControl
import brick_control.usbConnection as usbConnection
import brick_control.colorControl as colorControl
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

#create color controller object
colorCtrl = colorControl.ColorControl(brick)


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
    global motorCtrl

    motorCtrl.move(distance, 1)
    motorCtrl.spinAround(180, 1)
    motorCtrl.move(distance, 1)
    motorCtrl.spinAround(180, 1)

def dance():
    global motorCtrl

    motorCtrl.spinAround(180, 1)
    sleep(1)
    motorCtrl.spinAround(60, -1)
    sleep(1)
    motorCtrl.spinAround(80, 1)
    sleep(1)
    motorCtrl.spinAround(60, -1)
    sleep(1)
    motorCtrl.spinAround(20, 1)
    sleep(1)
    motorCtrl.spinAround(160, -1)

def waveArm(full):
    global motorCtrl

    motorCtrl.moveArm(650, 1)
    motorCtrl.moveArm(650, -1)
    motorCtrl.moveArm(170, 1)
    if full:
        motorCtrl.moveArm(130, -1)

def minorShake():
    global motorCtrl

    motorCtrl.spinAround(60, 1)
    sleep(1)
    motorCtrl.spinAround(20, -1)
    sleep(1)
    motorCtrl.spinAround(40, 1)
    sleep(1)
    motorCtrl.spinAround(50, -1)
    sleep(1)
    motorCtrl.spinAround(10, 1)
    sleep(1)
    motorCtrl.spinAround(40, -1)
        

def filter(frame):
    global running_events
    global soundCtrl
    global motorCtrl
    global ledsCtrl
    
    for obj in frame:

        if obj.signature == '1':
            #half spin
            motorCtrl.spinAround(180, 1)

            t1 = threading.Thread(target=soundCtrl.play, args=("Super Mario", ))
            t2 = threading.Thread(target=waveArm, args=(True,))
            t3 = threading.Thread(target=ledsCtrl.handle_music, args=("Super Mario", ))
            t4 = threading.Thread(target=minorShake)

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            break

        elif obj.signature == '4':
            t1 = threading.Thread(target=soundCtrl.play, args=("Darude Sandstorm", ))
            t2 = threading.Thread(target=waveArm, args=(False,))
            t3 = threading.Thread(target=ledsCtrl.handle_music, args=("Darude Sandstorm", ))
            t4 = threading.Thread(target=darudeRun, args=(360,))

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            break

        elif obj.signature == '6':
            #blue_action()
            t1 = threading.Thread(target=soundCtrl.play, args=("Super Mario Underworld", ))
            t2 = threading.Thread(target=waveArm, args=(False,))
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
        #print(line)
        objectAttributeList = re.findall(r'[0-9]+', line)
        if len(objectAttributeList) > 4: 
            obj = Object(objectAttributeList[0],objectAttributeList[1],
                        objectAttributeList[2],objectAttributeList[3],
                        objectAttributeList[4])
    frame.append(obj)
    return frame


try:
    os.mkfifo(FIFO)
except OSError as oe: 
    if oe.errno != errno.EEXIST:
        raise

#print("Waiting for camera connection")
with open(FIFO) as fifo:
    #print("Camera has been connected")
    soundCtrl.playNote(500, 1000)

    while True:
        data = fifo.readline()
        #color = colorCtrl.get_color()

        #print color

        if len(data) == 0:
            #print("Writer closed")
            break
        
        #.decode("utf-8")
        if running_events == False:
            running_events = True
            frame = processFrame(data.split('\n'))
            x = threading.Thread(target=filter, args=(frame,))
            x.start()



    
