from algorithms_circle import get_data_spectrum_circle
from algorithms_ellipse import get_data_spectrum_ellipse
from data import algorithms

import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import time
import pandas as pd
from pprint import pprint


def compare_time_circle(canvas, algorithm_funcs, data):
    data_checked = get_data_spectrum_circle(data)
    if not data_checked:
        return None

    matplotlib.use('TkAgg')
    plt.figure(2)
    plt.get_current_fig_manager().set_window_title('Зависимость времени построения окржуности от радиуса')
    plt.get_current_fig_manager().toolbar.pack_forget()
    plt.get_current_fig_manager().resize(700, 700)

    x, y, r1 = data_checked[0], data_checked[1], data_checked[2]
    r2, n = data_checked[3], data_checked[4]

    values = []
    step = (r2 - r1) / (n - 1)
    iters = 100

    for index, func in enumerate(algorithm_funcs):
        r_cur = r1
        cur_values = []
        if index != 4:
            for i in range(n):
                total = 0
                for _ in range(iters):
                    start = time.time()
                    func(x, y, r_cur)
                    finish = time.time() - start
                    total += finish

                cur_values.append(total / iters)
                r_cur += step
            values.append(cur_values)
        else:
            for i in range(n):
                total = 0
                for _ in range(iters):
                    start = time.time()
                    func([x - r_cur, y - r_cur, x + r_cur, y + r_cur])
                    finish = time.time() - start
                    total += finish

                cur_values.append(total / iters)
                r_cur += step
            values.append(cur_values)
            canvas.delete_all()

    data = dict()
    for i in range(5):
        data[algorithms[i]] = values[i]
    df = pd.DataFrame(data)
    radius = np.arange(r1, r2 + 1, step)

    plt.plot(radius, df)
    plt.legend(data, loc=2)
    plt.xlabel('Радиус')
    plt.ylabel('Время')
    plt.show()


def compare_time_ellipse(canvas, algorithm_funcs, data, choice):
    data_checked = get_data_spectrum_ellipse(data)
    if not data_checked:
        return None

    matplotlib.use('TkAgg')
    plt.figure(2)
    plt.get_current_fig_manager().set_window_title('Зависимость времени построения эллипса от полуоси')
    plt.get_current_fig_manager().toolbar.pack_forget()
    plt.get_current_fig_manager().resize(700, 700)

    x, y, t1, t2 = data_checked[0], data_checked[1], data_checked[2], data_checked[3]
    t, n = data_checked[4], data_checked[5]

    values = []
    step = (t2 - t1) / (n - 1)
    iters = 100

    for index, func in enumerate(algorithm_funcs):
        t_cur = t1
        cur_values = []
        if index != 4:
            for i in range(n):
                total = 0
                for _ in range(iters):
                    if choice == 0:
                        start = time.time()
                        func(x, y, t_cur, t)
                        finish = time.time() - start
                        total += finish
                    else:
                        start = time.time()
                        func(x, y, t, t_cur)
                        finish = time.time() - start
                        total += finish
                cur_values.append(total / iters)
                t_cur += step
            values.append(cur_values)
        else:
            for i in range(n):
                total = 0
                for _ in range(iters):
                    if choice == 0:
                        start = time.time()
                        func(x - abs(t1), y + abs(t), x + abs(t2), y - abs(t))
                        finish = time.time() - start
                        total += finish
                    else:
                        start = time.time()
                        func(x - abs(t), y + abs(t1), x + abs(t), y - abs(t2))
                        finish = time.time() - start
                        total += finish
                cur_values.append(total / iters)
                t_cur += step
            values.append(cur_values)
            canvas.delete_all()

    data = dict()
    for i in range(5):
        data[algorithms[i]] = values[i]

    df = pd.DataFrame(data)
    axis = np.arange(t1, t2 + 1, step)

    plt.plot(axis, df)
    plt.legend(data, loc=2)

    if choice == 0:
        plt.xlabel('Полуось a')
    else:
        plt.xlabel('Полуось b')

    plt.ylabel('Время')
    plt.show()
