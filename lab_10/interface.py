import lab_10.algorithm as alg
import lab_10.canvas as cv
import lab_10.config as cfg
from lab_10.config import FONT, FONT_BOLD, PADX, PADY, FUNCS
import numpy as np
import tkinter as tk
import tkinter.colorchooser as cch


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = cv.Canvas(self)
        self.add_canvas()

        self.x = [-10, 10, 0.1]
        self.z = [-10, 10, 0.1]
        self.scale = 50

        self.frame_color = tk.Frame(self)
        self.color = 'black'
        self.color_win = None
        self.add_color()

        self.frame_funcs = tk.Frame(self)
        self.func = tk.IntVar()
        self.func.set(0)
        self.add_funcs()

        self.frame_buttons = tk.Frame(self)
        self.add_buttons()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=4, padx=5, pady=5)

    def add_color(self):
        cfg.create_label(self.frame_color, 'ЦВЕТ: ', FONT_BOLD, 0, 0, PADX, 4, tk.N, 'groove')
        self.color_win = cfg.create_button(self.frame_color, '', FONT, 1, 0, PADX, 0, 1, 'WE',
                                           self.choose_color, self.color)

        self.frame_color.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def choose_color(self):
        self.color = cch.askcolor()[1]
        self.color_win.config(**{'background': self.color, 'activebackground': self.color})

    def add_funcs(self):
        cfg.create_label(self.frame_funcs, 'ФУНКЦИЯ: ', FONT_BOLD, 0, 0, PADX, 4, tk.N, 'groove')
        for i, func in enumerate(FUNCS):
            cfg.create_radiobutton(self.frame_funcs, self.func, i, func, FONT, i + 1, 0, PADX, 0, 'WN')

        self.frame_funcs.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def add_buttons(self):
        cfg.create_button(self.frame_buttons, 'ПРИМЕНИТЬ', FONT, 0, 0, PADX, PADY, 1, 'WE', self.draw_func)
        cfg.create_button(self.frame_buttons, 'ОЧИСТИТЬ ХОЛСТ', FONT, 1, 0, PADX, PADY, 1, 'WE', self.canvas.delete_all)

        self.frame_buttons.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def draw_func(self):
        f = alg.get_funcs()[self.func.get()]
        high_horizon = [0 for _ in range(900)]
        low_horizon = [900 for _ in range(900)]
        z_from, z_to, z_step = self.z[0], self.z[1], self.z[2]
        x_from, x_to, x_step = self.x[0], self.x[1], self.x[2]

        for z in np.arange(z_from, z_to + z_step, z_step):
            self.canvas.draw_horizon(f, high_horizon, low_horizon, x_from, x_to, x_step, z)

        for z in np.arange(z_from, z_to, z_step):
            p1 = self.canvas.transform_point([x_from, f(x_from, z), z])
            p2 = self.canvas.transform_point([x_from, f(x_from, z + z_step), z + z_step])
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=self.color)
            p1 = self.canvas.transform_point([x_to, f(x_to, z), z])
            p2 = self.canvas.transform_point([x_to, f(x_to, z + z_step), z + z_step])
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=self.color)
