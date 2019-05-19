from PIL import Image
import numpy as np

import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

import random


im = Image.open("image.png")
imageData = np.array(im)



def rotateImageLeft():

    global imageData
    global im

    exists = os.path.isfile('rotated.png')
    if exists:
        tmpImageData = np.array(Image.open("rotated.png"))
    else:
        tmpImageData = np.array(im)

    rotatedImage = np.rot90(tmpImageData)

    Image.fromarray(rotatedImage).save('rotated.png')


def rotateImageRight():

    global imageData
    global im

    exists = os.path.isfile('rotated.png')
    if exists:
        tmpImageData = np.array(Image.open("rotated.png"))
    else:
        tmpImageData = np.array(im)

    rotatedImage = np.rot90(tmpImageData, 3)

    Image.fromarray(rotatedImage).save('rotated.png')


def mirrorReflectionY():
    global imageData

    tmpImageData = imageData[::-1]
    Image.fromarray(tmpImageData).save('mirroredY.png')

def mirrorReflectionX():
    global imageData

    tmpImageData = imageData[:, ::-1]

    Image.fromarray(tmpImageData).save('mirroredX.png')

def inversion():
    global imageData

    tmpImageData = imageData
    tmpImageData[...] = (~imageData[...])

    Image.fromarray(tmpImageData).save('inverted.png')

def grey():
    global imageData

    tmpImageData = np.array(im)

    for i in tmpImageData:
        for j in i:
            tmp = j[0]
            j[1] = tmp
            j[2] = tmp

    Image.fromarray(tmpImageData).save('grey.png')


def brightening():
    tmpImageData = np.array(im)
    tmpImageData[...] = tmpImageData[...] + (256 - tmpImageData[...]) * 0.10
    Image.fromarray(tmpImageData).save('brighter.png')

def darker():
    tmpImageData = np.array(im)
    tmpImageData[...] = tmpImageData[...] - (tmpImageData[...]) * 0.5
    Image.fromarray(tmpImageData).save('darker.png')


def highlighting():
    tmpImageData = np.array(im)
    len1, len2, len3 = tmpImageData.shape

    for i in range(len1-1):
        for j in range(len2-1):
            for k in range(len3-1):
                tmp = (9 * tmpImageData[i, j, k]
                        - tmpImageData[i - 1, j, k]
                        - tmpImageData[i + 1, j, k]
                        - tmpImageData[i, j + 1, k]
                        - tmpImageData[i, j - 1, k]
                        - tmpImageData[i - 1, j + 1, k]
                        - tmpImageData[i - 1, j - 1, k]
                        - tmpImageData[i + 1, j - 1, k]
                        - tmpImageData[i + 1, j + 1, k])
                if tmp < 0:
                    tmp = 0
                if tmp > 255:
                    tmp = 255
                tmpImageData[i, j, k] = tmp

    Image.fromarray(tmpImageData).save('highlighted.png')





if __name__== "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    button1 = QPushButton('Rotate Right')
    button2 = QPushButton('Rotate Left')
    button3 = QPushButton('Make Darker')
    button4 = QPushButton('Make Brighter')
    button5 = QPushButton('Make mirror reflection around X')
    button6 = QPushButton('Make mirror reflection around Y')
    button7 = QPushButton('Highlighting')


    button1.clicked.connect(rotateImageRight)
    button2.clicked.connect(rotateImageLeft)
    button3.clicked.connect(darker)
    button4.clicked.connect(brightening)
    button5.clicked.connect(mirrorReflectionX)
    button6.clicked.connect(mirrorReflectionY)
    button7.clicked.connect(highlighting)



    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addWidget(button4)
    layout.addWidget(button5)
    layout.addWidget(button6)
    layout.addWidget(button7)

    window.setLayout(layout)
    window.show()
    app.exec_()

    os.remove('darker.png')
    os.remove('rotated.png')
    os.remove('highlighted.png')
    os.remove('brighter.png')
    os.remove('mirroredY.png')
    os.remove('mirroredX.png')









