from lab_04.algorithms_circle import add_symmetric_coors
from math import sqrt, sin, cos
from tkinter import messagebox as mb


def get_data_ellipse(data):
    try:
        x = float(data[0])
    except ValueError:
        return not mb.showerror('Ошибка', 'Координата X центра эллипса должна быть числом')
    try:
        y = float(data[1])
    except ValueError:
        return not mb.showerror('Ошибка', 'Координата Y центра эллипса должна быть числом')
    try:
        a = float(data[2])
    except ValueError:
        return not mb.showerror('Ошибка', 'Первая полуось эллипса должна быть числом')
    try:
        b = float(data[3])
    except ValueError:
        return not mb.showerror('Ошибка', 'Вторая полуось эллипса должна быть числом')

    return x, y, a, b


def int_n(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def canonical_ellipse(x0, y0, a, b):
    values = []
    s = sqrt(a ** 2 + b ** 2)
    limit = int_n(a ** 2 / s)
    # x, y = 0, 0
    m = b / a

    for x in range(limit + 1):
        y = int_n(sqrt(a ** 2 - x ** 2) * m)
        values.extend(add_symmetric_coors(x0, y0, x, y))

    limit = int_n(b ** 2 / s)
    m = 1 / m

    for y in range(limit + 1):
        x = int_n(sqrt(b ** 2 - y ** 2) * m)
        values.extend(add_symmetric_coors(x0, y0, x, y))

    return values


def parametric_ellipse(x0, y0, a, b):
    values = []
    angle = 0
    x, y = a, 0
    yk = int_n(b ** 2 / sqrt(a ** 2 + b ** 2))  # точка перегиба
    step = 1 / b

    while y <= yk:
        x = a * cos(angle)
        y = b * sin(angle)

        values.extend(add_symmetric_coors(x0, y0, x, y))
        angle += step

    step = 1 / a
    while x > 0:
        x = a * cos(angle)
        y = b * sin(angle)

        values.extend(add_symmetric_coors(x0, y0, x, y))
        angle += step

    return values


def horizontal_step(x, d, b):
    x += 1
    d += b ** 2 * (2 * x + 1)
    return x, d


def diagonal_step(x, y, d, a, b):
    x += 1
    y -= 1
    d += b ** 2 * (2 * x + 1) + a ** 2 * (1 - 2 * y)
    return x, y, d


def vertical_step(y, d, a):
    y -= 1
    d += a ** 2 * (1 - 2 * y)
    return y, d


def bresenham_ellipse(x0, y0, a, b):
    values = []
    x, y, = 0, b
    d = a ** 2 + b ** 2 - 2 * a ** 2 * y

    while y >= 0:
        values.extend(add_symmetric_coors(x0, y0, x, y))

        if d < 0:
            d1 = 2 * d + 2 * a ** 2 * y - a ** 2
            if d1 > 0:
                x, y, d = diagonal_step(x, y, d, a, b)
            else:
                x, d = horizontal_step(x, d, b)
        elif d == 0:
            x, y, d = diagonal_step(x, y, d, a, b)
        else:
            d2 = 2 * d - 2 * b ** 2 * x - b ** 2
            if d2 < 0:
                x, y, d = diagonal_step(x, y, d, a, b)
            else:
                y, d = vertical_step(y, d, a)

    return values


def midpoint_ellipse(x0, y0, a, b):
    values = []
    limit = int_n(a ** 2 / sqrt(a ** 2 + b ** 2))
    x, y = 0, b
    df = 0
    f = b ** 2 - a ** 2 * y + 0.25 * a ** 2 + 0.5
    delta = -2 * a ** 2 * y

    for x in range(limit + 1):
        values.extend(add_symmetric_coors(x0, y0, x, y))
        if f >= 0:
            y -= 1
            delta += 2 * a ** 2
            f += delta
        df += 2 * b ** 2
        f += df + b ** 2

    delta = 2 * b ** 2 * x
    f += -b ** 2 * (x + 0.75) - a ** 2 * (y - 0.75)
    df = -2 * a ** 2 * y

    while y >= 0:
        values.extend(add_symmetric_coors(x0, y0, x, y))
        if f < 0:
            x += 1
            delta += 2 * b ** 2
            f += delta

        df += 2 * a ** 2
        f += df + a ** 2
        y -= 1

    return values
