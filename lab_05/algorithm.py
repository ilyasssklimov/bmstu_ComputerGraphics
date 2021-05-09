# Алгоритм с перегородкой

import config as cfg
import math
import time
from tkinter import messagebox as mb


def bresenham_int(canvas, start, finish):
    x1, y1, x2, y2 = start.x, start.y, finish.x, finish.y
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]
    canvas.create_line(start.x, start.y, finish.x, finish.y, fill=start.color)


def abresenham_int(canvas, start, finish):
    x1, y1, x2, y2 = start.x, start.y, finish.x, finish.y

    abs_dx = abs(x2 - x1)
    abs_dy = abs(y2 - y1)
    if abs_dx > abs_dy:
        L = abs_dx
    else:
        L = abs_dy

    x, y = x1, y1
    dx, dy = (x2 - x1) / L, (y2 - y1) / L

    color = start.color
    for _ in range(L):
        canvas.set_pixel(cfg.Point(round(x), round(y), color))
        x += dx
        y += dy

    # return values


def abresenham_int(canvas, start, finish):
    x1, y1, x2, y2 = start.x, start.y, finish.x, finish.y
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]

    dx, dy = x2 - x1, y2 - y1
    sx, sy = cfg.sign(dx), cfg.sign(dy)
    dx, dy = abs(dx), abs(dy)
    # m = dy / dx

    if dx > dy:
        exchange = 0
    else:
        dx, dy = dy, dx
        exchange = 1

    e = dy + dy - dx
    x, y = cfg.int_n(x1), cfg.int_n(y1)
    color = start.color

    for _ in range(int(dx)):
        canvas.set_pixel(cfg.Point(x, y, color))
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


def get_color(canvas, x, y):
    # print(canvas.frame.img.get(canvas.winfo_rootx() + x, canvas.winfo_rooty() + y))
    return canvas.frame.img.get(x, y)


def find_x_max(edges):
    m = None

    for i in range(len(edges)):
        if m is None or edges[i][0].x > m:
            m = edges[i][0].x
        if m is None or edges[i][1].x > m:
            m = edges[i][1].x

    return m


def find_partition(edges):
    min_x = None

    for i in range(len(edges)):
        if min_x is None or edges[i][0].x < min_x:
            min_x = edges[i][0].x
        if min_x is None or edges[i][1].x < min_x:
            min_x = edges[i][1].x

    return (find_x_max(edges) - min_x) / 2 + min_x


def algorithm_partition(canvas, delay=False):
    if not canvas.edges:
        return mb.showerror('Ошибка!', 'Невозможно выполнить действие, так как отсутствует область для закрашивания')
    start = time.time()
    # x_max = cfg.int_n(find_x_max(canvas.edges))
    partition = find_partition(canvas.edges)

    for edge in canvas.edges:
        # print(edge[0].x, edge[1].x)
        x1, y1 = edge[0].x, edge[0].y
        x2, y2 = edge[1].x, edge[1].y

        if y1 != y2:
            if y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            dx = (x2 - x1) / abs(y2 - y1)

            # bresenham_int(canvas, cfg.Point(edge[0].x, edge[0].y, 'white'), edge[1])
            x_start = x1
            print(f'dx = {dx}')
            # print(f'length = {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}')
            for y_cur in range(y1, y2):
                x_cur = cfg.int_n(x_start)
                # canvas.set_pixel(cfg.Point(x_cur, y_cur, canvas.color))
                # x_start += dx
                # continue
                if x_cur < partition:
                    x_cur += 1
                    while x_cur <= partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur += 1
                else:
                    x_cur -= 1
                    while x_cur > partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur -= 1

                x_start += dx

                if delay:
                    time.sleep(0.2)
                canvas.update()

        # bresenham_int(canvas, edge[0], edge[1])

    finish = time.time() - start
    print(f'Время = {finish}')


def fill_pixels(canvas, begin, end, y):
    for x in range(begin, end + 1):
        canvas.inverse_pixel(x, y, canvas.color)


def aalgorithm_partition(canvas, delay=False):
    max_x = find_x_max(canvas.edges)
    for edge in canvas.edges:
        x1, y1 = edge[0].x, edge[0].y
        x2, y2 = edge[1].x, edge[1].y

        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        dx = (x2 - x1) / (y2 - y1)
        x = x1
        for y in range(y1, y2):
            fill_pixels(canvas, cfg.int_n(x), max_x, y)
            x += dx
            canvas.update()
            if delay:
                time.sleep(0.2)


'''
def algorithm_partition(canvas, delay=False):
    start = time.time()
    # x_max = cfg.int_n(find_x_max(canvas.edges))
    partition = find_partition(canvas.edges)

    for edge in canvas.edges:
        # print(edge[0].x, edge[1].x)
        x1, y1 = edge[0].x, edge[0].y
        x2, y2 = edge[1].x, edge[1].y
        coors = bresenham_int(canvas, edge[0], edge[1])
        if y1 != y2:
            if y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            # y_cur, y_end = y1, y2
            dx = (x2 - x1) / (y2 - y1)
            # dy = (y2 - y1) / abs(x2 - x1)

            # print(f'dx = {dx}')
            x_start = x1
            # x_start = coors[0][0]
            # i = 0
            for y_cur in range(y1, y2):
                x_cur = x_start
                canvas.update()
                if x_cur < partition:
                    while x_cur < partition:
                        canvas.inverse_pixel(cfg.int_n(x_cur), cfg.int_n(y_cur), canvas.color)
                        x_cur += 1
                else:
                    while x_cur >= partition:
                        canvas.inverse_pixel(cfg.int_n(x_cur), cfg.int_n(y_cur), canvas.color)
                        x_cur -= 1
                # i += 1
                x_start += dx
        else:
            print('Hello')

        # bresenham_int(canvas, edge[0], edge[1])

    finish = time.time() - start
    print(f'Время = {finish}')
'''
