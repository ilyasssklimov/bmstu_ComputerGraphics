# Алгоритм с перегородкой

import config as cfg
import time
from tkinter import messagebox as mb


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

    start = time.time()
    partition = find_partition(canvas.edges)

    for edge in canvas.edges:
        x1, y1 = edge[0].x, edge[0].y
        x2, y2 = edge[1].x, edge[1].y

        if y1 != y2:
            if y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            dx = (x2 - x1) / abs(y2 - y1)
            x_start = x1

            for y_cur in range(y1, y2):
                x_cur = cfg.int_n(x_start)

                if x_cur < partition:
                    while x_cur < partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur += 1
                else:
                    while x_cur >= partition:
                        canvas.inverse_pixel(x_cur, y_cur, canvas.color)
                        x_cur -= 1

                x_start += dx

                if delay:
                    time.sleep(0.05)
                    canvas.update()
    canvas.update()
    finish = time.time() - start
    return finish
