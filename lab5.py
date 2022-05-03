from main import coordinate_axis, DDA, brez_for_circle
from PIL import Image


def figure(array: [int]):
    '''
    функция отвечает за постороения картинки закращенной фигуры
    Параметры:
        array []: список целых значений
    Возвращаемое значение:
        img.show : выводить картинку с закращенной фигурой
    '''
    img = Image.new('RGB', ((2 * max(array)) + 1,
                            (2 * max(array)) + 1),
                    (0, 0, 0))
    size = max(array)
    array = [array[i:i + 4] for i in range(0, len(array), 4)]
    for i in array:
        arrayDDA = DDA(i)

        for i in range(len(arrayDDA)):
            img.putpixel((coordinate_axis(arrayDDA[i][0],
                                          arrayDDA[i][1],
                                          size)),
                         (255, 255, 255))
    color(img, size)
    print(img.getpixel((0, 0)))
    return img.show()


def kawaii(ss):
    img = Image.new('RGB', ((2 * ss) + 1, 2 * (ss + 1)), (0, 0, 0))
    brez_for_circle(ss, img, 1)
    color(img, ss)
    return img.show()





def color(img, size):
    '''
    Фунция закрашивает полую фигуру
        Параметры:
         img: картинка для закраски пикселей

    :param size:
    :return:
    '''
    stek = [[size / 2, size / 2]]
    while stek:
        xy = tuple(stek[-1])
        stek.pop()
        if img.getpixel(tuple(coordinate_axis(xy[0], xy[1], size))) == (0, 0, 0):
            img.putpixel((coordinate_axis(xy[0], xy[1], size)), (255, 255, 255))
        if img.getpixel(tuple(coordinate_axis(xy[0] + 1, xy[1], size))) == (0, 0, 0):
            stek.append([xy[0] + 1, xy[1]])
        if img.getpixel(tuple(coordinate_axis(xy[0] - 1, xy[1], size))) == (0, 0, 0):
            stek.append([xy[0] - 1, xy[1]])
        if img.getpixel(tuple(coordinate_axis(xy[0], xy[1] - 1, size))) == (0, 0, 0):
            stek.append([xy[0], xy[1] - 1])
        if img.getpixel(tuple(coordinate_axis(xy[0], xy[1] + 1, size))) == (0, 0, 0):
            stek.append([xy[0], xy[1] + 1])


if __name__ == '__main__':
    ''' программа основана на прямых из 1 лабораторной работы 
        для примера
        для посттроения квадрата находящегося в начале координат нужно: 
            первая прямая (0,0)(50,0)
            вторая прямая (50,0)(50,50)
            третья прямая (0,0)(0,50)
            четертая прямая (50,50)(0,50)
        в программе задавать координаты в ввиде: 0 0 50 0 50 0 50 50 0 0 0 50 50 50 0 50    
    '''
    a = int(input('''введите число:
                    1-задать координаты многоугольника и закрасить его
                    2-задать радиус окружности находящейся в начале координат и закрасить его: '''))
    while int(a):
        if a == 1:
            figure([int(i) for i in input('введите координаты многоугольника: ').split()])
        elif a == 2:
            'введите радиус окружности'
        a = int(input('Введите номер лабораторной работы(1 или 2 ):'))
