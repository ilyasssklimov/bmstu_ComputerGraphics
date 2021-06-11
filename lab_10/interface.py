import lab_10.algorithm as alg
import canvas as cv
import config as cfg
from config import FONT, FONT_BOLD, PADX, PADY, FUNCS
import numpy as np
import tkinter as tk
import tkinter.colorchooser as cch
import tkinter.ttk as ttk
import tkinter.messagebox as mb


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = cv.Canvas(self)
        self.add_canvas()

        self.x = [-10, 10, 0.1]
        self.z = [-10, 10, 0.1]
        self.ox = 0
        self.oy = 0
        self.oz = 0
        self.scale = None

        self.frame_color = tk.Frame(self)
        self.color = 'black'
        self.color_win = None
        self.add_color()

        self.frame_funcs = tk.Frame(self)
        self.func = tk.IntVar()
        self.func.set(0)
        self.add_funcs()

        self.frame_limits = tk.Frame(self)
        self.dx = []
        self.dz = []
        self.add_limits()

        self.frame_entries = tk.Frame(self)
        self.add_entry()

        self.frame_buttons = tk.Frame(self)
        self.add_buttons()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=5, padx=5, pady=5)

    def add_color(self):
        cfg.create_label(self.frame_color, 'ЦВЕТ: ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        self.color_win = cfg.create_button(self.frame_color, '', FONT, 1, 0, PADX, 0, 1, 'WE',
                                           self.choose_color, self.color)

        self.frame_color.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def choose_color(self):
        self.color = cch.askcolor()[1]
        self.color_win.config(**{'background': self.color, 'activebackground': self.color})

    def add_funcs(self):
        cfg.create_label(self.frame_funcs, 'ФУНКЦИЯ: ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        for i, func in enumerate(FUNCS):
            cfg.create_radiobutton(self.frame_funcs, self.func, i, func, FONT, i + 1, 0, PADX, 0, 'WN')

        self.frame_funcs.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def add_limits(self):
        cfg.create_label(self.frame_limits, 'ПРЕДЕЛЫ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove', 4)
        cfg.create_label(self.frame_limits, 'ОТ', FONT, 1, 1, 0, 0, tk.N, 'groove')
        cfg.create_label(self.frame_limits, 'ДО', FONT, 1, 2, 0, 0, tk.N, 'groove')
        cfg.create_label(self.frame_limits, 'ШАГ', FONT, 1, 3, 0, 0, tk.N, 'groove')

        cfg.create_label(self.frame_limits, 'ПО Х:', FONT, 2, 0, 0, 0, tk.N, 'groove')
        self.dx.append(cfg.create_entry(self.frame_limits, FONT, 2, 1, PADX, PADY, tk.N, 4))
        self.dx[0].insert(0, '-10')
        self.dx.append(cfg.create_entry(self.frame_limits, FONT, 2, 2, PADX, PADY, tk.N, 4))
        self.dx[1].insert(0, '10')
        self.dx.append(cfg.create_entry(self.frame_limits, FONT, 2, 3, PADX, PADY, tk.N, 4))
        self.dx[2].insert(0, '0.1')

        cfg.create_label(self.frame_limits, 'ПО Y:', FONT, 3, 0, 0, 0, tk.N, 'groove')
        self.dz.append(cfg.create_entry(self.frame_limits, FONT, 3, 1, PADX, PADY, tk.N, 4))
        self.dz[0].insert(0, '-10')
        self.dz.append(cfg.create_entry(self.frame_limits, FONT, 3, 2, PADX, PADY, tk.N, 4))
        self.dz[1].insert(0, '10')
        self.dz.append(cfg.create_entry(self.frame_limits, FONT, 3, 3, PADX, PADY, tk.N, 4))
        self.dz[2].insert(0, '0.1')

        cfg.create_button(self.frame_limits, 'ПРИМЕНИТЬ', 'Times 10', 4, 0, PADX, PADY, 4, 'WE', self.change_limits)

        self.frame_limits.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def add_entry(self):
        cfg.create_label(self.frame_entries, 'ПОВОРОТ ВОКРУГ ОСЕЙ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove', 3)

        cfg.create_label(self.frame_entries, 'ПО Х:', FONT, 1, 0, PADX, PADY, tk.N)
        self.ox = cfg.create_entry(self.frame_entries, FONT, 1, 1, PADX, PADY, tk.N, 5)
        self.ox.insert(0, '0')
        cfg.create_button(self.frame_entries, 'ПРИМЕНИТЬ', 'Times 10', 1, 2, PADX, PADY, 1, 'WE', self.canvas.rotate_x)

        cfg.create_label(self.frame_entries, 'ПО Y:', FONT, 2, 0, PADX, PADY, tk.N)
        self.oy = cfg.create_entry(self.frame_entries, FONT, 2, 1, PADX, PADY, tk.N, 5)
        self.oy.insert(0, '0')
        cfg.create_button(self.frame_entries, 'ПРИМЕНИТЬ', 'Times 10', 2, 2, PADX, PADY, 1, 'WE', self.canvas.rotate_y)

        cfg.create_label(self.frame_entries, 'ПО Z:', FONT, 3, 0, PADX, PADY, tk.N)
        self.oz = cfg.create_entry(self.frame_entries, FONT, 3, 1, PADX, PADY, tk.N, 5)
        self.oz.insert(0, '0')
        cfg.create_button(self.frame_entries, 'ПРИМЕНИТЬ', 'Times 10', 3, 2, PADX, PADY, 1, 'WE', self.canvas.rotate_z)

        ttk.Separator(self.frame_entries, orient='horizontal').grid(row=4, column=0, columnspan=3, pady=8, sticky='WE')
        cfg.create_label(self.frame_entries, 'МАСШТАБИРОВАНИЕ', FONT_BOLD, 5, 0, PADX, PADY, tk.N, 'groove', 3)

        cfg.create_label(self.frame_entries, 'K:', FONT, 6, 0, PADX, PADY, tk.N)
        self.scale = cfg.create_entry(self.frame_entries, FONT, 6, 1, PADX, PADY, tk.N, 5)
        self.scale.insert(0, '50')
        cfg.create_button(self.frame_entries, 'ПРИМЕНИТЬ', 'Times 10', 6, 2, PADX, PADY, 1, 'WE', self.draw_func)

        self.frame_entries.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N)

    def add_buttons(self):
        cfg.create_button(self.frame_buttons, 'НАРИСОВАТЬ', FONT, 0, 0, PADX, PADY, 1, 'WE', self.draw_func)
        cfg.create_button(self.frame_buttons, 'ОЧИСТИТЬ ХОЛСТ', FONT, 1, 0, PADX, PADY, 1, 'WE', self.canvas.delete_all)

        self.frame_buttons.grid(row=4, column=1, padx=5, pady=5, sticky=tk.N)

    def draw_func(self):
        self.canvas.delete('all')
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

    def change_limits(self):
        try:
            x0 = float(self.dx[0].get())
            x1 = float(self.dx[1].get())
            dx = float(self.dx[2].get())
            z0 = float(self.dz[0].get())
            z1 = float(self.dz[1].get())
            dz = float(self.dz[2].get())
        except ValueError:
            return mb.showerror('Ошибка', 'Проверьте значения коэффициентов')

        self.x[0] = x0
        self.x[1] = x1
        self.x[2] = dx
        self.z[0] = z0
        self.z[1] = z1
        self.z[2] = dz

        self.draw_func()
