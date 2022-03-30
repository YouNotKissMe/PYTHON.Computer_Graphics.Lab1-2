from math import fabs \
    # sin, radians, acos, sqrt, cos, pi, degrees
from PIL import Image
import matplotlib.pyplot as plt


# --------------------------1 лабораторная работа


def length(array):
    # выбор длины
    if fabs(array[2] - array[0]) >= fabs(array[3] - array[1]):
        return fabs(array[2] - array[0])
    else:
        return fabs(array[3] - array[1])


def sign(integer):
    if integer == 0:
        return 0
    elif integer > 0:
        return 1
    else:
        return -1


def DDA(array):
    # Цифровой дифференциальный анализатор
    graph = []
    deltaX = (array[2] - array[0]) / length(array)
    deltaY = (array[3] - array[1]) / length(array)
    X = array[0] + 0.5 * sign(deltaX)
    Y = array[1] + 0.5 * sign(deltaY)
    for i in range(int(length(array))):
        graph.append([int(X), int(Y)])
        X += deltaX
        Y += deltaY
    return graph


def brez(array):
    # общий алгоритм Брезенхема
    x, y = array[0], array[1]
    dx = fabs(array[2] - array[0])
    dy = fabs(array[3] - array[1])
    s2, s1 = sign(array[3] - array[1]), sign(array[2] - array[0])
    trade = None
    if dy > dx:
        dx, dy = dy, dx
        trade = 1
    line = []
    e = 2 * dy - dx
    for i in range(int(dx)):
        line.append([x, y])
        while e > 0:
            if trade == 1:
                x += s1
            else:
                y += s2
            e -= 2 * dx
        if trade == 1:
            y += s2
        else:
            x += s1
        e += 2 * dy
    return line


def MAX(array):
    max = None
    for i in array:
        if not max:
            max = fabs(i)
        else:
            if fabs(i) > max:
                max = fabs(i)
    return int(max)


def coordinate_axis(x, y, size):
    # полностью переназначит закраску пикселей
    if y > 0:
        y = size - y
    else:
        y = size + fabs(y)
    if x > 0:
        x += size
    else:
        x = size - fabs(x)
    return int(x), int(y)


def vector(algoritm):
    x, y = [i[0] for i in algoritm], \
           [i[1] for i in algoritm]
    return x, y


def paint(array):
    # общая функция для алгоритмов + вывод рисунка
    arratCDA, arrayBrez = DDA(array), \
                          brez(array)
    img = Image.new('RGB', ((2 * MAX(array)) + 1,
                            (2 * MAX(array)) + 1),
                    (0, 0, 0))
    for i in range(len(arratCDA)):
        img.putpixel((coordinate_axis(arratCDA[i][0],
                                      arratCDA[i][1],
                                      MAX(array))),
                     (255, 255, 255))
    for i in range(len(arrayBrez)):
        img.putpixel((coordinate_axis(arrayBrez[i][0],
                                      arrayBrez[i][1],
                                      MAX(array))),
                     (255, 0, 0))
    plt.plot(vector(arratCDA)[0],
             vector(arratCDA)[1],
             vector(arrayBrez)[0],
             vector(arrayBrez)[1])
    plt.show()
    return img.show()


# ----------------------------------------2 лабораторная работа
def interface(*array):
    array = [int(i) for i in array[0].split()]
    print(array)
    if array[-1] == 1:
        img = Image.new('RGB', (2 * MAX(array[:-1]) + 1, 2 * MAX(array[:-1]) + 1), (256, 256, 256))
        for i in array[:-1]:
            brez_for_circle(r=i, img=img, number_task=array[-1])
        return img.show()
    elif array[-1] == 2:
        array = [array[i:i + 6] for i in range(0, len(array[0:-1]), 6)]
        print(array)
        maxs, y = picture_size(array)
        img = Image.new('RGB', (2 * (maxs + y) + 1, 2 * (maxs + y) + 1), (256, 256, 256))
        for i in array:
            brez_for_circle(r=i[2], img=img, number_task=2, x=i[0], y=i[1], rgb=tuple(i[3:]))
        return img.show()
    # else:
    #     array = [array[i:i + 8] for i in range(0, len(array[0:-1]), 8)]
    #     maxs, y = picture_size(array)
    #     img = Image.new('RGB', (2 * (maxs + y) + 1, 2 * (maxs + y) + 1), (256, 256, 256))
    #     for i in array:
    #         angle_in_degrees(i, img=img)
    #     return img.show()


def brez_for_circle(r, img, number_task, x=0, y=0, rgb=(255, 0, 0)):
    x1, y1 = x, y
    x, y = 0, r
    d = 2 * (1 - y)
    pixel(img, number_task, x, y, x1, y1, rgb)
    while (y >= x):
        pixel(img, number_task, x, y, x1, y1, rgb)
        x += 1
        if (d > 0):
            y -= 1
            d += 2 * (x - y) + 1

        else:
            d += 2 * x + 1


def pixel(img, number_task, x, y, x1=0, y1=0, rgb=(255, 0, 0)):
    if number_task == 1 or number_task == 2:
        img.putpixel(coordinate_axis(x1 + x, y1 - y, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 + x, y1 + y, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 - x, y1 + y, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 - x, y1 - y, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 + y, y1 - x, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 + y, y1 + x, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 - y, y1 + x, (img.size[0] / 2)), rgb)
        img.putpixel(coordinate_axis(x1 - y, y1 - x, (img.size[0] / 2)), rgb)


def picture_size(array: [int]):
    maxs, y = None, None
    for i in array:
        if maxs:
            if maxs < i[2]:
                maxs = i[2]
        else:
            maxs = i[2]
    for i in array:
        if y:
            if y < MAX(i[0:2]):
                y = MAX(i[0:2])
        else:
            y = MAX(i[0:2])
    return maxs, y


# def angle_in_degrees(array: [int], img):
#     grad = refactor(*array[0:2])
#     pass
#
#
# def refactor(bx, by):
#     x0, y0 = bx, 0
#     mb = sqrt(bx ** 2 + by ** 2)
#     res = (x0 * bx + y0 * by) / (x0 ** 2 * mb)
#     return degrees(cos(res)) * pi / 2


if __name__ == '__main__':
    # ОБЩЕЕ МЕНЮ
    a = int(input('Введите номер лабораторной работы(1 или 2 ):'))
    while int(a):
        if a == 1:
            paint([int(i) for i in input('Введите координаты точек: ').split()])
        elif a == 2:
            try:
                b = int(input('введите задание ко 2 лабораторной работе: \n'
                              '1 - введите R для отображения окружности расположенной в точке (0,0)\n'
                              '2 - ввдите координаты окружности, её радиус и цвет(цвет в формате rgb 0 0 0): \n'
                              '3 - (являяется 4 лабораторной работой) построение четвертинок окружности:\n'
                              ))
                if b in [1, 2]:
                    if b == 1:
                        interface(input('вы можете задать более 1 радиуса для '
                                        'отображения нескольких окружностей: ') + f' {b}')
                    elif b == 2:
                        interface(input('вы можете задать более 1 окружности: ') + f' {b}')
                    # elif b == 3:
                    #     interface(input('введите координаты радиус цвет и угол в градусах:') + f' {b}')
                    else:
                        print('Вы ввели число которое не принадлежит номеру лабораторной работы')
            except ValueError:
                print('Вы ввели не числа')
        a = int(input('Введите номер лабораторной работы(1 или 2 ):'))
