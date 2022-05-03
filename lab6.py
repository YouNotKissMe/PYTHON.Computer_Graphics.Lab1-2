from main import coordinate_axis, DDA, MAX
from PIL import Image


def fortest(img):
    arrayY1 = DDA([-200, -200, -200, 200])
    arrayY2 = DDA([200, -200, 200, 200])
    arrayX1 = DDA([-200, 200, 200, 200])
    arrayX2 = DDA([-200, -200, 200, -200])
    # img = Image.new('RGB', (800 + 1, 800 + 1,))
    printFigure(arrayY1, img)
    printFigure(arrayY2, img)
    printFigure(arrayX1, img)
    printFigure(arrayX2, img)
    return img


def figureUser():
    pass


def printFigure(array, img):
    for i in range(len(array)):
        img.putpixel((coordinate_axis(array[i][0],
                                      array[i][1],
                                      400)),
                     (255, 255, 255))
    return img


def printLine(array: [int], img, arrayX1, arrayY1):
    array = DDA(array)
    for i in array:
        if i[0] in range(arrayX1[0], arrayX1[2] + 1) and i[1] in range(arrayY1[1], arrayX1[3]):
            img.putpixel((coordinate_axis(i[0],
                                          i[1],
                                          400)),
                         (255, 255, 255))
        else:
            img.putpixel((coordinate_axis(i[0],
                                          i[1],
                                          400)),
                         (255, 0, 0))


if __name__ == '__main__':
    img = Image.new('RGB', (800 + 1, 800 + 1,))
    fortest(img)
    printLine([0, 0, 400, 400], img, [-200, -200, 200, 200], [0, -200, 0, 200])
    printLine([-400, -400, -250, -250], img, [-200, -200, 200, 200], [0, -200, 0, 200])
    printLine([-400, 0, -125, 0], img, [-200, -200, 200, 200], [0, -200, 0, 200])
    img.show()
