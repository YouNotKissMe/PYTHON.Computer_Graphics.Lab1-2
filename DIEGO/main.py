import PIL as pl
from math import fabs


def Hilbert_curve():
    """
    Параметры:
    Возвращаемое значение:
    """
    pass


def coordinate_axis(x, y, size):
    '''
    Возвращает такие значения x,y
    при которых построение рисунака будет начинаться с начала координат
        Параметры:
            x (int): координата по оси Ox
            y (int): координата по оси Oy
            size : размер картинки
        Возвращаемое значение:
            x (int): правильная координата по оси Ox
            y (int): правильная координата по оси Oy

    '''
    if y > 0:
        y = size - y
    else:
        y = size + fabs(y)
    if x > 0:
        x += size
    else:
        x = size - fabs(x)
    return int(x), int(y)


def MAX(array):
    '''
    свой метод поиска наибольшего целого значения в массиве наибольшего значения
        Параметры:
            array: массив чисел
        Возвращаемое значение:
            max (int): максимальное целое число в массиве
    '''
    max = None
    for i in array:
        if not max:
            max = fabs(i)
        else:
            if fabs(i) > max:
                max = fabs(i)
    return int(max)


if __name__ == '__main__':
    pass