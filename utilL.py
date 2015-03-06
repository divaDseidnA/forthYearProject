import numpy as np
import os.path
import datetime
import configL
import modL
import csv


def createFile():
    """
    
    Create file into a chosen folder.

    Example for filePath format:
    'C:/Users/David/Documents/Personal files/Code/Python file'
    """
 
    #creating name
    firstPart = str(datetime.date.today())
    numberExp = '-' + str(configL.counter)
    
    #concatinating name
    concName = os.path.join(configL.filePath, firstPart + numberExp +'.csv')
    print concName
    
    #this section gives the opportunity for saving measurement into separate files
    # while True == os.path.isfile(concName):
    #     modL.increaseVal()
    #     numberExp = '-' + str(configL.counter)
    #     concName = os.path.join(configL.filePath, firstPart + numberExp +'.csv')

    if True != os.path.isfile(concName):
        fileL = open(concName, 'w')
        fileL.close()

    modL.updateExactPath(concName)

    noOfExp = modL.quantityCount()
    
    fileL = open(concName, 'a')
    
    if noOfExp != 1:
        fileL.write('' + '\n')

    fileL.write(str(firstPart) + ' No# '+ str(noOfExp) + '\n')
    fileL.write('Sent signal: ' + str(configL.mSent) + '\n')
    fileL.write('zDistance: ' + str(configL.zDistance) + '\n')
    fileL.close()
    writeLine('Cycles','Alpha','Ratio','Time Difference')

    return configL.counter

def findMax(numpyArray):
    """
    Return maximum value from array numpyArray.
    """

    return np.amax(numpyArray, axis=None)

def writeLine(label,alpha,ratio,timeDiff):
    """
    Append data to the file.
    """
    fileL = open(configL.exactPath, 'ab')
    toFile = csv.writer(fileL)
    toFile.writerow([label,alpha,ratio,timeDiff])
    fileL.close()

def handleL(numpyArray):
    """
    Wrap up.
    Assumption: the type of the argument numpyArray is numpy array.
    """

    if configL.timeMeasure == 0:
        modL.startTimer()
    else:
        modL.calcTime()

    if configL.exactPath == '':
        createFile()
        modL.restartLabel()

    
    maximum = findMax(numpyArray)
    #print 'Maximum: ' + str(maximum)
    modL.updateAlpha(maximum)
    #print 'newbie: ' + str(configL.alpha)
    modL.updateAlphas(configL.alpha)
    modL.updateRatio(configL.alphas)
    alphaToWrite = configL.alphas[1]
    writeLine(configL.label,alphaToWrite,configL.ratio, configL.timeDifference)
    modL.updateLabel()