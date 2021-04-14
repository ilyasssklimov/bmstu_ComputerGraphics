from tkinter import messagebox
import math


def int_n(num):
    # num = int(num + (0.5 if num > 0 else -0.5))
    return int(num)


def sin_angle(angle):
    to_radians = math.radians(angle)
    return math.sin(to_radians)


def cos_angle(angle):
    to_radians = math.radians(angle)
    return math.cos(to_radians)


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def get_coordinates(coordinates):
    try:
        x1 = float(coordinates[0])
    except ValueError:
        return not messagebox.showerror('Ошибка', 'X начала отрезка должен быть числом')
    try:
        y1 = float(coordinates[1])
    except ValueError:
        return not messagebox.showerror('Ошибка', 'Y начала отрезка должен быть числом')
    try:
        x2 = float(coordinates[2])
    except ValueError:
        return not messagebox.showerror('Ошибка', 'X конца отрезка должен быть числом')
    try:
        y2 = float(coordinates[3])
    except ValueError:
        return not messagebox.showerror('Ошибка', 'Y конца отрезка должен быть числом')

    return x1, y1, x2, y2


def get_intensity(canvas, color, cur):
    r1, g1, b1 = canvas.winfo_rgb(color)
    r2, g2, b2 = canvas.winfo_rgb('white')
    new_r = int(r1 + ((r2 - r1) * (1 - cur)))
    new_g = int(g1 + ((g2 - g1) * (1 - cur)))
    new_b = int(b1 + ((b2 - b1) * (1 - cur)))

    new_color = "#%4.4x%4.4x%4.4x" % (new_r, new_g, new_b)
    return new_color


def dda(coors):
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]

    values = []
    abs_dx = int(abs(x2 - x1))
    abs_dy = int(abs(y2 - y1))
    if abs_dx > abs_dy:
        L = abs_dx
    else:
        L = abs_dy

    x, y = x1, y1
    dx, dy = (x2 - x1) / L, (y2 - y1) / L

    for _ in range(L):
        values.append((int_n(x), int_n(y)))
        x += dx
        y += dy

    return values


def bresenham_float(coors):
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]

    values = []
    dx, dy = x2 - x1, y2 - y1
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if dx > dy:
        exchange = 0
    else:
        dx, dy = dy, dx
        exchange = 1

    m = dy / dx
    e = m - 0.5
    x, y = int_n(x1), int_n(y1)

    for _ in range(int(dx)):
        values.append((x, y))

        if e >= 0:
            if exchange == 1:
                x += sx
            else:
                y += sy
            e -= 1
        if e < 0:
            if exchange == 1:
                y += sy
            else:
                x += sx
        e += m

    return values


def bresenham_int(coors):
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]

    values = []
    dx, dy = x2 - x1, y2 - y1
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)
    # m = dy / dx

    if dx > dy:
        exchange = 0
    else:
        dx, dy = dy, dx
        exchange = 1

    e = dy + dy - dx
    x, y = int_n(x1), int_n(y1)

    for _ in range(int(dx)):
        values.append((x, y))
        if e >= 0:
            if exchange == 1:
                x += sx
            else:
                y += sy
            e -= (dx + dx)
        if e < 0:
            if exchange == 1:
                y += sy
            else:
                x += sx
        e += (dy + dy)

    return values


def bresenham_smooth(coors, intensity):
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        return [(x1, y1, intensity)]

    values = []
    dx, dy = x2 - x1, y2 - y1
    sx, sy = sign(dx), sign(dy)
    dx, dy = abs(dx), abs(dy)

    if dx > dy:
        exchange = 0
    else:
        dx, dy = dy, dx
        exchange = 1
    m = dy / dx
    e = intensity / 2
    x, y = int_n(x1), int_n(y1)
    m *= intensity
    w = intensity - m

    values.append((x, y, e / intensity))

    for _ in range(1, int(dx)):
        if e < w:
            if exchange == 0:
                x += sx
            else:
                y += sy
            e += m
        elif e > w:
            x += sx
            y += sy
            e -= w

        values.append((x, y, e / intensity))

    return values


def wu(coors):
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        return [(x1, y1, 255)]

    values = []
    dx, dy = x2 - x1, y2 - y1
    # sx, sy = sign(dx), sign(dy)
    sx = 1 if dx == 0 else sign(dx)
    sy = 1 if dy == 0 else sign(dy)
    dx, dy = abs(dx), abs(dy)

    if dx > dy:
        exchange = 0
    else:
        dx, dy = dy, dx
        exchange = 1
    m = dy / dx
    e = -1
    x, y = int_n(x1), int_n(y1)

    # e = intensity / 2
    # m *= intensity
    # w = intensity - m

    for _ in range(int(dx)):
        values.append((x, y, -e))
        if exchange == 0:
            values.append((x, y + sy, 1 - (-e)))
        else:
            values.append((x + sx, y, 1 - (-e)))
        e += m
        if e >= 0:
            if exchange == 1:
                x += sx
            else:
                y += sy
            e -= 1

        if exchange == 0:
            x += sx
        else:
            y += sy

    return values
