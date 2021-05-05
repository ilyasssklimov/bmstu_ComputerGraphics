# Алгоритм с перегородкой

import config as cfg
import time


def bresenham_int(canvas, start, finish):
    x1, y1, x2, y2 = start.x, start.y, finish.x, finish.y
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]

    # values = []
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
        # values.append((x, y))
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
    print(min_x, find_x_max(edges))
    print((find_x_max(edges) - min_x) / 2)
    return (find_x_max(edges) - min_x) / 2 + min_x


def algorithm_partition(canvas, delay=False):
    start = time.time()
    x_max = cfg.int_n(find_x_max(canvas.edges))
    partition = find_partition(canvas.edges)

    for edge in canvas.edges:
        print(edge[0].x, edge[1].x)
        x1, y1 = edge[0].x, edge[0].y
        x2, y2 = edge[1].x, edge[1].y

        if y1 != y2:
            if y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            # y_cur, y_end = y1, y2
            dx = (x2 - x1) / abs(y2 - y1)
            # dy = (y2 - y1) / abs(x2 - x1)

            print(f'dx = {dx}')
            x_start = x1

            for y_cur in range(y1, y2):
                x_cur = x_start
                canvas.update()
                if x_cur <= partition:
                    while x_cur <= partition:
                        canvas.inverse_pixel(cfg.int_n(x_cur), cfg.int_n(y_cur), canvas.color)
                        x_cur += 1
                else:
                    while x_cur >= partition:
                        canvas.inverse_pixel(cfg.int_n(x_cur), cfg.int_n(y_cur), canvas.color)
                        x_cur -= 1

                x_start += dx

        bresenham_int(canvas, edge[0], edge[1])

    finish = time.time() - start
    print(f'Время = {finish}')
