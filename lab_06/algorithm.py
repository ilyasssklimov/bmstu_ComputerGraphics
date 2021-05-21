# Алгоритм потрочного заполнения с затравкой

import config as cfg
import time
from tkinter import messagebox as mb


def affiliation(point, edges):
    flag = False
    x, y = point.x, point.y

    for edge in edges:
        dx, dy = edge[1].x - edge[0].x, edge[1].y - edge[0].y
        if (edge[0].y < y < edge[1].y or edge[1].y < y < edge[0].y) and (
                dy != 0 and x > (dx * (y - edge[0].y) / dy + edge[0].x)):
            flag = not flag

    return flag


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


def algorithm_seed(canvas, seed_point, delay=False):
    if not canvas.edges:
        return mb.showerror('Ошибка!', 'Невозможно выполнить действие, так как отсутствует область для закрашивания')

    if not canvas.seed and not seed_point:
        return mb.showerror('Ошибка!', 'Невозможно выполнить действие, так как отсутствует затравочный пиксель')
    else:
        if canvas.seed:
            x, y = canvas.seed.x, canvas.seed.y
        else:
            seed = list(map(int, seed_point.split()))
            x, y = seed[0], seed[1]

        if not affiliation(cfg.Point(x, y), canvas.edges):
            return mb.showerror('Ошибка!', 'Невозможно выполнить действие, так как затравочный пиксель находится '
                                           'вне области для закрашивания')
    start = time.time()
    if canvas.seed:
        seed_stack = [f'{canvas.seed.x} {canvas.seed.y}']
        canvas.delete('seed')
        canvas.seed = cfg.Point(exist=False)
    else:
        seed_stack = [seed_point]
    
    while seed_stack:
        cur_seed = seed_stack.pop()
        cur_seed = list(map(int, cur_seed.split()))
        canvas.set_pixel(cfg.Point(int(cur_seed[0]), int(cur_seed[1]), canvas.color))

        x_seed = cur_seed[0]
        x = x_seed + 1
        y = cur_seed[1]

        while get_color(canvas, x, y) == cfg.WHITE_COLOR:
            canvas.set_pixel(cfg.Point(x, y, canvas.color))
            x += 1
        # canvas.update()

        xr = x - 1

        x = x_seed - 1
        while get_color(canvas, x, y) == cfg.WHITE_COLOR:
            canvas.set_pixel(cfg.Point(x, y, canvas.color))
            x -= 1
        # canvas.update()

        xl = x + 1

        x, y = xl, cur_seed[1] + 1
        while x <= xr:
            flag = 0
            while get_color(canvas, x, y) == cfg.WHITE_COLOR and x <= xr:
                if not flag:
                    flag = 1
                x += 1
            if flag:
                if x == xr and get_color(canvas, x, y) == cfg.WHITE_COLOR:
                    seed_stack.append(f'{x} {y}')
                else:
                    seed_stack.append(f'{x - 1} {y}')
                # flag = 0

            x_in = x
            while get_color(canvas, x, y) != cfg.WHITE_COLOR and x <= xr:
                x += 1

            if x == x_in:
                x += 1

        x, y = xl, cur_seed[1] - 1
        while x <= xr:
            flag = 0
            while get_color(canvas, x, y) == cfg.WHITE_COLOR and x <= xr:
                if not flag:
                    flag = 1
                x += 1
            if flag:
                if x == xr and get_color(canvas, x, y) == cfg.WHITE_COLOR:
                    seed_stack.append(f'{x} {y}')
                else:
                    seed_stack.append(f'{x - 1} {y}')
                # flag = 0

            x_in = x
            while get_color(canvas, x, y) != cfg.WHITE_COLOR and x <= xr:
                x += 1

            if x == x_in:
                x += 1

        if delay:
            canvas.update()

    finish = time.time() - start
    print(finish)
    return finish
