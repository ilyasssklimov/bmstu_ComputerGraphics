from lab_04.algorithms_circle import add_symmetric_coors
from math import sqrt, sin, cos
from tkinter import messagebox as mb


def get_data_spectrum_ellipse(data):
    data_checked = get_data_ellipse(data[:-2])
    if not data_checked:
        return None
    try:
        n = int(data[-2])
        if n <= 0:
            raise ValueError
        if data_checked[2] >= data_checked[3]:
            raise ArithmeticError
    except ValueError:
        mb.showerror('Ошибка', 'Количество шагов должно быть положительным целым числом')
        return None
    except ArithmeticError:
        mb.showerror('Ошибка', 'Начальное значение полуоси должно быть меньше конечного')
        return None

    try:
        t = abs(float(data[-1]))
        if t == 0:
            raise ValueError
    except ValueError:
        mb.showerror('Ошибка', 'Неизменяемая полуось эллипса должна быть ненулевым числом')
        return None

    data_checked += (t, n)
    return data_checked


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
        a = abs(float(data[2]))
        if a == 0:
            raise ValueError
    except ValueError:
        return not mb.showerror('Ошибка', 'Первая полуось эллипса должна быть ненулевым числом')
    try:
        b = abs(float(data[3]))
        if b == 0:
            raise ValueError
    except ValueError:
        return not mb.showerror('Ошибка', 'Вторая полуось эллипса должна быть ненулевым числом')

    return x, y, a, b


def int_n(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def canonical_ellipse(x0, y0, a, b):
    values = []
    aq, bq = a ** 2, b ** 2
    s = sqrt(aq + bq)
    limit = int_n(aq / s)
    m = b / a
    # i = 0
    for x in range(limit):
        # i += 1
        y = int_n(sqrt(aq - x ** 2) * m)
        values.extend(add_symmetric_coors(x0, y0, x, y))

    limit = int_n(bq / s)
    m = 1 / m

    for y in range(limit + 1):
        # i += 1
        x = int_n(sqrt(bq - y ** 2) * m)
        values.extend(add_symmetric_coors(x0, y0, x, y))
    # print(f'canon {i}, {len(values)}')
    return values


def parametric_ellipse(x0, y0, a, b):
    values = []
    angle = 0
    x, y = a, 0
    yk = int_n(b ** 2 / sqrt(a ** 2 + b ** 2))  # точка перегиба
    step = 1 / b
    # i = 0
    while y <= yk:
        # i += 1
        x = int_n(a * cos(angle))
        y = int_n(b * sin(angle))

        values.extend(add_symmetric_coors(x0, y0, x, y))
        angle += step

    step = 1 / a
    while x > 0:
        # i += 1
        x = int_n(a * cos(angle))
        y = int_n(b * sin(angle))

        values.extend(add_symmetric_coors(x0, y0, x, y))
        angle += step

    # print(f'param {i}, {len(values)}')
    return values


def horizontal_step(x, d, bq):
    x += 1
    d += bq * (2 * x + 1)
    return x, d


def diagonal_step(x, y, d, aq, bq):
    x += 1
    y -= 1
    d += bq * (2 * x + 1) + aq * (1 - 2 * y)
    return x, y, d


def vertical_step(y, d, aq):
    y -= 1
    d += aq * (1 - 2 * y)
    return y, d


def bresenham_ellipse(x0, y0, a, b):
    values = []
    x, y, = 0, b
    aq, bq = a ** 2, b ** 2
    d = aq + bq - 2 * aq * y

    # i = 0
    while y >= 0:
        # i += 1
        values.extend(add_symmetric_coors(x0, y0, x, y))

        if d < 0:
            d1 = 2 * d + 2 * aq * y - aq
            if d1 > 0:
                x, y, d = diagonal_step(x, y, d, aq, bq)
            else:
                x, d = horizontal_step(x, d, bq)
        elif d == 0:
            x, y, d = diagonal_step(x, y, d, aq, bq)
        else:
            d2 = 2 * d - 2 * bq * x - bq
            if d2 < 0:
                x, y, d = diagonal_step(x, y, d, aq, bq)
            else:
                y, d = vertical_step(y, d, aq)
    # print(f'bres {i}, {len(values)}')
    return values


def midpoint_ellipse(x0, y0, a, b):
    values = []
    aq, bq = a ** 2, b ** 2
    limit = int_n(aq / sqrt(aq + bq))
    x, y = 0, b
    df = 0
    f = bq - aq * y + 0.25 * aq + 0.5
    delta = -2 * a ** 2 * y

    for x in range(limit + 1):
        values.extend(add_symmetric_coors(x0, y0, x, y))
        if f >= 0:
            y -= 1
            delta += 2 * aq
            f += delta
        df += 2 * bq
        f += df + bq

    delta = 2 * bq * x
    f += -bq * (x + 0.75) - aq * (y - 0.75)
    df = -2 * aq * y

    while y >= 0:
        values.extend(add_symmetric_coors(x0, y0, x, y))
        if f < 0:
            x += 1
            delta += 2 * bq
            f += delta

        df += 2 * aq
        f += df + aq
        y -= 1

    return values
