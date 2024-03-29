import lab_10.algorithm as alg
import math
import numpy as np
import time
import tkinter as tk
import tkinter.messagebox as mb


class Canvas(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = 900
        self.height = 750

        self.transform_matrix = [[int(i == j) for i in range(4)] for j in range(4)]

        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')

    def delete_all(self):
        self.transform_matrix = [[int(i == j) for i in range(4)] for j in range(4)]
        self.delete('all')

    def set_pixel(self, x, y):
        self.create_line(x, y, x + 1, y + 1, fill=self.frame.color)

    def draw_point(self, x, y, hh, lh):
        if not alg.is_visible([x, y]):
            return False

        if y > hh[x]:
            hh[x] = y
            self.set_pixel(x, y)

        elif y < lh[x]:
            lh[x] = y
            self.set_pixel(x, y)

        return True

    def draw_horizon_part(self, p1, p2, hh, lh):
        if p1[0] > p2[0]:
            p1, p2 = p2, p1

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        if dx > dy:
            length = dx
        else:
            length = dy

        dx /= length
        dy /= length

        x, y = p1[0], p1[1]

        for _ in range(int(length) + 1):
            if not self.draw_point(int(round(x)), y, hh, lh):
                return
            x += dx
            y += dy

    def draw_horizon(self, func, hh, lh, _from, to, step, z):
        def f(_x):
            return func(_x, z)

        prev = None
        for x in np.arange(_from, to + step, step):
            current = self.transform_point([x, f(x), z])
            if prev:
                self.draw_horizon_part(prev, current, hh, lh)
            prev = current

    def transform_point(self, point):
        point.append(1)
        res_point = [0, 0, 0, 0]
        for i in range(4):
            for j in range(4):
                res_point[i] += point[j] * self.transform_matrix[j][i]

        try:
            for i in range(3):
                res_point[i] *= float(self.frame.scale.get())
        except ValueError:
            return mb.showerror('Ошибка', 'Проверьте значени коэффициента')

        res_point[0] += 900 / 2
        res_point[1] += 750 / 2

        return res_point[:3]

    def rotate_x(self):
        try:
            value = float(self.frame.ox.get()) / 180 * math.pi
        except ValueError:
            return mb.showerror('Ошибка', 'Проверьте значени коэффициента')

        rotate_matrix = [
            [1, 0, 0, 0],
            [0, math.cos(value), math.sin(value), 0],
            [0, -math.sin(value), math.cos(value), 0],
            [0, 0, 0, 1]
        ]

        self.transform_matrix = alg.rotate_matrix(self.transform_matrix, rotate_matrix)
        self.frame.draw_func()

    def rotate_y(self):
        try:
            value = float(self.frame.oy.get()) / 180 * math.pi
        except ValueError:
            return mb.showerror('Ошибка', 'Проверьте значени коэффициента')

        rotate_matrix = [
            [math.cos(value), 0, -math.sin(value), 0],
            [0, 1, 0, 0],
            [math.sin(value), 0, math.cos(value), 0],
            [0, 0, 0, 1]
        ]

        self.transform_matrix = alg.rotate_matrix(self.transform_matrix, rotate_matrix)
        self.frame.draw_func()

    def rotate_z(self):
        try:
            value = float(self.frame.oz.get()) / 180 * math.pi
        except ValueError:
            return mb.showerror('Ошибка', 'Проверьте значени коэффициента')

        rotate_matrix = [
            [math.cos(value), math.sin(value), 0, 0],
            [-math.sin(value), math.cos(value), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        self.transform_matrix = alg.rotate_matrix(self.transform_matrix, rotate_matrix)
        self.frame.draw_func()
