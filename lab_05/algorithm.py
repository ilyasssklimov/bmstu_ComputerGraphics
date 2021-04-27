# Алгоритм с перегородкой

import config as cfg
from ctypes import windll
import time


def get_color(x, y):
    dc = windll.user32.GetDC(0)
    rgb = windll.gdi32.GetPixel(dc, int(x), int(y))

    r = rgb & 0xff
    g = (rgb >> 8) & 0xff
    b = (rgb >> 16) & 0xff

    return r, g, b


def find_x_max(edges):
    m = None

    for i in range(len(edges)):
        if m is None or edges[i][0].x > m:
            m = edges[i][0].x
        if m is None or edges[i][1].x > m:
            m = edges[i][1].x

    return m


def algorithm_partition(canvas, delay=False):
    start = time.time()
    x_max = int(find_x_max(canvas.edges))

    for edge in canvas.edges:
        x1, y1 = edge[0].x, edge[0].y
        x2, y2 = edge[1].x, edge[1].y

        if y1 != y2:
            if y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            y_cur, y_end = y1, y2
            dx = (x2 - x1) / abs(y2 - y1)
            x_start = x1
            while y_cur < y_end:
                x_cur = x_start
                while x_cur < x_max:
                    canvas.reverse_pixel(x_cur, y_cur, canvas.color)
                    # canvas.set_pixel(cfg.Point(x_cur, y_cur, canvas.color))
                    x_cur += 1

                x_start += dx
                y_cur += 1

    finish = time.time() - start
    print(f'Время = {finish}')
