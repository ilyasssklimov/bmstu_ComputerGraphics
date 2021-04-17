import tkinter.messagebox as mb
from math import sqrt, sin, cos, pi
import numpy as np


def int_n(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def get_data_spectrum_circle(data):
    data_checked = get_data_circle(data[:-2])
    if not data_checked:
        return None
    try:
        n = int(data[-1])
        if n <= 0:
            raise ValueError
    except ValueError:
        mb.showerror('Ошибка', 'Количество шагов должно быть положительным целым числом')
        return None

    try:
        r2 = float(data[-2])
        if r2 <= 0:
            raise ValueError
        if data_checked[2] >= r2:
            raise ArithmeticError
    except ValueError:
        mb.showerror('Ошибка', 'Радиус окружности должен быть неотрицательным числом')
        return None
    except ArithmeticError:
        mb.showerror('Ошибка', 'Начальный радиус должен быть меньше конечного')
        return None

    return *data_checked, r2, n


def get_data_circle(data):
    try:
        x = float(data[0])
    except ValueError:
        return not mb.showerror('Ошибка', 'Координата X центра окружности должна быть числом')
    try:
        y = float(data[1])
    except ValueError:
        return not mb.showerror('Ошибка', 'Координата Y центра окружности должна быть числом')
    try:
        r = float(data[2])
        if r < 0:
            raise ValueError
    except ValueError:
        return not mb.showerror('Ошибка', 'Радиус окружности должен быть неотрицательным числом')

    return x, y, r


def get_y_canon_circle(x0, y0, x, r):
    tmp = sqrt(r ** 2 - (x - x0) ** 2)
    return [int_n(-x + x0 * 2), int_n(-tmp + y0)], [int_n(x), int_n(-tmp + y0)],\
           [int_n(x), int_n(tmp + y0)], [int_n(-x + x0 * 2), int_n(tmp + y0)]


def get_x_param_circle(x0, r, t):
    return int_n(x0 + r * cos(t))


def get_y_param_circle(y0, r, t):
    return int_n(y0 + r * sin(t))


def canonical_circle(x0, y0, r):
    values = []
    limit = int_n(r / sqrt(2))

    for x in range(limit + 1):
        y = int_n(sqrt(r ** 2 - x ** 2))
        values.extend(add_symmetric_coors(x0, y0, x, y))
        values.extend(add_symmetric_coors(x0, y0, y, x))

    return values


'''
        public static void DrawCircle(Bitmap b, Point center, int radius, Color color)
        {
            int x = 0, y;
            int rr = radius * radius;
            double halfR = radius / Math.Sqrt(2); 

            for (x = 0; x <= halfR; x++)
            {
                y = Convert.ToInt32(Math.Sqrt(rr - x * x));

                DrawHack.DrawSymmetric(b, center, x, y, color);
                DrawHack.DrawSymmetric(b, center, y, x, color);
            }
        }
'''


def parametric_circle(x0, y0, r):
    values = []
    for t in np.arange(0, 2 * pi, 1 / r):

        values.extend([get_x_param_circle(x0, r, t), get_y_param_circle(y0, r, t)])
    return values


def horizontal_step(x, d):
    x += 1
    d += 2 * x + 1
    return x, d


def diagonal_step(x, y, d):
    x += 1
    y -= 1
    d += 2 * (x - y + 1)
    return x, y, d


def vertical_step(y, d):
    y -= 1
    d += 1 - 2 * y
    return y, d


def add_symmetric_coors(x0, y0, x, y):
    return [x0 + x, y0 + y, x0 - x, y0 - y, x0 + x, y0 - y, x0 - x, y0 + y]


def bresenham_circle(x0, y0, r):
    x, y = 0, r
    d = 2 * (1 - r)  # первоначальная ошибка
    yk = 0
    values = [x, y]

    while y >= yk:
        values.extend(add_symmetric_coors(x0, y0, x, y))
        values.extend(add_symmetric_coors(x0, y0, y, x))

        if d < 0:
            d1 = 2 * d + 2 * y - 1
            if d1 < 0:
                x, d = horizontal_step(x, d)
            else:
                x, y, d = diagonal_step(x, y, d)
        elif d == 0:
            x, y, d = diagonal_step(x, y, d)
        else:
            d2 = 2 * d - 2 * x - 1
            if d2 < 0:
                x, y, d = diagonal_step(x, y, d)
            else:
                y, d = vertical_step(y, d)

    return values


def midpoint_circle(x0, y0, r):
    x, y = 0, r
    p = 1 - r
    values = []

    values.extend(add_symmetric_coors(x0, y0, x, y))
    values.extend(add_symmetric_coors(x0, y0, y, x))

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        values.extend(add_symmetric_coors(x0, y0, x, y))
        values.extend(add_symmetric_coors(x0, y0, y, x))

    return values
