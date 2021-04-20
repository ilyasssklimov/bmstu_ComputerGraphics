import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import time
import pandas as pd


def int_n(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def get_coordinates(coordinates):
    x1 = float(coordinates[0])
    y1 = float(coordinates[1])
    x2 = float(coordinates[2])
    y2 = float(coordinates[3])
    return x1, y1, x2, y2


def dda_steps(coors):
    steps = 0
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        steps += 1
        return steps

    values = []
    abs_dx = abs(x2 - x1)
    abs_dy = abs(y2 - y1)
    L = abs_dx if abs_dx > abs_dy else abs_dy
    # L = max(abs_dx, abs_dy)

    x, y = x1, y1
    previous_x, previous_y = -1, -1
    start = False
    dx, dy = (x2 - x1) / L, (y2 - y1) / L
    for _ in range(int(L)):
        if not start or (int(previous_x) != int(x) and int(previous_y) != int(y)):
            start = True
            previous_x = x
            previous_y = y
            steps += 1
        # values.append((int_n(x), int_n(y)))
        x += dx
        y += dy

    return steps


def bresenham_float_steps(coors):
    steps = 0
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        steps += 1
        return steps

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
    previous_x, previous_y = -1, -1
    start = False
    for _ in range(1, int(dx) + 1):
        if not start or (int(previous_x) != int(x) and int(previous_y) != int(y)):
            start = True
            previous_x = x
            previous_y = y
            steps += 1
        # values.append((x, y))
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

    return steps


def bresenham_int_steps(coors):
    steps = 0
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        steps += 1
        return steps

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
    previous_x, previous_y = -1, -1
    start = False

    for _ in range(1, int(dx) + 1):
        if not start or (int(previous_x) != int(x) and int(previous_y) != int(y)):
            start = True
            previous_x = x
            previous_y = y
            steps += 1
        # values.append((x, y))
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

    return steps


def bresenham_smooth_steps(coors, intensity):
    steps = 0
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        steps += 1
        return steps

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

    # values.append((x, y, e / intensity))
    previous_x, previous_y = x, y
    steps += 1

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

        if int(previous_x) != int(x) and int(previous_y) != int(y):
            previous_x = x
            previous_y = y
            steps += 1

        # values.append((x, y, e / intensity))

    return steps


def wu_steps(coors):
    steps = 0
    x1, y1, x2, y2 = coors[0], coors[1], coors[2], coors[3]
    if x1 == x2 and y1 == y2:
        steps += 1
        return steps

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
    x, y = x1, y1
    previous_x, previous_y = -1, -1
    start = False
    # e = intensity / 2
    # m *= intensity
    # w = intensity - m

    for _ in range(int(dx)):
        if not start or (int(previous_x) != int(x) and int(previous_y) != int(y)):
            previous_x = x
            previous_y = y
            steps += 1
            start = True

        # values.append((int_n(x), int_n(y), -e))
        # if exchange == 0:
        #     values.append((int_n(x), int_n(y + sy), 1 - (-e)))
        # else:
        #     values.append((int_n(x + sx), int_n(y), 1 - (-e)))
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

    return steps


def compare_time(algorithms, length, coeffs):
    matplotlib.use('TkAgg')
    plt.figure(1)
    plt.get_current_fig_manager().set_window_title('Сравнение временных характеристик алгоритмов')
    plt.get_current_fig_manager().toolbar.pack_forget()
    plt.get_current_fig_manager().resize(700, 700)

    names = ['ЦДА', 'Брезенхем\n(с действ.\nданными)', 'Брезенхем\n(с целыми\nданными)',
             'Брезенхем\n(с устранением\nступенчатости)', 'Ву']
    values = []

    angle = 1
    max_angle = 360
    iters = 10
    x1 = 0
    y1 = 0

    for index, algorithm in enumerate(algorithms):
        total = 0
        cur_angle = 0
        while cur_angle < max_angle:
            cur_angle += angle
            cos_angle = math.cos(math.radians(cur_angle))
            sin_angle = math.sin(math.radians(cur_angle))
            x2 = x1 + cos_angle * length
            y2 = y1 + sin_angle * length
            coors = [x1, y1, x2, y2]

            for _ in range(iters):
                if index != 3:
                    start = time.process_time()
                    algorithm(coors)
                    total += time.process_time() - start
                else:
                    start = time.process_time()
                    algorithm(coors, 256)
                    total += time.process_time() - start

        values.append(total / (max_angle / angle * iters) * coeffs[index])

    plt.bar(names, values, align='center')
    plt.ylabel('Время')

    plt.show()


def compare_steps(algorithms, length):
    matplotlib.use('TkAgg')
    plt.figure(2)
    plt.get_current_fig_manager().set_window_title('Зависимость количества ступенек от угла наклона отрезка')
    plt.get_current_fig_manager().toolbar.pack_forget()
    plt.get_current_fig_manager().resize(700, 700)
    names = ['ЦДА', 'Брезенхем\n(с действ.\nданными)', 'Брезенхем\n(с целыми\nданными)',
             'Брезенхем\n(с устранением\nступенчатости)', 'Ву']
    values = []

    angle = 5
    max_angle = 90
    x1 = 0
    y1 = 0

    for index, algorithm in enumerate(algorithms):
        cur_angle = -angle
        cur_values = []
        while cur_angle < max_angle:
            cur_angle += angle
            cos_angle = math.cos(math.radians(cur_angle))
            sin_angle = math.sin(math.radians(cur_angle))
            x2 = x1 + cos_angle * length
            y2 = y1 + sin_angle * length
            coors = [x1, y1, x2, y2]

            if index != 3:
                cur_values.append(algorithm(coors))
            else:
                cur_values.append(algorithm(coors, 256))
        values.append(cur_values)

    data = dict()
    for i in range(5):
        data[names[i]] = values[i]
    df = pd.DataFrame(data)
    angles = np.arange(0, max_angle + 1, angle)
    plt.plot(angles, df)
    plt.legend(data, loc=2)
    plt.show()
