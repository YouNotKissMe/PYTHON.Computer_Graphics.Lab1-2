from main import coordinate_axis
from PIL import Image
from math import sqrt


# обойдемся 1 функией, задание 1 поэтому без фспомогательных


def interface(array: [int]):
    array = [array[i:i + 8] for i in range(0, len(array), 8)]
    return print(array)


if __name__ == '__main__':
    interface([int(i) for i in input('Введите координаты, радиус,\
    начальный и конечный угол, цвет,можете ввести несколько: ').split()])
