from algorithms_circle import get_data_circle, canonical_circle, parametric_circle
from algorithms_circle import bresenham_circle, midpoint_circle, get_data_spectrum_circle
from algorithms_ellipse import get_data_ellipse, canonical_ellipse, parametric_ellipse
from algorithms_ellipse import bresenham_ellipse, midpoint_ellipse, get_data_spectrum_ellipse
from config import *
from data import colors
import tkinter as tk
import tkinter.messagebox as mb
from pprint import pprint


class CanvasCirclesClass(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = CANVAS_WIDTH
        self.height = CANVAS_HEIGHT
        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')

    def delete_all(self):
        self.delete('all')

    def set_pixel(self, x, y, color):
        self.create_rectangle((x, y) * 2, outline='', fill=color)
        # self.create_line(x, y, x + 1, y, fill=color)

    def draw_by_algo(self, values, algorithm, color):
        fill = list(colors.values())[color]
        if algorithm < 0:
            # values = [value for dot in values for value in dot]
            for i in range(0, len(values) - 3, 2):
                self.create_line(values[i], values[i + 1], values[i + 2], values[i + 3], fill=fill)
            # self.create_polygon(values, outline=fill, fill='')
        elif algorithm < 4:
            for i in range(0, len(values), 2):
                self.set_pixel(values[i], values[i + 1], fill)
        elif algorithm == 4:
            self.create_oval(*values, outline=fill)

    def draw_circle(self, data, algorithm, color):
        data_checked = get_data_circle(data)
        if not data_checked:
            return None
        x, y, r = data_checked[0], data_checked[1], data_checked[2]
        values = []

        if algorithm == 0:
            values = canonical_circle(x, y, r)
        elif algorithm == 1:
            values = parametric_circle(x, y, r)
        elif algorithm == 2:
            values = bresenham_circle(x, y, r)
        elif algorithm == 3:
            values = midpoint_circle(x, y, r)
        elif algorithm == 4:
            values = [x - r, y - r, x + r, y + r]

        self.draw_by_algo(values, algorithm, color)

    def draw_ellipse(self, data, algorithm, color):
        data_checked = get_data_ellipse(data)
        if not data_checked:
            return None
        x, y, a, b = data_checked[0], data_checked[1], data_checked[2], data_checked[3]
        values = []

        if algorithm == 0:
            values = canonical_ellipse(x, y, a, b)
        elif algorithm == 1:
            values = parametric_ellipse(x, y, a, b)
        elif algorithm == 2:
            values = bresenham_ellipse(x, y, a, b)
        elif algorithm == 3:
            values = midpoint_ellipse(x, y, a, b)
        elif algorithm == 4:
            values = [x - abs(a), y + abs(b), x + abs(a), y - abs(b)]

        self.draw_by_algo(values, algorithm, color)

    def draw_spectrum_circle(self, data, algorithm, color):
        data_checked = get_data_spectrum_circle(data)
        if not data_checked:
            return None

        x, y, r1 = data_checked[0], data_checked[1], data_checked[2]
        r2, n = data_checked[3], data_checked[4]
        step = (r2 - r1) / (n - 1)
        for _ in range(n):
            self.draw_circle([x, y, r1], algorithm, color)
            r1 += step

    def draw_spectrum_ellipse(self, data, choice, algorithm, color):
        data_checked = get_data_spectrum_ellipse(data)
        if not data_checked:
            return None

        x, y, t1, t2 = data_checked[0], data_checked[1], data_checked[2], data_checked[3]
        t, n = data_checked[4], data_checked[5]

        step = (t2 - t1) / (n - 1)
        if choice == 0:
            for i in range(n):
                self.draw_ellipse([x, y, t1, t], algorithm, color)
                t1 += step
        else:
            for i in range(n):
                self.draw_ellipse([x, y, t, t1], algorithm, color)
                t1 += step
