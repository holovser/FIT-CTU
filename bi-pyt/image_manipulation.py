from PIL import Image
import numpy as np

im = Image.open("image.png")
imageData = np.array(im)


f = open("demofile.txt", "a")


def rotateImageRight(count=1):
    global imageData

    tmpImageData = imageData

    for i in range(count):
        tmpImageData = np.rot90(imageData)

    Image.fromarray(tmpImageData).save('rotated.png')


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

    tmpImageData = imageData

    for i in tmpImageData:
        for j in i:
            tmp = j[0]
            j[1] = tmp
            j[2] = tmp

    Image.fromarray(imageData).save('grey.png')



rotateImageRight(2)
mirrorReflectionY()
mirrorReflectionX()
inversion()
grey()


# print(imageData)



