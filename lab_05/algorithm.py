# Алгоритм с перегородкой

import config as cfg
import math
import time
from tkinter import messagebox as mb


def bresenham_int(canvas, start, finish):
    x1, y1, x2, y2 = start.x, start.y, finish.x, finish.y

    dx, dy = x2 - x1, y2 - y1
    sx, sy = cfg.sign(dx), cfg.sign(dy)
    dx, dy = abs(dx), abs(dy)

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
    return canvas.frame.img.get(x, y)


def find_partition(edges):
    max_x = None
    min_x = None

    for i in range(len(edges)):
        if max_x is None or edges[i][0].x > max_x:
            max_x = edges[i][0].x
        if max_x is None or edges[i][1].x > max_x:
            max_x = edges[i][1].x

        if min_x is None or edges[i][0].x < min_x:
            min_x = edges[i][0].x
        if min_x is None or edges[i][1].x < min_x:
            min_x = edges[i][1].x

    return (max_x - min_x) / 2 + min_x


def algorithm_partition(canvas, delay=False):
    if not canvas.edges:
        return mb.showerror('Ошибка!', 'Невозможно выполнить действие, так как отсутствует область для закрашивания')
    # canvas.create_image((canvas.width / 2, canvas.height / 2), image=canvas.frame.img, state='normal')
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
            # print(f'first = {x1}, second = {x2}, dx = {dx}')
            # bresenham_int(canvas, cfg.Point(edge[0].x, edge[0].y, 'white'), edge[1])
            x_start = x1
            # print(f'length = {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}')
            for y_cur in range(y1, y2):
                x_cur = cfg.int_n(x_start)
                # canvas.set_pixel(cfg.Point(x_cur, y_cur, canvas.color))
                # x_start += dx
                # continue
                if x_cur < partition:
                    # x_cur += 1
                    while x_cur < partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur += 1
                else:
                    # x_cur -= 1
                    while x_cur >= partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur -= 1

                x_start += dx

                if delay:
                    time.sleep(0.2)
                canvas.update()

        # bresenham_int(canvas, edge[0], edge[1])

    finish = time.time() - start
    return finish
def algorithm_partition(canvas, delay=False):
    if not canvas.edges:
        return mb.showerror('Ошибка!', 'Невозможно выполнить действие, так как отсутствует область для закрашивания')
    # canvas.create_image((canvas.width / 2, canvas.height / 2), image=canvas.frame.img, state='normal')
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
            # print(f'first = {x1}, second = {x2}, dx = {dx}')
            # bresenham_int(canvas, cfg.Point(edge[0].x, edge[0].y, 'white'), edge[1])
            x_start = x1
            # print(f'length = {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}')
            for y_cur in range(y1, y2):
                x_cur = cfg.int_n(x_start)
                # canvas.set_pixel(cfg.Point(x_cur, y_cur, canvas.color))
                # x_start += dx
                # continue
                if x_cur < partition:
                    # x_cur += 1
                    while x_cur < partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur += 1
                else:
                    # x_cur -= 1
                    while x_cur >= partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur -= 1

                x_start += dx

                if delay:
                    time.sleep(0.2)
                    canvas.update()

        # bresenham_int(canvas, edge[0], edge[1])

    finish = time.time() - start
    return finish