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
        mb.showerror('Ошибка', 'Радиус окружности должен быть положительным числом')
        return None
    except ArithmeticError:
        mb.showerror('Ошибка', 'Начальный радиус должен быть меньше конечного')
        return None

    data_checked += (r2, n)
    return data_checked


def get_data_circle(data):
    try:
        x = float(data[0])
    except ValueError:
        mb.showerror('Ошибка', 'Координата X центра окружности должна быть числом')
        return None
    try:
        y = float(data[1])
    except ValueError:
        mb.showerror('Ошибка', 'Координата Y центра окружности должна быть числом')
        return None
    try:
        r = float(data[2])
        if r <= 0:
            raise ValueError
    except ValueError:
        mb.showerror('Ошибка', 'Радиус окружности должен быть положительным числом')
        return None

    return x, y, r


def canonical_circle(x0, y0, r, draw=True):
    values = []
    limit = int_n(r / sqrt(2))

    for x in range(limit + 1):
        y = int_n(sqrt(r ** 2 - x ** 2))
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
            values.extend(add_symmetric_coors(x0, y0, y, x))

    return values


def parametric_circle(x0, y0, r, draw=True):
    values = []

    step = 1 / r
    for t in np.arange(0, pi / 4 + step, step):
        x = int_n(r * cos(t))
        y = int_n(r * sin(t))
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
            values.extend(add_symmetric_coors(x0, y0, y, x))

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


def bresenham_circle(x0, y0, r, draw=True):
    x, y = 0, r
    d = 2 * (1 - r)  # первоначальная ошибка
    yk = r / sqrt(2)
    values = [x, y]

    while y >= yk:
        if draw:
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


def midpoint_circle(x0, y0, r, draw=True):
    x, y = 0, r
    p = 1 - r
    values = []

    if draw:
        values.extend(add_symmetric_coors(x0, y0, x, y))
        values.extend(add_symmetric_coors(x0, y0, y, x))

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
            values.extend(add_symmetric_coors(x0, y0, y, x))

    return values
