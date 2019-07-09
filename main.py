import re

def returnStringOfDataRAW (dataRaw = []):
    for line in dataRaw:
        for eachLine in line.split('\n'):
           array= re.findall(r'[0-9]+', eachLine)
           print(array)
           
        
    print(dataRaw)
