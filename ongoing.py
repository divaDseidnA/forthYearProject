##The MIT License (MIT)
##
##Copyright (c) <2015> <David Nagy>
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in
##all copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
##THE SOFTWARE.

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

    