import numpy as np
import os.path
import datetime
import string
import math
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
    
    while True == os.path.isfile(concName):
        modL.increaseVal()
        numberExp = '-' + str(configLewis.counter)
        concName = os.path.join(configL.filePath, firstPart + numberExp +'.csv')
    
    modL.updateExactPath(concName)
    fileL = open(concName, 'w')
    fileL.write(firstPart + ' No# '+ configL.counter + '\n')
    fileL.close()

    return configL.counter

def findMax(numpyArray):
    """
    Return maximum value from array numpyArray.
    """

    return numpy.amax(numpyArray, axis=None)

def writeLine(label,alpha,ratio):
    """
    Append data to the file.
    """
    fileL = open(configL.exactPath, 'ab')
    toFile = csv.writer(fileL)
    toFile.writerow([label,alpha,ratio])
    fileL.close()

def handleL(numpyArray):
    """
    Control the process.
    """

    if configL.exactPath == '':
        createFile()
        modL.restartLabel()

    
    maximum = findMax(numpyArray)
    newbie = modL.updateAlpha(maximum)
    modL.updateAlphas(newbie)
    modL.updateRatio(configL.alphas)
    alphaToWrite = configL.alphas[1]
    writeLine(configL.label,alphaToWrite,configL.ratio)

    