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

    print(np.dot([2, 3], [2, 3]))

    tmpImageData = imageData

    # for i in tmpImageData:
    #     for j in i:
    #         # print(j[0])
    #         j[0] *= 0.75
    #         j[1] *= 0.75
    #         j[2] *= 0.75
    # Image.fromarray(tmpImageData).save('grey.png')

    imageData[...] = imageData[...] * (1 - 0.25)
    Image.fromarray(imageData).save('grey.png')




    # tmpImageData = np.dot(imageData[..., :3], [0.2989, 0.5870, 0.1140])
    # Image.fromarray(tmpImageData).save('greyImage.png')


rotateImageRight(2)
mirrorReflectionY()
mirrorReflectionX()
inversion()
grey()


# print(imageData)



