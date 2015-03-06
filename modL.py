import configL
import math
import time

def increaseVal():
    configL.counter += 1

def updateAlpha(mReceived):
    """
    It takes the natural logarithm of the percentage of mReceived received
    and mSen sent signal; and multiply this by -1/zDistance distance.

    Example;
    input math.e, sent = 1 distance = 1
    >>>updateAlpha(math.e)
    >>>-1
    """
    
    configL.alpha = (-float(1)/configL.zDistance)*(math.log(float(mReceived)/configL.mSent))
    return

def updateAlphas(newAlpha):
    if configL.alphas[1] == 'None':
        configL.alphas[1] = newAlpha
    else:
        temp = configL.alphas[1]
        configL.alphas[0] = configL.alphas[1]
        configL.alphas[1] = newAlpha
    return configL.alphas

def updateRatio(alphas):
    """
    Returns the ratio between alpha1 and alpha2.
    """
        
    if configL.alphas[0] == None:
        return 'nan'
    else:
        #print alphas[0]
        #print alphas[1]
        #print type(alphas[0])
        #print type(alphas[1])
        configL.ratio = float(alphas[0])/float(alphas[1])

def updateExactPath(filePath):
    configL.exactPath = filePath

def updateLabel():
    configL.label += 1

def restartLabel():
    configL.label = 1

def startTimer():
    configL.timeMeasure = time.clock()

def calcTime():
    #processor time difference in seconds (float)
    timeNow = time.clock()
    configL.timeDifference = timeNow - configL.timeMeasure

def quantityCount():
    fileL = open(configL.exactPath, 'r')
    lines = fileL.readlines()
    fileL.close()
    counter = 1
    for e in lines:
        if 'Sent signal' in e:
            counter += 1
    return counter
