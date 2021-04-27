from algorithms_circle import add_symmetric_coors
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


def canonical_ellipse(x0, y0, a, b, draw=True):
    values = []
    a, b = int_n(a), int_n(b)
    aq, bq = a ** 2, b ** 2
    s = sqrt(aq + bq)
    limit = int_n(aq / s)
    m = b / a

    for x in range(limit + 1):
        y = int_n(sqrt(aq - x ** 2) * m)
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))

    limit = int_n(bq / s)
    m = 1 / m

    for y in range(limit + 1):
        x = int_n(sqrt(bq - y ** 2) * m)
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))

    return values


def parametric_ellipse(x0, y0, a, b, draw=True):
    values = []
    angle = 0
    x, y = a, 0
    yk = int_n(b ** 2 / sqrt(a ** 2 + b ** 2))
    step = 1 / b

    while y < yk:
        x = int_n(a * cos(angle))
        y = int_n(b * sin(angle))
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
        angle += step

    step = 1 / a
    while x > 0:
        x = int_n(a * cos(angle))
        y = int_n(b * sin(angle))

        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
        angle += step

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


def bresenham_ellipse(x0, y0, a, b, draw=True):
    values = []
    # a, b = int_n(a), int_n(b)
    x, y, = 0, b
    aq, bq = a ** 2, b ** 2
    aq2, bq2 = aq + aq, bq + bq
    d = aq + bq - aq2 * y

    while y >= 0:
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))

        if d < 0:
            d1 = 2 * d + aq2 * y - aq
            if d1 > 0:
                x, y, d = diagonal_step(x, y, d, aq, bq)
            else:
                x, d = horizontal_step(x, d, bq)
        elif d == 0:
            x, y, d = diagonal_step(x, y, d, aq, bq)
        else:
            d2 = 2 * d - bq2 * x - bq
            if d2 < 0:
                x, y, d = diagonal_step(x, y, d, aq, bq)
            else:
                y, d = vertical_step(y, d, aq)

    return values


def midpoint_ellipse(x0, y0, a, b, draw=True):
    values = []
    aq, bq = a ** 2, b ** 2
    aq2, bq2 = aq + aq, bq + bq

    limit = int_n(aq / sqrt(aq + bq))
    x, y = 0, b
    df = 0
    f = bq - aq * y + 0.25 * aq + 0.5
    delta = -2 * aq * y

    for x in range(limit + 1):
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
        if f >= 0:
            y -= 1
            delta += aq2
            f += delta
        df += bq2
        f += df + bq

    delta = bq2 * x
    f += -bq * (x + 0.75) - aq * (y - 0.75)
    df = -aq2 * y

    while y >= 0:
        if draw:
            values.extend(add_symmetric_coors(x0, y0, x, y))
        if f < 0:
            x += 1
            delta += bq2
            f += delta

        df += aq2
        f += df + aq
        y -= 1

    return values
