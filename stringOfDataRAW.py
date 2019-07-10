import re

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
        

def filter(frame):
    for object in frame:
        if object.signature == '4':
            print ("Green")
            
        
def processFrame (objectsFromFrame = []):
    
    frame = []
    for line in objectFromFrame:
        objectAttributeList = re.findall(r'[0-9]+', line))
        object = Object(objectAttributeList[0],objectAttributeList[1],
                        objectAttributeList[2],objectAttributeList[3])
    frame.append(object)
    return frame

    
        
    #print(dataRaw)


frame = processFrame()

filter(frame)
    
